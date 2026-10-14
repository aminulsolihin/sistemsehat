# SistemSehat writing guide

How to write for SistemSehat, in English and in Bahasa Indonesia. Read it before you add or change a page. The content report (`python3 tools/content_report.py`) checks the parts of this guide that a program can check.

## 1. Who we write for

- **Procurement officials** in district health offices and public hospitals: the PPK, the Pokja Pemilihan, procurement officials. They know the procurement rules well, but not every device.
- **Clinicians** who help write specifications and check what is delivered. They know the device well, but not procurement.
- **Technical and maintenance staff**, and **planners** who prepare budgets.

Most readers of the English pages are Indonesian and read English as a second language. Many read on a phone, between other tasks. So we write to be understood on the first reading, by someone in a hurry.

## 2. Voice

- **Plain and direct.** Say what to do. "Ask for the test report", not "It is recommended that the test report be requested".
- **Talk to the reader.** English: "you". Indonesian: "Anda", always with a capital A.
- **Neutral.** No brands, no praise, no hype. We guide; we do not sell.
- **Literal, not figurative.** No idioms, no metaphors, no wordplay. They do not translate, and second-language readers miss them.

## 3. Sentences and paragraphs

- **One idea per sentence**, and no more than 25 words. If a sentence has a list of four things or more, split it, or use a real list.
- **Paragraphs are short:** no more than three sentences in a rule.
- **Use the active voice.** "The PPK sets the HPS", not "The HPS is set".
- **Write numbers as digits** when they are measurements or counts: 20 tests, 5 years, 40 units.

## 4. How a rule is built

Every rule in a guide has the same five parts. The build and the checks rely on them.

| Part | What it is | Rules |
|---|---|---|
| Number | `1.4`, `A.6` | The same number in both languages. Never reuse a number for a different rule. |
| Heading | What to do | An instruction, no more than about 8 words. Literal: say "Size each lot so that several suppliers can bid", not "Draw lots the market can serve". |
| Explanation | Why, and what it means | One short paragraph, about 60 words or fewer. |
| Example | One concrete case | One or two sentences. Use the devices we know: an infant warmer, a laboratory analyzer, a puskesmas, a district hospital. Mark made-up figures "(Illustrative figures.)". |
| Ask yourself | One question to check your own work | A single question the reader can answer with yes/no, a name, a number or a document. It appears again on the checklist. |

In `src/content_en.py` and `src/content_id.py`, a rule looks like this:

```python
clause("2.2", "Count the cost over the device's whole life",
       ["The purchase price is only part of the cost. ..."],          # explanation
       "What will this device cost each year once it is in use?",     # Ask yourself
       "A puskesmas that runs 20 tests a day ..."),                   # Example
```

## 5. Words we use

Use the same word for the same thing everywhere. When a reader sees two different words, they assume two different things.

| English | Bahasa Indonesia | Avoid |
|---|---|---|
| bidder (a company that submits a bid) | peserta | tenderer |
| supplier (a company that sells and delivers) | penyedia | vendor |
| bidding document | dokumen pemilihan | tender docs |
| cost estimate (HPS) | HPS | owner's estimate |
| amendment | adendum | addendum letter |
| pre-bid meeting | pemberian penjelasan | aanwijzing (only as an aside) |
| lot | paket | package |
| scored on quality as well as price | sistem nilai | rated criteria |
| acceptance test | uji terima | |
| commissioning | uji fungsi | |
| marketing authorisation (*izin edar*) | izin edar | registration (on its own) |
| consumables | bahan habis pakai | |
| test report | laporan uji | certificate (it is not one) |
| rule (in a guide) | prinsip | kaidah, aturan (confused with *peraturan*) |
| device | alat | product (unless you mean the commercial product) |
| Sources (the library page) | Sumber rujukan | Library, Pustaka |

Spelling in English is British ("authorisation", "organisation"), except "analyzer", which is the spelling used by manufacturers and in Indonesian catalogues.

## 6. Abbreviations and terms

- **Every abbreviation must be in the glossary**, in both languages, with the same id. The content report lists any that are missing.
- **You do not need to link terms by hand.** The build links the first use of each glossary term on every page to its definition, with a dotted underline and a tooltip. To make this work, add the patterns that find the term (for example `r"\bHPS\b"`) to the glossary entry.
- **Indonesian words on English pages** go in `<em>`: `<em>izin edar</em>`. The build marks them as Indonesian so screen readers pronounce them correctly.
- **English words on Indonesian pages** that have no common Indonesian equivalent get `<em lang="en">`, as in `<em lang="en">health technology assessment</em>`. Device names used in Indonesian catalogues (infant warmer, analyzer) are written normally.

## 7. Numbers, money and dates

| | English | Bahasa Indonesia |
|---|---|---|
| Money | Rp150 million, US$1,850 | Rp150 juta, US$1.850 |
| Thousands | 25,000 | 25.000 |
| Dates | 11 October 2026 | 11 Oktober 2026 |
| Percentages | 70% | 70% |

Indonesian follows EYD edisi V and KBBI.

## 8. Facts and sources

- Every figure and every requirement comes from a public document, and the page cites it.
- Regulations change. Name the regulation and its year, give the date you checked it, and update "Last reviewed" (`REVIEWED` at the top of each content file) when you check again.
- Examples are illustrative unless a source is cited. Say so.
- Never write about a tender that is still being evaluated, and never rate a brand.

## 9. Links

- Link text says where the link goes: "the WHO template for technical specifications", never "click here".
- Link to the document itself when you can, not to a search page.

## 10. Both languages

- The two versions say the same thing, but each is written for its own readers. Do not translate word for word. Use the terms Indonesian procurement staff use (HPS, dokumen pemilihan, penyedia) on the Indonesian pages.
- Keep the same rules, rule numbers, examples and glossary ids in both. The checks fail if a page's anchors differ between the languages.

## 11. Before you publish

1. `python3 src/build.py`
2. `python3 tools/check.py`: links, anchors, both languages, titles.
3. `python3 tools/content_report.py`: long sentences, words to replace, abbreviations, rules without an example.
4. Read the changed page aloud, in both languages. If you stumble, rewrite.
5. For a new or changed rule, ask someone who does that job (a PPK, a clinician, a technician) to read it.
