# SistemSehat website

Independent guidance on specifying, pricing and procuring medical equipment, in English and Indonesian. A static site: plain HTML, one stylesheet, one small script, self-hosted fonts and no requests to any other server. It is built by a short Python program, so every rule and every label is written once.

## What is in this folder

| Folder | What it is |
| --- | --- |
| `docs/` | The website, ready to publish. GitHub Pages serves this folder. **Built automatically: do not edit it by hand.** |
| `src/` | Where you edit. `content_en.py` and `content_id.py` hold the words; `assets/` holds the design, the script, fonts and icons |
| `tools/check.py` | Checks the built site: links, anchors, the two languages, titles and the security policy |
| `tools/content_report.py` | Checks the writing: long sentences, words to avoid, unexplained abbreviations, rules without an example |
| `WRITING-GUIDE.md` | How to write for the site, in both languages: voice, how a rule is built, the word list |
| `drafts/` | Templates for hand-written pages, such as a dossier |
| `.github/workflows/` | Runs the build and the checks on GitHub every time you push |

English pages are at the top of `docs/`, Indonesian pages in `docs/id/` with the same file names.

## Change the content

1. Edit `src/content_en.py` and `src/content_id.py` in any text editor. Each page is a block of HTML inside the file, under a comment line that ends with the page's name (for example `Pricing`).
2. Build the site:

   ```bash
   python3 src/build.py
   ```

   Python 3.9 or newer, nothing else to install. On Windows, type `python` instead of `python3`.
3. Check it:

   ```bash
   python3 tools/check.py
   python3 tools/content_report.py
   ```

4. Open `docs/index.html` in a browser to look, then publish.

Things the build does for you:

- **A rule is written once.** Each rule is a `clause(...)` in its guide, with a heading, an explanation, an example and an "Ask yourself" question (see WRITING-GUIDE.md). The list of rules at the top of the guide, the checklist and the search index are all built from it.
- **The two languages are kept in step.** A rule needs the same number (for example `3.7`) in both files. The build stops if the two languages have a different number of rules, and the check fails if a page's anchors differ between languages, because the EN | ID switch uses them to keep the reader's place.
- **Indonesian terms on English pages.** Wrap them in `<em>`, as in `<em>izin edar</em>`. The build marks them as Indonesian so screen readers pronounce them correctly.
- **Glossary terms link themselves.** Each glossary entry has an id, the term, the definition and the patterns that find it in text, for example `("hps", "HPS", "...", [r"\bHPS\b"])`. The first use of each term on every page becomes a link to its definition. Keep the id the same in both languages.
- **Reading time** under each guide's title is counted by the build.
- **Latest updates** on the home page are hand-written in each language. Add a line to both when you publish something new.

Colours and type sizes are at the top of `src/assets/style.css`, under `:root`. Behaviour is in `src/assets/site.js`.

## Before you publish

A GitHub Pages site is public as soon as it is deployed. On a free GitHub account the repository must be public as well.

1. Get written approval from your supervisor for the site. The disclosure on the About page says you work in public-sector procurement and does not name your employer.
2. Add a contact line to the About page in both languages. Search `src/content_en.py` for `CONTACT` and `src/content_id.py` for `KONTAK`.
3. Check the name. Confirm the domain you want is free and search the PDKI trademark database. The Ministry of Health's national platform is called SATUSEHAT, so decide whether the similarity is acceptable to you. To rename, search and replace `SistemSehat` in `src/` and rebuild.
4. Read every page once, in both languages, on a computer and on a phone. The Indonesian pages are written for Indonesian readers rather than translated word for word (they say HPS where the English says "the estimate", for example). Change anything you would not sign.
5. Recheck the regulation page. Its rules were checked on 11 October 2026 against the sources listed at its foot. Update the "Last reviewed" date (`REVIEWED` at the top of each content file) when you recheck.
6. Read the six steps under "How a dossier is made" on the Dossiers page. Step 5 promises that a clinical user reads each dossier before publication. Keep it only if you will do it.

## Publish on GitHub Pages

With git (recommended, because it also uploads the hidden `.github` folder that runs the checks):

```bash
cd sistemsehat
git init -b main
git add .
git commit -m "Publish SistemSehat"
git remote add origin https://github.com/YOUR-USERNAME/sistemsehat.git
git push -u origin main
```

