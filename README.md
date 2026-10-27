# Ahmed Mahrous — academic homepage

Static academic website published using GitHub Pages at https://amahrous.com/.

## Update

Edit `publications.json` for metadata and TL;DR summaries, `abstracts.json` for complete author-written abstracts, and `build.py` for the profile and layout. Each paper's PDF lives at `docs/papers/<slug>/paper.pdf`, beside its HTML page and `citation.bib`. `pdf_source` records the original public source. Historical `/pdfs/<slug>.pdf` links remain available.

`content/<slug>.html` contains the complete article body. Where original LaTeX-derived HTML is available, equations use MathML, tables use HTML, and figures use the original artwork. A `content/native-<slug>.json` manifest records the source and conversion checks. The remaining articles use PDF-derived text with exact extracts for content that cannot be faithfully reconstructed. Published metadata and citations are maintained separately from the article body.

Rebuild pages:

```sh
python3 build.py
```

To regenerate PDF-derived full text after replacing a manuscript, install `requirements.txt`, run `python3 scripts/extract_fulltext.py` for the affected paper, check the output against the PDF, and rebuild. Do not overwrite native HTML fragments with PDF extraction. Use `python3 scripts/native_stable_pump.py` for Stablecoins and PumpSense. For FinMoji and the cross-cultural article, prepare a cache directory containing `<slug>.html` downloaded from each manifest's `html_source` and an extracted `<slug>/` folder downloaded from `tex_source`, then run `python3 scripts/build_native_emoji_articles.py <cache-directory>`. Verify abstracts separately after a manuscript change.

Run `python3 scripts/check_site.py` before publishing to verify article content, equations, citations, figures, and local links.

Reflexivity Threshold's PDF and native HTML are synchronized with arXiv `2610.29577v1`. To repeat that import, cache the versioned HTML, PDF and TeX archive as `reflexivity.html`, `reflexivity.pdf` and `reflexivity.tar`, then run `python3 scripts/import_reflexivity_arxiv.py <cache-directory>` and rebuild. The source version and checksums are recorded in `content/native-reflexivity-threshold.json`.

Text and math crops in Reflexivity Threshold and Financial Microblog Emojis have been replaced with native HTML and MathML. `scripts/native_paper_passages.py` records the PDF-checked transcriptions and can apply them to the original extracted fragments. The source PDFs and scientific wording are unchanged. Figures blend into the active page theme through CSS; printing retains the original graphic colors.

Commit the updated source and `docs/` files. GitHub Pages deploys branch **main**, folder **/docs**.
