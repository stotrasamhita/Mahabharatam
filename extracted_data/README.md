# extracted_data/

Generated intermediate data — not hand-edited. One JSON file per parva, produced by
`../extract_xml.py` from the TEI-XML source in
[`../SARIT-corpus/mahabharata-devanagari.xml`](../SARIT-corpus/README.md), and in turn
consumed by `../write_TeX.ipynb` to produce the typeset `.tex` files in
[`../parvas/`](../parvas/README.md).

```
SARIT-corpus/mahabharata-devanagari.xml → (extract_xml.py) → extracted_data/*.json → (write_TeX.ipynb) → parvas/*.tex
```

Files are named and numbered the same way as their `parvas/` counterparts, e.g.
`04-virāṭaparva.json` corresponds to `parvas/04-virāṭaparva.tex`.

## Structure

Each file is a JSON object keyed by the parva's TEI `xml:id`, containing one entry per
chapter (adhyāya), keyed by that chapter's `xml:id`. Each chapter entry holds, where present:

- `head` — the chapter heading text, if the source marked one.
- `topic` — introductory/topic text for the chapter.
- `before_verses` / `after_verses` / `footnotes` — surrounding prose or footnote text outside
  the verses proper.
- `verses` — a list of verses, each with:
  - `verse_no` — the verse's `xml:id` (chapter-verse numbering).
  - `chandas` — the metre, where the source records one.
  - `verse_text` — the verse's lines (split on the daṇḍa `।`), as extracted from the XML.

To regenerate this directory from scratch, run `python3 extract_xml.py` from the repo root
(requires `beautifulsoup4`, `lxml`, and `pandas`).

---

*The README.md files on this repo were generated and beautified with Claude.*
