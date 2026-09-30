# Site build scripts

Not published: GitHub Pages skips folders that start with an underscore.

Run from the repo root after editing:

- `python3 _build/build_products.py products.html` rebuilds the English products page from the product data in the script.
- `python3 _build/build_products_fr.py` rebuilds `fr/products.html` (French copy of the same data).
- `python3 _build/build_fr_index.py` rebuilds `fr/index.html` from `index.html`. It stops with an error if an English string it translates has changed, so update its dictionary when the English copy changes.
