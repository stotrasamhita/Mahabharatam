# parvas/

The 18 parvas (books) of the Mahābhārata, one LaTeX file per parva, in traditional order.
Each file is `\input` by the top-level book files at the repo root
(`Mahabharatam-Kumbhaghonam.tex` etc.) and contains that parva's chapters (`\chapter`) and
verses, typeset with the macros from [`shloka.sty`](../shloka.sty).

These files are generated from `extracted_data/*.json` by `write_TeX.ipynb` — see the root
[README](../README.md#data-pipeline) for the pipeline. They are the canonical, checked-in
typeset text; edits meant to persist should generally go back through the pipeline (or the
`fix_incorrect_makaara_endings.py` cleanup script) rather than being made by hand only.

| # | File | Parva | Devanāgarī |
|---|---|---|---|
| 1 | `01-ādiparva.tex` | Ādi Parva — Book of the Beginning | आदिपर्व |
| 2 | `02-sabhāparva.tex` | Sabhā Parva — Book of the Assembly Hall | सभापर्व |
| 3 | `03-araṇyaparva.tex` | Āraṇyaka (Vana) Parva — Book of the Forest | अरण्यपर्व |
| 4 | `04-virāṭaparva.tex` | Virāṭa Parva — Book of Virāṭa | विराटपर्व |
| 5 | `05-udyogaparva.tex` | Udyoga Parva — Book of the Effort | उद्योगपर्व |
| 6 | `06-bhīṣmaparva.tex` | Bhīṣma Parva — Book of Bhīṣma | भीष्मपर्व |
| 7 | `07-droṇaparva.tex` | Droṇa Parva — Book of Droṇa | द्रोणपर्व |
| 8 | `08-karṇaparva.tex` | Karṇa Parva — Book of Karṇa | कर्णपर्व |
| 9 | `09-śalyaparva.tex` | Śalya Parva — Book of Śalya | शल्यपर्व |
| 10 | `10-sauptikaparva.tex` | Sauptika Parva — Book of the Sleeping Warriors | सौप्तिकपर्व |
| 11 | `11-strīparva.tex` | Strī Parva — Book of the Women | स्त्रीपर्व |
| 12 | `12-śāntiparva.tex` | Śānti Parva — Book of Peace | शान्तिपर्व |
| 13 | `13-anuśāsanaparva.tex` | Anuśāsana Parva — Book of Instructions | अनुशासनपर्व |
| 14 | `14-āśvamedhikaparva.tex` | Āśvamedhika Parva — Book of the Horse Sacrifice | आश्वमेधिकपर्व |
| 15 | `15-mausalaparva.tex` | Mausala Parva — Book of the Clubs | मौसलपर्व |
| 16 | `16-āśramavāsikaparva.tex` | Āśramavāsika Parva — Book of the Hermitage | आश्रमवासिकपर्व |
| 17 | `17-mahāprasthānikaparva.tex` | Mahāprasthānika Parva — Book of the Great Journey | महाप्रस्थानिकपर्व |
| 18 | `18-svargārohaṇaparva.tex` | Svargārohaṇa Parva — Book of the Ascent to Heaven | स्वर्गारोहणपर्व |

## Other files

- `04-virāṭaparva-orig.tex` — an earlier, hand-adjusted version of Virāṭa Parva, kept for
  reference/comparison against the generated `04-virāṭaparva.tex`.
- `04-virāṭaparva-verse-patterns.txt` — a per-verse metrical (chandas) analysis of Virāṭa
  Parva: laghu/guru syllable pattern and identified meter for each verse, used as a
  cross-check against the typeset text (see also `../res/`).

`PativrataMahatmyaParva.tex` at the repo root typesets a single episode from within Āraṇyaka
Parva rather than an entire numbered parva, so it doesn't have its own file in this directory.
