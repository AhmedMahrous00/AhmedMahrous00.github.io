# Ahmed Mahrous — academic homepage

Static academic website published using GitHub Pages.

## Update

Edit `publications.json` for paper metadata or `build.py` for the profile and layout. Run:

```sh
python3 build.py
```

Commit the updated source and `docs/` files. In Settings → Pages, select **Deploy from a branch**, **main**, and **/docs**.

Site: https://amahrous.com/

PDFs are hosted in `docs/pdfs/`. Set each publication's `pdf` to its root-relative path (for example, `/pdfs/finmoji.pdf`). Every paper shows a single **PDF** button on the homepage, CV, and paper page, opening the hosted file in a new tab.

`pdf_source` records the original public source for provenance; `url`, `html`, and `code` metadata are retained but are not displayed as extra publication buttons. To replace a PDF, update the file in `docs/pdfs/`, then rebuild and commit the source and generated pages.
