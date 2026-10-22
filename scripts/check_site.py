"""Check publication pages, source coverage, math, images and internal links."""
import base64
import io
import json
from pathlib import Path
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup
from PIL import Image
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
papers = json.loads((ROOT/'publications.json').read_text())
abstracts = json.loads((ROOT/'abstracts.json').read_text())
images = 0

for paper in papers:
    slug = paper['slug']
    folder = DOCS/'papers'/slug
    soup = BeautifulSoup((folder/'index.html').read_text(), 'html.parser')
    pdf = pymupdf.open(folder/'paper.pdf')
    assert 'Item Type' not in pdf[0].get_text(), (slug, 'repository cover')
    assert soup.select_one('#tldr h2').get_text() == 'TL;DR', slug
    assert [p.get_text() for p in soup.select('#abstract p')] == abstracts[slug].split('\n\n'), slug
    native_path = ROOT/'content'/f'native-{slug}.json'
    native = native_path.exists()
    if native:
        assert soup.select_one('#full-text .native-article'), (slug, 'native article missing')
        assert not soup.select('#full-text .source-page, #full-text .math-excerpt'), (slug, 'PDF crop remains')
        for math in soup.select('#full-text math'):
            assert math.select_one('annotation[encoding="application/x-tex"]'), (slug, 'math source missing')
        assert not soup.select('#full-text script, #full-text iframe, #full-text object'), (slug, 'active source content')
    else:
        assert len(soup.select('#full-text .source-page')) == len(pdf), (slug, 'page coverage')
    if soup.select_one('#full-text .native-passages'):
        assert not soup.select('#full-text .math-excerpt'), (slug, 'text/math screenshot remains')
        for math in soup.select('#full-text math'):
            assert math.select_one('annotation[encoding="application/x-tex"]'), (slug, 'math source missing')
        numbers = [n.get_text() for n in soup.select('.equation-number')]
        if slug == 'reflexivity-threshold':
            assert numbers == [f'({i})' for i in range(1,17)], (slug, 'equation numbering')
    assert len(soup.select('#full-text h3')) > 2, (slug, 'section headings')
    assert 'references' in soup.select_one('#full-text').get_text().lower(), (slug, 'references')
    assert soup.select_one('meta[name=citation_pdf_url]')['content'] == 'https://amahrous.com/papers/'+slug+'/paper.pdf', slug
    assert soup.select_one('#citation pre').get_text() == (folder/'citation.bib').read_text(), slug
    schema = json.loads(soup.select_one('script[type="application/ld+json"]').string)
    assert schema['abstract'] == abstracts[slug], slug
    assert not soup.select('.version-note, .page-source, .text-transcription'), (slug, 'conversion notice')
    ids = [node['id'] for node in soup.select('[id]')]
    assert len(ids) == len(set(ids)), (slug, 'duplicate IDs')
    for image in soup.select('#full-text img'):
        assert image.get('alt'), (slug, 'image alt')
        src = image['src']
        if src.startswith('data:image/'):
            raw = base64.b64decode(src.split(',', 1)[1], validate=True)
            Image.open(io.BytesIO(raw)).verify()
            images += 1
        else:
            assert not urlparse(src).scheme, (slug, 'external image', src)
            target = (folder/unquote(src)).resolve()
            assert target.is_relative_to(folder.resolve()) and target.exists(), (slug, 'missing image', src)
            if target.suffix == '.svg':
                svg = BeautifulSoup(target.read_text(), 'xml')
                assert not svg.select('script, foreignObject'), (slug, 'active SVG', src)
            else:
                Image.open(target).verify()
            images += 1
    for link in soup.find_all('a', href=True):
        url = urlparse(link['href'])
        if url.scheme:
            continue
        if not url.path:
            if url.fragment:
                assert unquote(url.fragment) in ids, (slug, 'missing anchor', link['href'])
            continue
        target = DOCS/url.path.lstrip('/') if url.path.startswith('/') else folder/url.path
        target = target.resolve()
        assert target.is_relative_to(DOCS.resolve()), (slug, 'escaping link', link['href'])
        assert target.exists(), (slug, 'missing link', link['href'])
    print(slug, 'native HTML;' if native else f'{len(pdf)} PDF pages;', len(soup.select('#full-text').pop().get_text().split()), 'HTML words')

print(f'PASS: {len(papers)} full-text pages, abstracts, citations, PDF paths and {images} figures.')
