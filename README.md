# Ahmed Mahrous — academic homepage

Static academic website published using GitHub Pages.

## Update

Edit `publications.json` for paper metadata or `build.py` for the profile and layout. Run:

```sh
python3 build.py
```

Commit the updated source and `docs/` files. In Settings → Pages, select **Deploy from a branch**, **main**, and **/docs**.

Site: https://amahrous.com/

Each publication can have a `pdf` URL pointing directly to a public PDF. These links open in a new tab from the homepage, CV, and individual paper pages. Keep the publisher or abstract page in `url`; identical PDF links are shown only once. Set `pdf_label` when a version needs identifying (for example, `PDF (preprint)`).

PDF sources: CRI-Lab author copies, arXiv preprints, ACL Anthology, and the KAUST institutional repository. The `pdf` URLs in `publications.json` record each source.