With the GitHub website: create a public repository, choose **Add file**, then **Upload files**, and drag in the `docs`, `src`, `tools` and `drafts` folders and `README.md`. Hidden files (`.github`, `.gitignore`, `docs/.nojekyll`) may not come along this way. The site works without them; only the automatic checks need `.github`.

Then turn the site on: **Settings**, **Pages**, **Build and deployment**, source **Deploy from a branch**, branch **main**, folder **/docs**, **Save**. After a minute or two the site is at `https://YOUR-USERNAME.github.io/sistemsehat/` and the Indonesian version at `.../sistemsehat/id/`.

### Then tell the build its address

Open `src/config.py` and set `SITE_URL` to that address, for example `"https://YOUR-USERNAME.github.io/sistemsehat/"`. Rebuild and publish again. This adds what needs a full address:

- language links that tell Google which English and Indonesian pages belong together
- link previews when someone shares a page on WhatsApp, LinkedIn or Facebook (an image and a summary, in the page's language)
- `docs/sitemap.xml`, which you can submit in Google Search Console
- absolute links on the 404 page, so it works at any depth

## Automatic checks

Every push to GitHub runs `.github/workflows/check.yml`. It rebuilds the site from `src/` and fails if:

- `docs/` was not rebuilt after a change in `src/` (run `python3 src/build.py` and push again), or
- anything `tools/check.py` looks for is wrong: a broken link or anchor, a page missing in one language, a missing or over-long title or description, duplicate ids, inline styles, or a script the security policy would block.

- a rule has no example, or an abbreviation is not in the glossary (`tools/content_report.py --strict`).

A red cross next to a commit on GitHub means one of these. The message in the **Actions** tab says which.

## Add a dossier

Dossiers are hand-written pages for now:

1. Copy `drafts/dossier-template.html` to `src/static/dossiers/DEVICE-NAME.html`, and `drafts/dossier-template-id.html` to `src/static/id/dossiers/DEVICE-NAME.html`. Use the same file name in both.
2. Replace the words in capitals in both, including `DEVICE-NAME` in the EN | ID switch near the top. Keep every row of the specification table; write "not applicable" ("tidak berlaku") where one does not apply.
3. In both content files, replace the matching "In preparation" row with a link to the new page.
4. Build and check. The check fails until every placeholder link is filled in and both languages exist.
5. Before publishing, apply the two publication rules on the Dossiers page: public sources only, and no tender still under evaluation.

Everything in `src/static/` is copied into `docs/` as it is.

## How the site is built to work

**Two languages.** Every page has an EN | ID switch. It opens the same page in the other language at the same place: rule 3.7 stays rule 3.7, and a search keeps its words. Visitors whose browser is set to Indonesian are offered the Indonesian page in a small notice; they are never redirected, and their choice is remembered. Checklist ticks are shared between languages.

**Phones.** Checked from 320 to 414 pixels wide, on tablets and turned sideways. Nothing scrolls sideways; tables become stacked blocks; the header stays in reach with search, language and menu; every link and button is at least 44 pixels tall; search boxes use 16-pixel text so iPhones do not zoom; long pages have a back-to-top button.

**Accessibility.** Checked against WCAG 2.2 AA with axe on all 26 pages (no violations), plus what automatic tools miss: keyboard use with the sticky header, screen-reader wording, Windows High Contrast mode, and Indonesian words marked as Indonesian on English pages. Tables keep their meaning for screen readers when stacked on phones.

**Speed and stability.** Lighthouse on a simulated mid-range phone: performance 98 to 100, layout shift 0. Fonts are hosted with the site, and the text is first set in Arial or Roboto scaled to the same width, so nothing jumps when the fonts arrive. Gzipped by GitHub, a page loads about 9 KB of CSS and 5 KB of script. File names carry a version (`style.css?v=...`), so after an update no one gets new pages with old styles.

**Security.** No third-party scripts, fonts or trackers. Each page carries a Content Security Policy that only allows files from the site itself and the one tiny inline script, by its hash. The hash is computed by the build, so it stays correct if that script changes.

**Search** runs in the browser over a prebuilt index, one per language. Matches are highlighted and each result shows the passage around the match.

## Fonts

Public Sans and Barlow Condensed, both under the SIL Open Font License. The licence texts are in `src/assets/fonts/` and must stay with the font files.

The fallback settings at the top of `style.css` (`size-adjust` and the `-override` values) were calculated from these font files and the site's own text. If you change a typeface, they need recalculating, or text will shift slightly while the new font loads.
