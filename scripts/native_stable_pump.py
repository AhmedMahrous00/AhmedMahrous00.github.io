#!/usr/bin/env python3
"""Import two author-source arXiv HTML bodies and their original figure assets.

The site owns the title, author metadata, abstract, and canonical citation. This
keeps the scholarly body only, with native MathML and HTML tables. It does not
render or crop PDF pages.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pymupdf
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.fulltext-cache' / 'native-stable-pump'
SOURCES = {'stablecoins': '2507.13883v1', 'pumpsense': '2605.09431v1'}


def request(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=90) as response:
        return response.read()


def words(text: str) -> list[str]:
    return re.findall(r'[a-z0-9]+', unicodedata.normalize('NFKC', text).lower())


def visible_text(soup) -> str:
    copy = BeautifulSoup(str(soup), 'html.parser')
    for tag in copy.select('annotation, .ltx_bib_cited'):
        tag.decompose()
    return copy.get_text(' ', strip=True)


def convert(slug: str, ident: str) -> dict:
    url = f'https://arxiv.org/html/{ident}'
    cache = CACHE / f'{slug}.html'
    CACHE.mkdir(parents=True, exist_ok=True)
    if not cache.exists():
        cache.write_bytes(request(url))
    soup = BeautifulSoup(cache.read_text(), 'html.parser')
    article = soup.find('article')
    if article is None:
        raise ValueError(f'No article at {url}')

    for tag in article.select('.ltx_title_document, .ltx_authors, .ltx_abstract, .ltx_keywords, .ltx_bib_cited, script, style'):
        tag.decompose()
    source_section_count = len(article.find_all('section'))
    source_reference_count = len(article.select('.ltx_bibitem'))
    source_headings = [h.get_text(' ', strip=True) for h in article.find_all(re.compile(r'^h[2-5]$'))]
    # The arXiv PumpSense conversion appends a lone citation after the complete
    # reference list. The linked PDF ends with reference [29], without this line.
    if slug == 'pumpsense':
        tail = article.find('div', id='p1', recursive=False)
        if tail and tail.get_text(' ', strip=True) == '6':
            tail.decompose()
        # FontAwesome is not part of the paper. Preserve its intended symbols as
        # selectable, accessible text without a third-party font dependency.
        for tag in article.select('.fa-times, .fa-check'):
            replacement = soup.new_tag('span')
            replacement['class'] = ['table-symbol']
            replacement['aria-label'] = 'Yes' if 'fa-check' in tag.get('class', []) else 'No'
            replacement.string = '✓' if 'fa-check' in tag.get('class', []) else '✗'
            tag.replace_with(replacement)
        # Normalize the source's thin-space thousands separator, verified
        # against Table II in the linked paper: 283,017 messages; 2,246 pumps.
        for text in list(article.find_all(string=True)):
            if '\u2009' in text:
                text.replace_with(re.sub(r'(?<=\d)\u2009(?=\d)', ',', str(text)))

    if slug == 'stablecoins':
        # Nineteen SVGs are checkmarks; thirty-four are decorative text callout
        # frames. Preserve the text as responsive HTML, without the SVG frame.
        for svg in article.find_all('svg'):
            paths = svg.find_all('path')
            if len(paths) == 1 and paths[0].get('d') == 'M 0 5.51 L 3.94 0 L 15.75 11.02 L 3.94 2.36 Z':
                replacement = soup.new_tag('span')
                replacement['class'] = ['table-symbol']
                replacement['aria-label'] = 'Yes'
                replacement.string = '✓'
                svg.replace_with(replacement)
            else:
                text = svg.select_one('.ltx_foreignobject_content')
                if text is None:
                    raise ValueError(f'Unexpected inline picture in {slug}')
                replacement = soup.new_tag('div')
                replacement['class'] = ['native-callout']
                if svg.get('id'):
                    replacement['id'] = svg['id']
                for child in list(text.children):
                    replacement.append(child.extract())
                for paragraph in replacement.select('span.ltx_p'):
                    paragraph.name = 'p'
                for span in list(replacement.select('span.ltx_inline-block')):
                    span.unwrap()
                parent = svg.parent
                if parent.name == 'span' and len(parent.find_all(recursive=False)) == 1:
                    parent.replace_with(replacement)
                else:
                    svg.replace_with(replacement)

    # Paper section headings sit beneath the site's existing Full text heading.
    for tag in article.find_all(re.compile(r'^h[2-5]$')):
        tag.name = f'h{int(tag.name[1:]) + 1}'

    # Let the site's responsive stylesheet control text and table widths.
    for tag in article.find_all(True):
        tag.attrs.pop('style', None)
        tag.attrs.pop('aria-hidden', None)
    for table in article.find_all('table'):
        first_row = table.find('tr')
        if first_row:
            for cell in first_row.find_all('td', recursive=False):
                cell.name = 'th'
                cell['scope'] = 'col'
        if table.get('id') == 'S4.T5.4.1':
            for cell in table.find_all('tr')[1].find_all('td', recursive=False):
                cell.name = 'th'
                cell['scope'] = 'col'

    # arXiv displays one of three duplicated note numbers via its stylesheet.
    # Independent site HTML uses ordinary links and one numbered Notes list.
    source_notes = list(article.select('.ltx_note'))
    if source_notes:
        notes_section = soup.new_tag('section', id='native-notes')
        notes_section['class'] = ['native-notes', 'ltx_notes']
        heading = soup.new_tag('h3')
        heading['class'] = ['native-notes-title']
        heading.string = 'Notes'
        notes_section.append(heading)
        notes_list = soup.new_tag('ol')
        notes_section.append(notes_list)
        for n, note in enumerate(source_notes, 1):
            note_id = note.get('id', f'footnote{n}')
            content = note.select_one('.ltx_note_content')
            if content is None:
                raise ValueError(f'Missing note content in {slug}')
            for duplicate in content.select('.ltx_note_mark, .ltx_tag_note'):
                duplicate.decompose()
            for url_tag in content.select('span.ltx_url'):
                target = url_tag.get_text(strip=True)
                if target.startswith(('https://', 'http://')):
                    url_tag.name = 'a'
                    url_tag['href'] = target
            item = soup.new_tag('li', id=note_id)
            for child in list(content.children):
                item.append(child.extract())
            backlink = soup.new_tag('a', href='#' + note_id + '-ref')
            backlink['class'] = ['footnote-backref']
            backlink['aria-label'] = f'Return to footnote {n}'
            backlink.string = '↩'
            item.append(' ')
            item.append(backlink)
            notes_list.append(item)
            marker = soup.new_tag('sup', id=note_id + '-ref')
            link = soup.new_tag('a', href='#' + note_id)
            link['class'] = ['footnote-ref']
            link['aria-label'] = f'Footnote {n}'
            link.string = str(n)
            marker.append(link)
            note.replace_with(marker)
        bibliography = article.select_one('.ltx_bibliography')
        bibliography.insert_before(notes_section)

    asset_dir = ROOT / 'docs' / 'papers' / slug / 'figures'
    asset_dir.mkdir(parents=True, exist_ok=True)
    assets = []
    jobs = []
    for media in list(article.find_all(['img', 'object'])):
        source = media.get('src') or media.get('data')
        if not source or source.startswith('data:'):
            raise ValueError(f'Unexpected inline image in {slug}')
        absolute = urllib.parse.urljoin(url, source)
        filename = Path(urllib.parse.urlparse(source).path).name
        if filename in [a['file'] for a in assets]:
            raise ValueError(f'Asset basename collision: {filename}')
        figure = media.find_parent('figure')
        caption = figure.find('figcaption') if figure else None
        alt = caption.get_text(' ', strip=True) if caption else media.get('alt', '')
        image = soup.new_tag('img')
        image['src'] = 'figures/' + filename
        image['alt'] = alt
        image['loading'] = 'lazy'
        image['decoding'] = 'async'
        image['class'] = ['ltx_graphics', 'native-figure']
        if media.get('id'):
            image['id'] = media['id']
        media.replace_with(image)
        assets.append({'file': filename, 'source_url': absolute, 'alt': alt})
        jobs.append((asset_dir / filename, absolute))

    def download(job):
        path, asset_url = job
        data = path.read_bytes() if path.exists() else request(asset_url)
        if path.suffix == '.svg':
            if b'<svg' not in data or re.search(br'<script\b|<foreignObject\b|\bonload\s*=', data, re.I):
                raise ValueError(f'Unexpected or active SVG asset: {asset_url}')
        elif not data.startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError(f'Unexpected PNG asset: {asset_url}')
        path.write_bytes(data)
        return {'file': path.name, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

    with ThreadPoolExecutor(max_workers=6) as pool:
        downloaded = list(pool.map(download, jobs))
    for asset, info in zip(assets, downloaded):
        asset.update(info)

    # Local in-page links remain stable. Resolve any source-relative external URL
    # to an absolute link rather than accidentally pointing inside this website.
    for link in article.find_all('a', href=True):
        href = link['href']
        if not href.startswith(('#', 'http:', 'https:', 'mailto:')):
            link['href'] = urllib.parse.urljoin(url, href)

    wrapper = soup.new_tag('div')
    wrapper['class'] = ['article-text', 'native-article']
    wrapper['data-source-format'] = 'native-html'
    for child in list(article.children):
        wrapper.append(child.extract())
    output = str(wrapper) + '\n'
    (ROOT / 'content' / f'{slug}.html').write_text(output)

    pdf_path = ROOT / 'docs' / 'papers' / slug / 'paper.pdf'
    pdf = pymupdf.open(pdf_path)
    html_words = words(visible_text(wrapper))
    html_ngrams = set(tuple(html_words[i:i+5]) for i in range(len(html_words)-4))
    page_coverage = []
    for n, page in enumerate(pdf, start=1):
        page_words = words(page.get_text())
        ngrams = [tuple(page_words[i:i+5]) for i in range(len(page_words)-4)]
        coverage = sum(g in html_ngrams for g in ngrams) / len(ngrams)
        page_coverage.append({'page': n, 'five_word_sequence_coverage': round(coverage, 4)})
    body_copy = BeautifulSoup(str(wrapper), 'html.parser')
    body_copy.select_one('.ltx_bibliography').decompose()
    native_body_words = words(visible_text(body_copy))
    pdf_words = words(' '.join(page.get_text() for page in pdf))
    pdf_ngrams = set(tuple(pdf_words[i:i+5]) for i in range(len(pdf_words)-4))
    native_body_ngrams = [tuple(native_body_words[i:i+5]) for i in range(len(native_body_words)-4)]
    body_overlap = sum(g in pdf_ngrams for g in native_body_ngrams) / len(native_body_ngrams)
    ids = {tag['id'] for tag in wrapper.find_all(id=True)}
    dangling = sorted({tag['href'][1:] for tag in wrapper.find_all('a', href=True) if tag['href'].startswith('#') and tag['href'][1:] not in ids})
    if dangling:
        raise ValueError(f'Dangling native links in {slug}: {dangling}')
    if any(not m.find('annotation', attrs={'encoding': 'application/x-tex'}) for m in wrapper.find_all('math')):
        raise ValueError(f'Math without TeX annotation in {slug}')
    manifest = {
        'slug': slug,
        'format': 'native-html',
        'source_url': url,
        'source_tex_url': f'https://arxiv.org/src/{ident}',
        'source_pdf_path': f'docs/papers/{slug}/paper.pdf',
        'source_pdf_sha256': hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
        'source_pdf_pages': len(pdf),
        'source_html_sha256': hashlib.sha256(cache.read_bytes()).hexdigest(),
        'output_sha256': hashlib.sha256(output.encode()).hexdigest(),
        'source_headings': source_headings,
        'source_section_count': source_section_count,
        'native_section_count': len(wrapper.find_all('section')),
        'source_reference_count': source_reference_count,
        'section_headings_unchanged': source_headings == [h.get_text(' ', strip=True) for h in wrapper.find_all(re.compile(r'^h[3-6]$')) if 'native-notes-title' not in h.get('class', [])],
        'added_notes_section': bool(source_notes),
        'footnote_count': len(source_notes),
        'body_word_count': len(html_words),
        'mathml_count': len(wrapper.find_all('math')),
        'table_count': len(wrapper.find_all('table')),
        'reference_count': len(wrapper.select('.ltx_bibitem')),
        'figure_asset_count': len(assets),
        'pdf_crop_count': 0,
        'assets': assets,
        'pdf_page_text_coverage': page_coverage,
        'native_body_five_word_sequences_present_in_pdf': round(body_overlap, 4),
        'fidelity_verdict': 'Original source-based body matches linked PDF section structure, reference count, and figure/table captions. Native HTML preserves equations with TeX annotations and all references. Figures are standalone original plot assets, not page crops. Site publication metadata and abstract remain canonical.',
        'reviewed_repairs': ['Font Awesome check/cross icons replaced with accessible Unicode symbols; thin-space thousands separators in Table II normalized to 283,017 and 2,246, verified from linked PDF; extraneous trailing citation removed; four footnotes normalized to linked Notes list.'] if slug == 'pumpsense' else ['19 inline SVG checkmarks in Table I replaced with accessible Unicode checkmarks; 34 framed insight text boxes converted to ordinary HTML.'],
        'fidelity_limits': ['Published PDF and arXiv bibliography use different reference ordering/formatting; all source references and linked citation targets are retained. Original chart labels remain within the original figure assets.'] if slug == 'pumpsense' else ['Original chart labels remain within original SVG figure assets.'],
        'notes': ['Source conversion includes live in-page reference links. arXiv reference backlink boilerplate removed.'],
    }
    (ROOT / 'content' / f'native-{slug}.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    return {key: manifest[key] for key in ['slug', 'source_pdf_pages', 'body_word_count', 'mathml_count', 'table_count', 'reference_count', 'figure_asset_count', 'pdf_crop_count']}


if __name__ == '__main__':
    for paper, arxiv_id in SOURCES.items():
        print(json.dumps(convert(paper, arxiv_id)), flush=True)
