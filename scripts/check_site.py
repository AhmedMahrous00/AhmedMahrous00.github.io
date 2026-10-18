"""Check publication pages, source coverage, local links and embedded images."""
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
    assert len(soup.select('#full-text .source-page')) == len(pdf), (slug, 'page coverage')
    assert len(soup.select('#full-text h3')) > 2, (slug, 'section headings')
    assert 'references' in soup.select_one('#full-text').get_text().lower(), (slug, 'references')
    assert soup.select_one('meta[name=citation_pdf_url]')['content'] == 'https://amahrous.com/papers/'+slug+'/paper.pdf', slug
    assert soup.select_one('#citation pre').get_text() == (folder/'citation.bib').read_text(), slug
    schema = json.loads(soup.select_one('script[type="application/ld+json"]').string)
    assert schema['abstract'] == abstracts[slug], slug
    for image in soup.select('#full-text img'):
        assert image.get('alt'), (slug, 'image alt')
        src = image['src']
        if src.startswith('data:image/'):
            raw = base64.b64decode(src.split(',', 1)[1], validate=True)
            Image.open(io.BytesIO(raw)).verify()
            images += 1
    for link in soup.find_all('a', href=True):
        url = urlparse(link['href'])
        if url.scheme or not url.path:
            continue
        target = DOCS/url.path.lstrip('/') if url.path.startswith('/') else folder/url.path
        target = target.resolve()
        assert target.is_relative_to(DOCS.resolve()), (slug, 'escaping link', link['href'])
        assert target.exists(), (slug, 'missing link', link['href'])
    print(slug, len(pdf), 'pages;', len(soup.select('#full-text').pop().get_text().split()), 'HTML words')

print(f'PASS: {len(papers)} full-text pages, abstracts, citations, PDF paths and {images} embedded images.')
