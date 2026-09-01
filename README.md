# महाभारतम् · Mahābhāratam

A LaTeX/Sanskrit-text project for the **Mahābhārata**, the great Sanskrit epic traditionally
attributed to Vyāsa. It contains the full text in Devanāgarī, organized by *parva* (book),
compiled book-length PDFs, and the pipeline used to go from a digitized source text to
typeset pages.

## What's here

| Path | What it is |
|---|---|
| `Mahabharatam-Kumbhaghonam.tex` / `.pdf` | The complete Mahābhārata, all 18 parvas, typeset as one book (A3, two-column). |
| `Mahabharatam-Kumbhaghonam-kindle.tex` / `.pdf` | The same complete text, reflowed to a Kindle-friendly page size (one column). |
| `VirataParva.tex` / `.pdf` | Virāṭa Parva alone, as a standalone booklet. |
| `PativrataMahatmyaParva.tex` / `.pdf` | The Pativratā-māhātmya episode (from within Āraṇyaka/Vana Parva) as a standalone booklet. |
| `parvas/` | The 18 parvas as individual `.tex` source files — see [`parvas/README.md`](parvas/README.md). |
| `SARIT-corpus/` | The source TEI-XML text the `.tex` files are generated from — see [`SARIT-corpus/README.md`](SARIT-corpus/README.md). |
| `extracted_data/` | Per-parva JSON, an intermediate step between the source XML and the `.tex` files — see [`extracted_data/README.md`](extracted_data/README.md). |
| `extract_xml.py` | Parses the SARIT TEI-XML and writes the per-parva JSON in `extracted_data/`. |
| `parse_TEI_xml.ipynb` | Exploratory notebook used while working out how to parse the TEI-XML structure. |
| `write_TeX.ipynb` | Reads the per-parva JSON and writes the typeset `.tex` files in `parvas/`. |
| `fix_incorrect_makaara_endings.py` | A cleanup script that corrects sandhi-related anusvāra/makāra mistakes (म् vs. ं) at line ends in generated `.tex` files. |
| `preamble.tex`, `frontmatter.tex`, `shloka.sty` | Shared LaTeX preamble, title/TOC front matter, and the custom style file with macros for typesetting Sanskrit verse (śloka) layouts. |
| `res/` | Small ad hoc analysis files used while checking Virāṭa Parva against the P. P. S. Sastri edition — laghu-guru (metrical) counts and a plain-text reference copy. Not part of the build. |

## The text

The typeset text is based on the **Kumbhakoṇam (Kumbhaghoṇam) edition** — *Śrīmān Mahābhāratam*,
edited by T. R. Krishnacharya and T. R. Vyasacharya (Nirnaya Sagar Press, Bombay, 1906–1910),
a critical edition mainly following the Southern recension. The Devanāgarī source text
(`SARIT-corpus/mahabharata-devanagari.xml`) is a digitization of that edition prepared by
Prof. Shrinivasa Varakhedi and collaborators, distributed via the
[SARIT](http://sarit.indology.info) project — see
[`SARIT-corpus/README.md`](SARIT-corpus/README.md) for its own licensing, which differs from
this repository's.

## Building the PDFs

The documents are written for **XeLaTeX** (see the `!TeX program = XeLaTeX` line at the top of
each `.tex` file) because they set Devanāgarī via `fontspec`. You'll need:

- A TeX distribution with XeLaTeX (e.g. TeX Live).
- The Devanāgarī fonts the documents call for by name: **Sanskrit 2003**, **Adishila**,
  and **Siddhanta** (different top-level documents use different ones — check each file's
  `\setmainfont` line). These are not bundled in this repo and need to be installed/available
  to `fontspec` separately.
- Standard LaTeX packages used throughout: `fontspec`, `etoolbox`, `geometry`, `fancyhdr`,
  `hyperref`, `wallpaper`, `fontawesome`.

To build the full book, for example:

```sh
xelatex Mahabharatam-Kumbhaghonam.tex
xelatex Mahabharatam-Kumbhaghonam.tex   # run twice for the table of contents / bookmarks
```

Each top-level `.tex` file `\input`s the parva files it needs from `parvas/`, along with
`preamble.tex` and `frontmatter.tex`, and relies on the macros defined in `shloka.sty`
(`\twolineshloka`, `\fourlineindentedshloka`, etc.) for verse layout.

## Data pipeline

The parva `.tex` files in `parvas/` are generated, not hand-typed, from the SARIT TEI-XML:

```
SARIT-corpus/mahabharata-devanagari.xml   (TEI-XML source text)
        │  extract_xml.py
        ▼
extracted_data/*.json                      (one JSON file per parva)
        │  write_TeX.ipynb
        ▼
parvas/*.tex                               (typeset LaTeX, one file per parva)
```

`extract_xml.py` walks the TEI `<div>` structure (parva → adhyāya → verse) with
BeautifulSoup and writes each parva's chapters, headings, topic/footnote text, and verses to
JSON. `write_TeX.ipynb` reads that JSON and emits LaTeX using the `shloka.sty` verse macros,
transliterating parva names to Devanāgarī along the way (via the `indic_transliteration`
Python package). `fix_incorrect_makaara_endings.py` is a separate, later pass over generated
`.tex` files to correct a specific recurring sandhi issue. `parse_TEI_xml.ipynb` is earlier,
exploratory work on the TEI structure and isn't part of the current pipeline.

`parvas/04-virāṭaparva-orig.tex` is kept alongside the generated `04-virāṭaparva.tex` as an
earlier, hand-adjusted version of Virāṭa Parva for reference/comparison.

## License

This repository's own code and build files are released under **CC0 1.0 Universal** (see
[`LICENSE`](LICENSE)) — to the extent the contributors hold any rights in them, they're
placed in the public domain. Note that the source text in `SARIT-corpus/` carries its own,
different license from the SARIT project (CC BY-SA); see
[`SARIT-corpus/README.md`](SARIT-corpus/README.md) before reusing it.

## Related projects

This repository is maintained alongside other Sanskrit-text projects under the
[StotraSamhita](https://github.com/stotrasamhita) organization, including
[ValmikiRamayanam](https://github.com/stotrasamhita/ValmikiRamayanam) and
[gita](https://github.com/stotrasamhita/gita). See [stotrasamhita.net](https://stotrasamhita.net)
for more.

---

*The README.md files on this repo were generated and beautified with Claude.*
