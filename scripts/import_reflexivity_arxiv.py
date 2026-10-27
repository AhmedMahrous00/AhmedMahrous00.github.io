"""Import the public arXiv v1 PDF and native HTML from a local cache.

Usage: python scripts/import_reflexivity_arxiv.py CACHE_DIRECTORY
The cache contains reflexivity.html, reflexivity.pdf and reflexivity.tar,
downloaded from the versioned URLs recorded in the output manifest.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import tarfile

from lxml import html
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'reflexivity-threshold'
VERSION = '2610.29577v1'


def import_article(cache):
    source = html.fromstring((cache / 'reflexivity.html').read_text())
    article = source.xpath('//article')[0]
    for node in list(article):
        if node.tag != 'section':
            article.remove(node)
    article.tag = 'div'
    article.attrib.clear()
    article.set('class', 'article-text native-article')
    figures = ROOT / 'docs' / 'papers' / SLUG / 'figures'
    figures.mkdir(exist_ok=True)
    assets = []
    with tarfile.open(cache / 'reflexivity.tar') as archive:
        for node in article.xpath('.//object'):
            filename = Path(node.get('data')).stem
            original = archive.extractfile(filename + '.pdf').read()
            with pymupdf.open(stream=original, filetype='pdf') as figure:
                assert len(figure) == 1
                svg = figure[0].get_svg_image(text_as_path=True)
            target = figures / (filename + '.svg')
            target.write_text(svg)
            replacement = html.Element('img', src='figures/' + target.name,
                                       alt=filename.replace('_', ' '),
                                       loading='lazy', decoding='async')
            replacement.set('class', 'ltx_graphics')
            if node.get('id'):
                replacement.set('id', node.get('id'))
            node.getparent().replace(node, replacement)
            assets.append({'path': str(target.relative_to(ROOT)),
                           'source': filename + '.pdf',
                           'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    for node in list(article.xpath('.//script | .//iframe')):
        node.getparent().remove(node)
    # The surrounding page supplies its own heading hierarchy and styling.
    for node in article.iter():
        if isinstance(node.tag, str) and re.fullmatch(r'h[2-6]', node.tag):
            node.tag = 'h' + str(min(6, int(node.tag[1]) + 1))
        node.attrib.pop('style', None)
        # Respect the site's punctuation convention without altering math.
        if node.tag not in ('annotation', 'mo'):
            if node.text:
                node.text = node.text.replace('\u2014', ' - ')
            if node.tail:
                node.tail = node.tail.replace('\u2014', ' - ')
    assert len(article.xpath('.//math')) > 400
    assert all(m.xpath('.//annotation[@encoding="application/x-tex"]')
               for m in article.xpath('.//math'))
    ids = article.xpath('.//*[@id]/@id')
    assert len(ids) == len(set(ids))
    for href in article.xpath('.//a/@href'):
        if href.startswith('#'):
            assert href[1:] in ids, href
    fragment = html.tostring(article, encoding='unicode', method='html')
    (ROOT / 'content' / (SLUG + '.html')).write_text(
        '\n'.join(line.rstrip() for line in fragment.splitlines()) + '\n')
    pdf = (cache / 'reflexivity.pdf').read_bytes()
    with pymupdf.open(stream=pdf, filetype='pdf') as document:
        assert len(document) == 20
        assert 'horizons up to order' in document[0].get_text()
    for target in (ROOT / 'docs/papers' / SLUG / 'paper.pdf',
                   ROOT / 'docs/pdfs' / (SLUG + '.pdf')):
        target.write_bytes(pdf)
    manifest = {
        'html_source': 'https://arxiv.org/html/' + VERSION,
        'pdf_source': 'https://arxiv.org/pdf/' + VERSION,
        'tex_source': 'https://arxiv.org/src/' + VERSION,
        'pdf_sha256': hashlib.sha256(pdf).hexdigest(),
        'math_count': len(article.xpath('.//math')),
        'section_ids': [s.get('id') for s in article.findall('section')],
        'assets': assets,
    }
    (ROOT / 'content' / ('native-' + SLUG + '.json')).write_text(
        json.dumps(manifest, indent=2) + '\n')
    print('Imported', VERSION, 'with', manifest['math_count'], 'MathML expressions')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cache', type=Path)
    import_article(parser.parse_args().cache)
