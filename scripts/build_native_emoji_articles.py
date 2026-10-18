"""Build two native reading articles from their original arXiv HTML and TeX.

Inputs are cached outside the repository. Figures are author-supplied source
assets; PDF figure files become SVG, rather than crops from a paper page.
"""
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from PIL import Image
import argparse, hashlib, json, re, unicodedata
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
EMOJI = {
    'victory-hand': '✌️', 'rocket': '🚀', 'gem': '💎', 'gem-stone': '💎',
    'skull': '💀', 'fire': '🔥', 'pile-of-poo': '💩', 'poop': '💩',
    'joy': '😂', 'face-with-tears-of-joy': '😂', 'rofl': '🤣', 'shrug': '🤷',
    'thinking': '🤔', 'thinking-face': '🤔', 'heart': '❤️', 'heart-eyes': '😍',
    'moneybag': '💰', 'money-bag': '💰', 'money-mouth-face': '🤑', 'eyes': '👀',
    'smiling-face-with-sunglasses': '😎', 'chart-with-upwards-trend': '📈',
    'chart-increasing': '📈', 'chart-decreasing': '📉', 'thumbsup': '👍',
    'thumbs-up': '👍', 'bear': '🐻', 'clown-face': '🤡', 'gorilla': '🦍',
    'muscle': '💪', 'raised-hands': '🙌', 'grin': '😁', 'laughing': '😆',
    'boom': '💥', 'drop-of-blood': '🩸', 'mag': '🔍', 'input-symbols': '🔣',
    'arrow-right': '➡️', 'right-arrow': '➡️', 'input-numbers': '🔢',
    'check-mark-button': '✅', 'notes': '🎶', 'sparkles': '✨', 'star': '⭐',
    'down-arrow': '⬇️', 'up-arrow': '⬆️',
}
PAPERS = {
    'finmoji': ('2605.09469v1', 'emojiPaper.tex'),
    'cross-cultural-emojis': ('2605.09414v1', 'main.tex'),
}


