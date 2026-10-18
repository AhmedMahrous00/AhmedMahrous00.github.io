# Ahmed Mahrous — academic homepage

Static academic website published using GitHub Pages at https://amahrous.com/.

## Update

Edit `publications.json` for metadata and TL;DR summaries, `abstracts.json` for complete author-written abstracts, and `build.py` for the profile and layout. Each paper's PDF lives at `docs/papers/<slug>/paper.pdf`, beside its HTML page and `citation.bib`. `pdf_source` records the original public source. Historical `/pdfs/<slug>.pdf` links remain available.

`content/<slug>.html` contains the full-text HTML reading edition, transcribed from the corresponding PDF. Equations and figures retain source images; source-page links point back to the PDF. Published DOIs identify the cited version; author-manuscript content is labeled separately.

Rebuild pages:

```sh
python3 build.py
```

To regenerate full text after replacing a manuscript, install `requirements.txt`, run `python3 scripts/extract_fulltext.py`, check the output against the PDF, and rebuild. Verify abstracts separately after a manuscript change.

Commit the updated source and `docs/` files. GitHub Pages deploys branch **main**, folder **/docs**.
