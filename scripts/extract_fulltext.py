#!/usr/bin/env python3
"""Build faithful, readable article fragments from the site's clean source PDFs.

The layout model supplies column order and paragraph/section boundaries. Its
formula, table, and figure crops are retained as images; mathematically dense
paragraphs with damaged font extraction also receive an exact source crop and
an explicit, visible transcription disclosure. No prose is generated or rewritten.
"""
from __future__ import annotations

import argparse
import base64
import html
import io
import json
from pathlib import Path
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup
from PIL import Image
import markdown
import pymupdf
import pymupdf4llm

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'content'
CACHE = ROOT / '.fulltext-cache'


def clean_text(text: str) -> str:
    # These PDF ligatures have ordinary Unicode equivalents. Preserve all other
    # scientific symbols and wording; C0 font-control glyphs cannot be displayed.
    for old, new in {'\ufb00': 'ff', '\ufb01': 'fi', '\ufb02': 'fl', '\ufb03': 'ffi', '\ufb04': 'ffl'}.items():
        text = text.replace(old, new)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)
    text = text.replace('\u00ad', '')
    return text


def compact_image(data: bytes) -> str:
    im = Image.open(io.BytesIO(data)).convert('RGB')
    target = io.BytesIO()
    # Lossless WebP keeps equation and table characters sharp and is markedly
    # smaller than the intermediate PNGs. The pixel dimensions are unchanged.
    im.save(target, format='WEBP', lossless=True, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(target.getvalue()).decode()


def crop(page, bbox, padding=2) -> str:
    rect = pymupdf.Rect(bbox) + (-padding, -padding, padding, padding)
    rect &= page.rect
    return compact_image(page.get_pixmap(matrix=pymupdf.Matrix(2, 2), clip=rect, alpha=False).tobytes('png'))


def transcription(page, bbox) -> str:
    text = clean_text(page.get_textbox(pymupdf.Rect(bbox)))
    text = re.sub(r'(?<=[a-z])\-\n(?=[a-z])', '', text)
    return re.sub(r'\s+', ' ', text).strip().replace('\ufffd', '[unmapped symbol]')


def bad_math_paragraph(text: str) -> bool:
    spans = re.findall(r'<sup>(.*?)</sup>', text, re.S)
    return ('\ufffd' in text or any(len(re.findall(r'[A-Za-z]{3,}', s)) > 5 for s in spans)
            or len(spans) >= 10)


def process_page(chunk: dict, page, number: int) -> str:
    text = chunk['text']
    # Replace only clearly damaged math-heavy text blocks. Retaining the source
    # crop prevents an extracted superscript from silently changing a theorem.
    replacements = []
    inline_images = []
    for item in page.get_images():
        for rect in page.get_image_rects(item[0]):
            if rect.width <= 32 and rect.height <= 32:
                inline_images.append(rect)
    for box in chunk.get('page_boxes', []):
        if box['class'] in ('page-header', 'page-footer'):
            # A genuine section can occur at a column's bottom and be mistaken
            # for a page footer. Recover section labels from the actual PDF.
            bbox = pymupdf.Rect(box['bbox']) + (-2, -2, 2, 2)
            raw = clean_text(page.get_textbox(bbox)).strip()
            if re.match(r'^(?:[IVX]+\.|[A-Z]\.|\d+(?:\.\d+)*\.?)\s+[A-Za-z]', raw) and len(raw.split()) >= 3:
                raw = re.sub(r'\s+', ' ', raw)
                # Locate its real column break in the reading stream.
                later = [b for b in chunk['page_boxes']
                         if b['class'] not in ('page-header', 'page-footer')
                         and (b['bbox'][0] > box['bbox'][2] + 20
                              or (abs(b['bbox'][0] - box['bbox'][0]) < 80 and b['bbox'][1] > box['bbox'][3]))]
                at = min((b['pos'][0] for b in later), default=len(text))
                replacements.append((at, at, '\n\n## ' + raw + '\n\n'))
            continue
        if box['class'] not in ('text', 'list-item', 'table'):
            continue
        a, b = box['pos']
        original = text[a:b]
        bounds = pymupdf.Rect(box['bbox']) + (-3, -3, 3, 3)
        if box['class'] == 'table' and bounds.x1 > page.rect.width / 2:
            # Inline emoji cells can extend beyond the text-only table bounds.
            bounds.x1 = min(page.rect.width, bounds.x1 + 36)
        symbols = [rect for rect in inline_images if bounds.intersects(rect)]
        has_inline_symbols = bool(symbols)
        if original.strip() and (bad_math_paragraph(original) or has_inline_symbols):
            raw = transcription(page, box['bbox'])
            label = 'Passage with inline symbols' if has_inline_symbols else 'Mathematical passage'
            if box['class'] == 'table':
                label = 'Table with inline symbols'
            crop_bounds = pymupdf.Rect(box['bbox'])
            for symbol in symbols:
                crop_bounds |= symbol
            replacement = ('\n\n<figure class="source-excerpt math-excerpt">'
                f'<img src="{crop(page, crop_bounds)}" alt="{label} from PDF page {number}" loading="lazy">'
                f'<figcaption><a href="paper.pdf#page={number}">{label}, PDF page {number}</a></figcaption>'
                '</figure>\n\n<details class="text-transcription"><summary>Extracted text transcription of this passage</summary>'
                + (original if box['class'] == 'table' else f'<p>{html.escape(raw)}</p>')
                + '</details>\n\n')
            replacements.append((a, b, replacement))
    # Positions refer to the unmodified Markdown; apply back to front.
    for a, b, replacement in sorted(replacements, key=lambda r: r[0], reverse=True):
        text = text[:a] + replacement + text[b:]
    rendered = markdown.markdown(clean_text(text), extensions=['tables', 'fenced_code', 'sane_lists'])
    soup = BeautifulSoup(rendered, 'html.parser')
    for image in soup.find_all('img'):
        src = image.get('src', '')
        if src.startswith('data:image/png;base64,'):
            image['src'] = compact_image(base64.b64decode(src.split(',', 1)[1]))
        if not image.get('alt'):
            image['alt'] = f'Figure, table, or displayed equation from PDF page {number}'
        image['loading'] = 'lazy'
        # Ordinary text captions immediately following the original PDF image
        # are left in the article, rather than being guessed from its pixels.
    for heading in soup.find_all(re.compile('^h[1-6]$')):
        title = heading.get_text(' ', strip=True)
        # Full-text wrapper uses h2; section and subsection headings begin h3.
        heading.name = 'h4' if re.match(r'^\d+\.\d+', title) else 'h3'
    for table in soup.find_all('table'):
        table['class'] = list(table.get('class', [])) + ['article-table']
        wrapper = soup.new_tag('div', attrs={'class': 'table-scroll', 'role': 'region', 'aria-label': f'Table from PDF page {number}', 'tabindex': '0'})
        table.wrap(wrapper)
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith(('javascript:', 'file:')):
            del link['href']
    # Author-affiliation footnotes belong below the page's body, rather than
    # between the last line of the left column and its right-column continuation.
    for p in list(soup.find_all('p')):
        if p.get_text(' ', strip=True).startswith('The authors are with the Computer, Electrical and Mathematical Sciences'):
            aside = soup.new_tag('aside', attrs={'class': 'source-footnote'})
            p.wrap(aside)
            aside.extract()
            soup.append(aside)
    return str(soup)


def repair_known_layout(slug: str, number: int, chunk: dict) -> dict:
    if slug == 'cross-cultural-emojis' and number == 15:
        # Tables in the right column caused row-wise rather than column-wise
        # ordering. Read the complete left column, then the complete right.
        boxes = [b for b in chunk['page_boxes'] if b['pos'][1] > b['pos'][0]]
        boxes.sort(key=lambda b: (b['bbox'][0] > 300, b['bbox'][1]))
        text, reordered = '', []
        for box in boxes:
            a, b = box['pos']
            segment = chunk['text'][a:b]
            reordered.append(dict(box, pos=[len(text), len(text) + len(segment)]))
            text += segment
        chunk = dict(chunk, text=text, page_boxes=reordered)
    # On the survey's final page the short right column begins with the final
    # URL of ref212 and ref213. The layout model reads it before refs194–212.
    # Move those original strings, without altering any bibliographic wording.
    if slug == 'stablecoins' and number == 35:
        text = chunk['text']
        match = re.search(r'(https://www\.techpolicy\.press/twitter-api-changes-set-to-d.*?)(?=\n- \[194\])', text, re.S)
        if match:
            tail = match.group(1)
            text = text[:match.start()] + text[match.end():]
            chunk = dict(chunk, text=text.rstrip() + '\n\n' + tail.strip() + '\n')
            # The moved references are ordinary prose; old offsets no longer
            # apply. There are no formulas, tables, or suppressed headings here.
            chunk['page_boxes'] = []
    return chunk


CHART_REGIONS = {
    ('prediction-market-launch', 5): (315,78,562,205),
    ('prediction-market-launch', 7): (315,300,562,430),
    ('pumpsense', 5): (46,576,304,699),
    ('stablecoins', 3): (309,490,567,668),
    ('stablecoins', 6): (309,570,567,731),
    ('stablecoins', 11): (309,432,567,590),
}


def repair_chart_regions(slug: str, number: int, chunk: dict, page) -> dict:
    """Retain exact plots when their axes were also classified as tables."""
    region = CHART_REGIONS.get((slug, number))
    if region is None:
        return chunk
    rect = pymupdf.Rect(region)
    text, boxes, inserted = '', [], False
    for box in chunk['page_boxes']:
        a, b = box['pos']
        segment = chunk['text'][a:b]
        bounds = pymupdf.Rect(box['bbox'])
        overlap = bounds & rect
        is_chart = (box['class'] in ('picture', 'table') and not overlap.is_empty
                    and overlap.get_area() / bounds.get_area() > .8)
        if is_chart:
            if inserted:
                continue
            segment = (f'\n\n<figure class="source-excerpt"><img src="{crop(page, rect)}" '
                       f'alt="Complete chart from PDF page {number}, including original axes and labels" loading="lazy"></figure>\n\n')
            box = dict(box, **{'class': 'picture', 'bbox': list(region)})
            inserted = True
        boxes.append(dict(box, pos=[len(text), len(text) + len(segment)]))
        text += segment
    return dict(chunk, text=text, page_boxes=boxes)


def start_at_introduction(fragment: str) -> tuple[str, bool]:
    soup = BeautifulSoup(fragment, 'html.parser')
    intro = next((h for h in soup.find_all(['h3', 'h4'])
                  if re.match(r'^(?:(?:\d+|[IVX]+)[.\s]*)?Introduction\b', h.get_text(' ', strip=True), re.I)), None)
    if intro is None:
        return fragment, False
    siblings = list(soup.contents)
    # Heading is normally a root element. If a converter wrapper intervenes,
    # retain the parent containing it and avoid deleting any body prose.
    node = intro
    while node.parent is not soup:
        node = node.parent
    return ''.join(str(x) for x in siblings[siblings.index(node):]), True


def cleanup_fragment(slug: str, number: int, fragment: str, page=None) -> str:
    soup = BeautifulSoup(fragment, 'html.parser')
    if slug == 'reflexivity-threshold' and number == 7 and page is not None:
        caption = next((p for p in soup.find_all('p') if p.get_text(' ', strip=True).startswith('Figure 1: The reflexivity threshold.')), None)
        if caption is not None:
            caption_html = str(caption)
            # Only the complete top figure precedes this caption. Its chart axes
            # were also misread as numeric tables; preserve the actual plotted
            # figure and captions, then resume the proof immediately below it.
            for node in list(caption.previous_siblings):
                node.extract()
            exact = BeautifulSoup(f'<figure class="source-excerpt"><img src="{crop(page, (105,65,508,291))}" alt="Figure 1: complete reflexivity-threshold plots with axes, legends, panel captions, and figure caption" loading="lazy"><figcaption>{caption_html}</figcaption></figure>', 'html.parser')
            caption.replace_with(exact)
    if slug == 'finmoji':
        for p in list(soup.find_all('p')):
            if number > 1 and p.get_text(' ', strip=True) == 'FinMoji: A Framework for Emoji-driven Sentiment Analysis in Financial Social Media':
                p.decompose()
    if slug == 'finmoji' and number == 31:
        # Author-manuscript running footer, not the final reference's wording.
        for node in soup.find_all(string=re.compile(r', 29 pages\.\s*$')):
            node.replace_with(re.sub(r', 29 pages\.\s*$', '', str(node)))
    if slug == 'cross-cultural-emojis' and number == 12 and page is not None:
        for figure in list(soup.find_all('figure', class_='math-excerpt')):
            image = figure.find('img')
            if image and image.get('alt', '').startswith('Table with inline symbols'):
                figure.decompose()
        table = soup.find('table')
        if table is not None:
            container = table.parent if table.parent.get('class') == ['table-scroll'] else table
            details = soup.new_tag('details', attrs={'class': 'text-transcription'})
            summary = soup.new_tag('summary')
            summary.string = 'Extracted table text'
            details.append(summary)
            container.wrap(details)
            exact = BeautifulSoup(f'<figure class="source-excerpt"><img src="{crop(page, (70,70,526,205))}" alt="Table 7 including each dataset’s top-five emoji symbols" loading="lazy"></figure>', 'html.parser')
            details.insert_before(exact)
            # Standalone glyphs were detached from the semantic table rows.
            for image in list(soup.find_all('img')):
                if image.find_parent('figure') is None:
                    parent = image.parent
                    image.decompose()
                    if parent.name == 'p' and not parent.get_text(strip=True):
                        parent.decompose()
    if slug == 'financial-microblog-emojis' and number == 2 and page is not None:
        figure = next((f for f in soup.find_all('figure') if f.find('img') and f.find('img').get('alt', '').startswith('Table with inline symbols')), None)
        if figure is not None:
            figure.find('img')['src'] = crop(page, (335,95,537,142))
        for image in list(soup.find_all('img')):
            if image.find_parent('figure') is not None:
                continue
            src = image.get('src', '')
            if src.startswith('data:image/'):
                im = Image.open(io.BytesIO(base64.b64decode(src.split(',', 1)[1])))
                if im.width < 45 and im.height < 45:
                    parent = image.parent
                    image.decompose()
                    if parent.name == 'p' and not parent.get_text(strip=True):
                        parent.decompose()
    if slug == 'cross-cultural-emojis' and number == 16 and page is not None:
        captions = {str(p.get_text(' ', strip=True)[:8]): p for p in soup.find_all('p')
                    if p.get_text(' ', strip=True).startswith(('Figure 3:', 'Figure 4:', 'Table 11:'))}
        table11 = next((p for p in soup.find_all('p') if p.get_text(' ', strip=True).startswith('Table 11:')), None)
        if table11 is not None:
            tail = [str(table11)] + [str(x) for x in table11.next_siblings]
            figures = []
            for n, rect in [(3,(70,70,526,307)),(4,(70,347,526,585))]:
                caption = next((p for p in soup.find_all('p') if p.get_text(' ', strip=True).startswith(f'Figure {n}:')), None)
                figures.append(f'<figure class="source-excerpt"><img src="{crop(page, rect)}" alt="Figure {n}: complete heatmap including emoji and community labels" loading="lazy"><figcaption>{str(caption) if caption else ""}</figcaption></figure>')
            soup = BeautifulSoup(''.join(figures + tail), 'html.parser')
    if slug == 'tstr-financial-fraud' and number == 1:
        frontmatter = soup.new_tag('aside', attrs={'class': 'source-footnote'})
        for heading in list(soup.find_all(['h3','h4'])):
            label = heading.get_text(' ', strip=True)
            if label in ('Abstract','CCS Concepts','Keywords','ACM Reference Format:'):
                following = heading.find_next_sibling()
                if label == 'Abstract':
                    heading.decompose()
                    if following and following.name == 'p':
                        following.decompose()
                else:
                    frontmatter.append(heading.extract())
                    if following and following.name == 'p':
                        frontmatter.append(following.extract())
        for p in list(soup.find_all('p')):
            label = p.get_text(' ', strip=True)
            if label.startswith(('∗Corresponding author.', 'This work is licensed under', '© 2025 Copyright', 'https://doi.org/10.1145/3768292.3770393')):
                frontmatter.append(p.extract())
        soup.append(frontmatter)
    if slug == 'tstr-financial-fraud' and number == 8:
        heading = next((h for h in soup.find_all(['h3','h4']) if h.get_text(' ', strip=True) == 'Artifact Availability'), None)
        artifact = next((p for p in soup.find_all('p') if p.get_text(' ', strip=True).startswith('Code and data used')), None)
        if heading and artifact:
            heading.insert_after(artifact.extract())
    return str(soup)


def extract(slug: str, force: bool = False) -> dict:
    source = ROOT / 'docs' / 'papers' / slug / 'paper.pdf'
    doc = pymupdf.open(source)
    cache_path = CACHE / f'{slug}.json'
    if cache_path.exists() and not force:
        chunks = json.loads(cache_path.read_text())
    else:
        chunks = pymupdf4llm.to_markdown(str(source), page_chunks=True,
                    embed_images=True, dpi=144, header=False, footer=False,
                    show_progress=False, use_ocr=False, table_output='html')
        cache_path.write_text(json.dumps(chunks, ensure_ascii=False))
    parts = []
    intro_found = False
    for i, chunk in enumerate(chunks):
        number = i + 1
        chunk = repair_known_layout(slug, number, chunk)
        chunk = repair_chart_regions(slug, number, chunk, doc[i])
        fragment = process_page(chunk, doc[i], number)
        fragment = cleanup_fragment(slug, number, fragment, doc[i])
        if i == 0:
            fragment, intro_found = start_at_introduction(fragment)
        parts.append(f'<section class="source-page" id="fulltext-page-{number}" aria-label="PDF page {number}">'
                     f'<p class="page-source"><a href="paper.pdf#page={number}">PDF page {number}</a></p>\n{fragment}\n</section>')
    final = '<div class="article-text">\n' + '\n'.join(parts) + '\n</div>\n'
    destination = OUT / f'{slug}.html'
    destination.write_text(final)
    soup = BeautifulSoup(final, 'html.parser')
    record = {'slug': slug, 'pages': len(doc), 'html_bytes': len(final.encode()),
              'images': len(soup.find_all('img')), 'words': len(soup.get_text(' ', strip=True).split()),
              'sections': [h.get_text(' ', strip=True) for h in soup.find_all(['h3', 'h4'])],
              'starts_at_introduction': intro_found,
              'source_pdf': str(source.relative_to(ROOT))}
    print(json.dumps(record), flush=True)
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('slugs', nargs='*')
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--worker', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args()
    OUT.mkdir(exist_ok=True)
    CACHE.mkdir(exist_ok=True)
    slugs = args.slugs or [p['slug'] for p in json.loads((ROOT / 'publications.json').read_text())]
    if args.worker:
        if len(slugs) != 1:
            parser.error('--worker requires exactly one paper slug')
        record = extract(slugs[0], args.force)
        (CACHE / f'{slugs[0]}.report.json').write_text(json.dumps(record, ensure_ascii=False))
        return
    if len(slugs) > 1:
        # A native layout engine can accumulate state over many documents. Each
        # worker handles one PDF and exits, bounding its memory and model state.
        def worker(slug):
            command = [sys.executable, str(Path(__file__).resolve()), '--worker', slug]
            if args.force:
                command.append('--force')
            subprocess.run(command, check=True)
            return json.loads((CACHE / f'{slug}.report.json').read_text())
        with ThreadPoolExecutor(max_workers=2) as pool:
            records = list(pool.map(worker, slugs))
    else:
        records = [extract(slugs[0], args.force)]
    report_path = OUT / 'extraction-report.json'
    existing = {r['slug']: r for r in json.loads(report_path.read_text())} if report_path.exists() else {}
    existing.update({r['slug']: r for r in records})
    order = [p['slug'] for p in json.loads((ROOT / 'publications.json').read_text())]
    report_path.write_text(json.dumps([existing[s] for s in order if s in existing], ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