def convert(slug, cache):
    ident, texname = PAPERS[slug]
    source = cache / slug
    raw_html = (cache / (slug + '.html')).read_text()
    tex = (source / texname).read_text()
    tex = re.sub(r'(?<!\\)%[^\n]*', '', tex)
    body_tex = tex[tex.index('\\begin{document}'):]
    emoji_names = re.findall(r'\\emoji\{([^}]+)\}', body_tex)
    soup = BeautifulSoup(raw_html, 'html.parser')
    article = soup.article
    # Keep the complete scientific body, including appendices and references.
    # Title, authors and abstract are already supplied by the landing page.
    for node in list(article.find_all(recursive=False)):
        if node.name != 'section':
            node.decompose()
    article.name = 'div'
    article.attrs = {'class': ['article-text', 'native-article']}
    emoji_images = [im for im in article.find_all('img')
                    if not im.get('src') or re.search(r'/x\d+\.png$', im['src'])]
    assert len(emoji_images) == len(emoji_names), (slug, len(emoji_images), len(emoji_names))
    image_emoji = {}
    for im, name in zip(emoji_images, emoji_names):
        char = EMOJI[name]
        if im.get('src'):
            key = im['src']
            assert image_emoji.get(key, char) == char, (key, name, image_emoji.get(key))
            image_emoji[key] = char
        span = soup.new_tag('span', attrs={'class': 'emoji', 'role': 'img',
                                         'aria-label': name.replace('-', ' ')})
        span.string = char
        im.replace_with(span)

    # Expand hover-only LaTeXML notes into ordinary linked endnotes.
    notes = []
    for note in list(article.select('.ltx_note')):
        note_id = note.get('id', 'note-' + str(len(notes) + 1))
        content = note.select_one('.ltx_note_content')
        if content is None:
            continue
        for mark in content.select('.ltx_note_mark, .ltx_note_type, .ltx_tag_note'):
            mark.decompose()
        notes.append((note_id, content.decode_contents()))
        sup = soup.new_tag('sup', id='ref-' + note_id)
        link = soup.new_tag('a', href='#' + note_id)
        link.string = str(len(notes))
        sup.append(link)
        note.replace_with(sup)
    if notes:
        section = soup.new_tag('section', attrs={'class': 'article-notes', 'id': 'article-notes'})
        title = soup.new_tag('h2'); title.string = 'Notes'; section.append(title)
        ol = soup.new_tag('ol')
        for note_id, contents in notes:
            li = soup.new_tag('li', id=note_id)
            parsed = BeautifulSoup(contents, 'html.parser')
            for child in list(parsed.contents):
                li.append(child.extract())
            backlink = soup.new_tag('a', href='#ref-' + note_id, attrs={'aria-label': 'Back to note reference'})
            backlink.string = ' ↩'; li.append(backlink); ol.append(li)
        section.append(ol)
        bibliography = article.select_one('.ltx_bibliography')
        if bibliography:
            bibliography.insert_before(section)
        else:
            article.append(section)

    figures = ROOT / 'docs' / 'papers' / slug / 'figures'
    figures.mkdir(parents=True, exist_ok=True)
    assets = []
    for node in list(article.find_all(['img', 'object'])):
        remote_path = node.get('src') or node.get('data')
        assert remote_path
        filename = Path(remote_path).name
        candidates = [source / 'figures' / filename, source / filename]
        # arXiv rasterizes some supplied PDF plots; use their vector originals.
        candidates += [source / 'figures' / (Path(filename).stem + '.pdf')]
        original = next((p for p in candidates if p.is_file()), None)
        if original is None and filename.endswith('.svg'):
            original = source / 'figures' / (Path(filename).stem + '.pdf')
        assert original and original.is_file(), (slug, filename)
        if original.suffix == '.pdf':
            dest = figures / (original.stem + '.svg')
            if not dest.exists() or original.stat().st_mtime > dest.stat().st_mtime:
                with pymupdf.open(original) as doc:
                    assert len(doc) == 1
                    dest.write_text(doc[0].get_svg_image(text_as_path=True))
        else:
            dest = figures / (original.stem + '.webp')
            if not dest.exists() or original.stat().st_mtime > dest.stat().st_mtime:
                with Image.open(original) as image:
                    image.save(dest, 'WEBP', lossless=True, method=6)
        caption = node.find_parent('figure')
        caption = caption.find('figcaption') if caption else None
        alt = caption.get_text(' ', strip=True) if caption else filename
        # Caption remains next to the figure; avoid repeating it in alt in full.
        alt = re.sub(r'\s+', ' ', alt)[:220]
        attrs = {k: v for k, v in node.attrs.items()
                 if k not in {'data', 'type', 'style', 'src', 'alt'}}
        attrs.update({'src': 'figures/' + dest.name, 'alt': alt,
                      'loading': 'lazy', 'decoding': 'async'})
        replacement = soup.new_tag('img', attrs=attrs)
        node.replace_with(replacement)
        assets.append({'path': str(dest.relative_to(ROOT)),
                       'original': str(original.relative_to(source)),
                       'sha256': hashlib.sha256(dest.read_bytes()).hexdigest()})

    for node in article.select('script, .ltx_bib_cited'):
        node.decompose()
    # A rotated TeX table is represented as spans by LaTeXML. Restore actual
    # table/row/cell elements and the rowspan encoded in LaTeXML class names.
    # Nested tabular environments inside cells only insert line breaks.
    for nested in list(article.select('.ltx_tabular .ltx_tabular')):
        nested.name = 'span'; nested['class'] = ['table-cell-lines']
        rows = nested.find_all(class_='ltx_tr', recursive=False)
        for row in rows:
            row.name = 'span'; row['class'] = ['table-cell-line']
            for cell in row.find_all(class_='ltx_td', recursive=False):
                cell.name = 'span'; cell['class'] = ['table-cell-text']
            if row is not rows[-1]:
                row.append(soup.new_tag('br'))
    for table in article.select('.ltx_tabular'):
        table.name = 'table'
        for row in table.select('.ltx_tr'):
            row.name = 'tr'
        for cell in table.select('.ltx_td'):
            cell.name = 'td'
            for cls in cell.get('class', []):
                for dimension in ['rowspan', 'colspan']:
                    match = re.fullmatch('ltx_' + dimension + r'_(\d+)', cls)
                    if match:
                        cell[dimension] = match.group(1)
        for parent in table.parents:
            if parent.name == 'figure':
                break
            if parent.name in ['p', 'span']:
                parent.name = 'div'
        first = table.find('tr')
        if first:
            for cell in first.find_all('td', recursive=False):
                cell.name = 'th'; cell['scope'] = 'col'
    # Preserve MathML and its original TeX annotation. Drop screen-only styling.
    for node in article.find_all(True):
        if node.name in ['h2', 'h3', 'h4', 'h5', 'h6']:
            node.name = 'h' + str(min(6, int(node.name[1]) + 1))
        if node.get('style'):
            del node['style']
    math = article.find_all('math')
    assert all(m.select_one('annotation[encoding="application/x-tex"]') for m in math)
    ids = [n['id'] for n in article.select('[id]')]
    assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
    unresolved = [a['href'] for a in article.select('a[href^="#"]')
                  if a['href'][1:] not in ids]
    assert not unresolved, unresolved
    assert not article.find('object')
    assert not article.find('foreignobject')
    assert not article.select('.ltx_missing')
    output = ROOT / 'content' / (slug + '.html')
    output.write_text(str(article) + '\n')
    linked_pdf = ROOT / 'docs' / 'papers' / slug / 'paper.pdf'
    with pymupdf.open(linked_pdf) as pdf:
        pdf_pages = len(pdf)
    manifest = {
        'slug': slug, 'mode': 'native-html',
        'html_source': 'https://arxiv.org/html/' + ident,
        'tex_source': 'https://arxiv.org/src/' + ident,
        'source_tex_file': texname,
        'source_pdf': str(linked_pdf.relative_to(ROOT)),
        'source_pdf_sha256': hashlib.sha256(linked_pdf.read_bytes()).hexdigest(),
        'source_pdf_pages': pdf_pages,
        'mathml_count': len(math),
        'equation_count': len(article.select('.ltx_equation')),
        'table_count': len(article.select('figure.ltx_table')),
        'bibliography_count': len(article.select('.ltx_bibitem')),
        'emoji_count': len(emoji_names),
        'assets': assets,
        'fidelity': 'Scientific body, appendices, references, equations and tables preserved from original arXiv HTML, with emoji positions verified against the TeX source and original figure assets. Linked PDF has the same paper body; citation typography and page layout differ.',
        'limitations': [],
    }
    (ROOT / 'content' / ('native-' + slug + '.json')).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(slug, 'math',len(math),'tables',manifest['table_count'], 'references',manifest['bibliography_count'], 'emoji',len(emoji_names), 'assets',len(assets))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cache', type=Path)
    args = parser.parse_args()
    for slug in PAPERS:
        convert(slug, args.cache)
