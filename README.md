# SistemSehat website

Independent guidance on medical technology in Indonesia, in English and Indonesian. The site has two halves of equal weight:

- **Build**, for people who develop medical technology: guides C (Design), D (Route to market) and E (Open source), and the Open projects list.
- **Buy**, for people who purchase it: guides 1 (Specification), 2 (Pricing), 3 (Process), A (Regulation) and B (Technology), and the device dossiers.

Articles, the checklist, the glossary, sources and search are shared by both.

The site is managed with **Jekyll**, which GitHub runs for you. The words live in plain text files (Markdown and YAML) that you can edit on github.com. Each time you save a change, GitHub rebuilds the site, checks it, and publishes it, usually within two minutes. You do not need to install anything.

Live site: <https://aminulsolihin.github.io/sistemsehat/>, Indonesian at `.../sistemsehat/id/`.

## Where things are

English pages are at the top of the repository, Indonesian pages in `id/` with the same file names.

| To change | Edit |
| --- | --- |
| A rule in a guide (heading, explanation, example, question) | Buy: `specification.md`, `pricing.md`, `process.md`, `regulation.md`, `technology.md`. Build: `design.md`, `to-market.md`, `open-source.md`. The same files in `id/`. The rules are in the `rules:` list at the top. |
| A table or the text under the rules of a guide | The same file: tables are in `tables:` at the top, the text is below the second `---` line. |
| The Open projects list | `_data/en/projects.yml` and `_data/id/projects.yml` |
| An article (the blog) | `_posts/` (English) and `id/_posts/` (Indonesian). See "Write an article" below. |
| The About or Dossiers page | `about.md`, `dossiers.md` (and `id/`) |
| The home page | `index.html` and `id/index.html`. All the words are in the top section. |
| A glossary term | `_data/en/glossary.yml` and `_data/id/glossary.yml` |
| The Sources page | `_data/en/sources.yml` and `_data/id/sources.yml` |
| Dossiers in preparation (table on the home and dossiers pages) | `_data/en/dossiers.yml` and `_data/id/dossiers.yml` |
| Menu, buttons, labels, the "Last reviewed" date, the Build and Buy descriptions, article topics | `_data/en/ui.yml` and `_data/id/ui.yml` |
| Colours, type, behaviour | `assets/style.css`, `assets/site.js` |
| Page design (shared by many pages) | `_layouts/` and `_includes/`. You rarely need these. |

How to write for the site, in both languages, is in `WRITING-GUIDE.md`.

## Edit on github.com

1. Open the file in the repository and click the pencil icon (**Edit this file**).
2. Make the change. Keep the indentation (the spaces at the start of lines) exactly as it is, because it gives the file its structure.
3. Click **Commit changes**, write a short note such as "Fix example in rule 2.2", and commit to `main`.
4. Open the **Actions** tab. A green tick means the site is published. A red cross means the check found a problem and the site was **not** changed. Click the run to read what to fix.
5. Make the same change in the other language.

## How a rule is written

Each guide begins with a section between two `---` lines (the "front matter"). Its rules look like this:

```yaml
rules:
  - number: "2.2"
    heading: Count the cost over the device's whole life
    explanation: >-
      The purchase price is only part of the cost. Add delivery and installation,
      consumables and reagents, maintenance and spare parts, training, and disposal.
    example: >-
      A puskesmas that runs 20 tests a day, 250 days a year, uses reagents for
      25,000 tests in five years.
    ask: What will this device cost each year once it is in use, and who will pay?
```

- `>-` lets a long text continue on the next lines. Indent those lines by two more spaces than the name above them.
- Keep the number in quotes. Use the same number in both languages: links and the language switch depend on it.
- Inside any text you can write a link as `[link text](https://address)`, and italics as `*izin edar*`. Straight quotes `"like this"` become curly quotes on the site.
- A text on one line that begins with a quote mark, `[`, `*` or another symbol, or contains `: `, must be wrapped in single quotes: `'"Brand X or equivalent"'`. Texts written after `>-` never need quotes.
- To add a rule, copy a whole block (from `- number:` to `ask:`), change it, and give it the next number. To add a guide, copy a guide file and change `order`, `number` and the rest.

From these lists the site builds the "rules in this guide" box, the checklist, the search index and the rule counts. Nothing else needs updating.

## Write an article

Articles are short pieces on one question, listed newest first on the Articles page.

1. Copy `drafts/article-template.md`.
2. Save it in `_posts/` with a name in this form: `YEAR-MONTH-DAY-short-name.md`, for example `_posts/2026-11-02-reading-a-test-report.md`. On github.com: **Add file**, **Create new file**, and type `_posts/2026-11-02-reading-a-test-report.md` as the name.
3. Fill in the top section:

   ```yaml
   ---
   title: How to read a test report
   description: One or two sentences. Shown under the title, in the list of articles and in link previews.
   author: Aminul Solihin
   topic: research
   ---
   ```

   `topic` is one of `innovation`, `open-source`, `research`, `procurement` or `regulation`. Readers can filter the list of articles by topic, and the count beside each topic shows whether the two halves are getting equal attention. The topics and their names are in `_data/en/ui.yml` and `_data/id/ui.yml`.

   Keep the title to 56 characters or fewer and the description to 160 or fewer; the check fails otherwise.
