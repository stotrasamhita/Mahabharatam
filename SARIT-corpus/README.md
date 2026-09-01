# SARIT-corpus/

The source text this project's Mahābhārata is typeset from: a single TEI-XML file,
`mahabharata-devanagari.xml` (~37 MB), containing the full Devanāgarī text of all 18 parvas,
marked up down to the level of individual verses (`<lg>`/`<l>` elements) inside chapters
(`<div>`) inside parvas (`<div>`).

## Provenance

Per the file's own `teiHeader`:

- **Text**: based on the *Kumbhakoṇam edition* — *Śrīmān Mahābhāratam*, edited by
  T. R. Krishnacharya and T. R. Vyasacharya (Nirnaya Sagar Press, Bombay, 1906–1910), a
  17-volume edition mainly based on South Indian ("Southern recension") manuscripts.
- **Digitization**: the machine-readable text was created by Prof. Shrinivasa Varakhedi with
  a team of collaborators (work begun at the Rashtriya Sanskrit Vidyapeetha, Tirupati, and
  continued with contributors in Hyderabad and Bangalore).
- **Distribution**: distributed as a "SARIT edition" by
  [SARIT: Search and Retrieval of Indic Texts](http://sarit.indology.info) (2012–2016).
- **A note in the file itself**: "Droṇaparva 15 is empty" — i.e. there's a known gap at that
  chapter in the source.

## License — different from the rest of this repository

The `teiHeader` states this text is distributed by SARIT under a
**Creative Commons Attribution-ShareAlike 3.0 Unported License**
(`CC BY-SA 3.0`, http://creativecommons.org/licenses/by-sa/3.0/), which requires attribution
and share-alike redistribution. This is **not** the same as the CC0 license covering the rest
of this repository (see the root [`LICENSE`](../LICENSE)) — if you reuse this XML file itself
(as opposed to the derived `.tex`/PDF output built from it), follow SARIT's CC BY-SA terms.

## Using this file

It's large and verbose (raw TEI-XML), not meant to be read directly. `../extract_xml.py`
parses it into the smaller, per-parva JSON files in [`../extracted_data/`](../extracted_data/README.md),
which is the practical starting point for further processing. See the root
[README's data-pipeline section](../README.md#data-pipeline) for the full flow from this file
to the typeset `.tex` sources in [`../parvas/`](../parvas/README.md).
