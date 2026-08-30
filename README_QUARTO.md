# Leandro Zipitría — Quarto website

Final design package for the new website.

## Approved structure

- Home: economist identity first; Industrial Organization + Applied Microeconomics as main fields.
- Research: three selected publications at top, full research record below, regulation book highlighted.
- Teaching: current courses first, cases and current guidance integrated, previous courses archived below.
- Professional: competition, regulation, and market analysis.
- TeXFlow: product landing page, including Beamer.
- More: Writing & Media, Personal, Reading, Contact.

## Static resources

- `files/` is a persistent public resource tree. During migration, **merge** this project's new teaching files into the existing repository `files/`; never replace or delete the existing tree.
- `libro-regulacion/` is the published Bookdown output copied from the independent book project `docs/`. Quarto does not build the book; it publishes this directory unchanged.

## Local preview / render

With Quarto installed:

```bash
quarto preview
```

Final validation before publication:

```bash
quarto render
python scripts/check_internal_links.py --root .
```

`--include-files` should only be used after this overlay has been merged into the real repository, where the complete legacy `files/` tree exists.