4. Write the article below the second `---` in Markdown: a blank line between paragraphs, `## ` for a heading, `[text](address)` for a link, `*word*` for italics. To link to a guide, put `../` in front: `[the pricing guide](../pricing.html#rule-2-2)`.
5. For the Indonesian version, save a file with **the same name** in `id/_posts/`. The EN | ID switch then moves between the two. An article can also be in one language only; the switch then opens the other language's list of articles.

The date in the file name is the publication date shown on the page. The site adds the reading time, the search entry, the sitemap entry, and links to glossary terms. A file dated in the future is skipped. It appears with the first build after that date, which happens on your next commit (or click **Run workflow** in the Actions tab).

## Add a guide

Copy a guide file in the same half and change the top section. Three lines place it on the site:

- `pillar: build` or `pillar: buy` puts it in that half: on the home page, the Guides page, the tabs at the top of each guide, and the previous/next links.
- `order:` sets its place in the lists (Buy guides are 1 to 5, Build guides 6 to 8).
- `number:` is the letter or number shown on its card and in its rule numbers, for example `"F"` with rules `"F.1"`, `"F.2"`.

A guide checked more recently than the others can carry its own date: `reviewed: 14 October 2026`.

## Add an open project

Add an entry to `_data/en/projects.yml` and the same `id` to `_data/id/projects.yml`. Say what the project is, its licence, and what its own documents say about medical use. Link to the source of each claim. Listing is not a recommendation: never rate or praise a project.

## Things the site does for you

- **Glossary terms link themselves.** Each term in `glossary.yml` has a `find:` list of the words that mark it. The first use on each page links to its definition, with the definition as a tooltip. Words in lowercase match any capitals; words with capitals must match exactly.
- **Indonesian terms on English pages** written as `*izin edar*` are marked as Indonesian, so screen readers pronounce them correctly.
- **Reading time**, rule counts and "Last reviewed" are filled in automatically. Change the date in `ui.yml` when you recheck the guides.
- **New versions reach every visitor.** File names carry a version, so no one gets new pages with old styles.

## The automatic check

After every build, GitHub runs two checks before publishing:

- `tools/check.py`: broken links and anchors, a page missing in one language, different anchors between the languages, missing or over-long titles and descriptions, duplicate ids, and anything the security policy would block.
- `tools/content_report.py --strict`: a rule without an example, or an abbreviation that is not in the glossary. The report also lists sentences over 25 words and words to avoid, as advice only.

If either fails, the live site stays as it was. Fix what the message names and commit again.

## Add a dossier

1. Copy `drafts/dossier-template.md` to `dossiers/DEVICE-NAME.md`, and `drafts/dossier-template-id.md` to `id/dossiers/DEVICE-NAME.md`. Use the same file name in both.
2. Replace every word in CAPITALS in both. Keep every row of the specification table; write "not applicable" ("tidak berlaku") where one does not apply. The check fails while a placeholder link (`URL`) is left.
3. In `_data/en/dossiers.yml` and `_data/id/dossiers.yml`, change the row's `status` to a link, for example `"[Read the dossier](dossiers/DEVICE-NAME.html)"`.
4. Before publishing, apply the two publication rules on the Dossiers page: public sources only, and no tender still under evaluation.

## Before you publish widely

1. Get written approval from your supervisor. The disclosure on the About page says you work in public-sector procurement and develop medical technology, and does not name your employer.
2. Add a contact line to `about.md` and `id/about.md`. Search for `CONTACT` and `KONTAK`.
3. Check the name: the domain, the PDKI trademark database, and the similarity to the Ministry of Health's SATUSEHAT.
4. Read every page once, in both languages, on a computer and on a phone.
5. Recheck the regulation page. Its rules were checked on 11 October 2026 against the sources at its foot.
6. Step 5 of "How a dossier is made" promises that a clinical user reads each dossier before publication. Keep it only if you will do it.

## Publishing settings

- **Settings > Pages > Build and deployment > Source: GitHub Actions.** The workflow is `.github/workflows/jekyll-gh-pages.yml`. Keep it as the only workflow that deploys.
- The address is set in `_config.yml` (`url` and `baseurl`). For a custom domain, set `url` to it and `baseurl` to `""`, and add the domain under Settings > Pages.

## Preview on your own computer (optional)

With Ruby installed:

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000/sistemsehat/>. Run the checks with `python3 tools/check.py` and `python3 tools/content_report.py`.

## How the site is built to work

**Two languages.** Every page has an EN | ID switch that opens the same page in the other language at the same place. Visitors whose browser is set to Indonesian are offered the Indonesian page; they are never redirected. Checklist ticks are shared between languages.

**Phones.** Checked from 320 to 414 pixels wide. Nothing scrolls sideways, tables become stacked blocks, and every link and button is at least 44 pixels tall.

**Accessibility.** Checked against WCAG 2.2 AA with axe on all pages (no violations), plus keyboard use, screen-reader wording and Windows High Contrast mode.

**Speed and security.** No third-party scripts, fonts or trackers. Fonts are hosted with the site, with fallbacks scaled so nothing jumps while they load. Each page carries a Content Security Policy that allows only the site's own files and one tiny inline script, by its hash (in `_config.yml`).

**Search** runs in the browser over an index built from the same files as the pages (`assets/search-index.js`).

## Fonts

Public Sans and Barlow Condensed, both under the SIL Open Font License. The licence texts are in `assets/fonts/` and must stay with the font files. The fallback settings at the top of `style.css` were calculated for these fonts; if you change a typeface, they need recalculating.
