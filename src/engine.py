"""Shared engine for the SistemSehat generator: page shell, building blocks and writers.

Each content module (content_en.py, content_id.py) calls begin() first and then builds its pages
with the helpers here. The helpers read the current language from S, so a module's rules, labels
and links stay in that language. Python 3.9 or newer, standard library only.
"""
import base64
import hashlib
import json
import re
from pathlib import Path

from config import SITE_URL as _SITE_URL

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DOCS = ROOT / "docs"        # the built website; GitHub Pages serves this folder
DRAFTS = ROOT / "drafts"    # templates for pages written by hand, kept off the site

SITE_URL = _SITE_URL.strip()
if SITE_URL and not SITE_URL.endswith("/"):
    SITE_URL += "/"

S = {}
VERSIONS = {}   # asset file name -> short content hash, appended as ?v= so browsers never mix old and new files

LANGS = ("en", "id")
LANG_NAMES = {"en": ("EN", "English"), "id": ("ID", "Bahasa Indonesia")}
OG_LOCALE = {"en": "en_US", "id": "id_ID"}

# Runs before the first paint, so phone layouts never flash the unfolded menu while site.js loads.
INLINE_JS = 'document.documentElement.classList.add("js")'
INLINE_JS_HASH = "sha256-" + base64.b64encode(hashlib.sha256(INLINE_JS.encode()).digest()).decode()

# GitHub Pages cannot send security headers, so the policy travels in a meta tag.
# Everything is served from the site itself; the one inline script is allowed by its hash.
CSP = ("default-src 'self'; script-src 'self' '" + INLINE_JS_HASH + "'; style-src 'self'; img-src 'self'; "
       "font-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'self'; object-src 'none'")

# Fonts are not preloaded: the metric-matched fallbacks in style.css keep the layout still while they load,
# and leaving them off the critical path gives the fastest Largest Contentful Paint on slow connections.
PRELOAD_FONTS = []

ICONS = {
    "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M10 13h6M10 17h6"/>',
    "tag": '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
    "route": '<circle cx="5" cy="6" r="2"/><path d="M7 6h7a3 3 0 0 1 0 6h-4a3 3 0 0 0 0 6h8"/><path d="M16 15l3 3-3 3"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.2 7.8-8 9-4.8-1.2-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "monitor": '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M6 11h3l1.5-3 2.5 6 1.5-3H18"/><path d="M9 21h6M12 17v4"/>',
    "check": '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M8 12l3 3 5-6"/>',
    "book": '<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/>',
    "shelf": '<path d="M5 4v16M9 4v16M13 6l5 14"/><path d="M3 20h18"/>',
    "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
    "folder": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
}


def begin(lang, ui, guides, nav, labels, reviewed):
    """Start a language: everything built after this call uses these strings."""
    S.clear()
    S.update(lang=lang, ui=ui, guides=guides, guide_files=[g[0] for g in guides],
             nav=nav, labels=labels, reviewed=reviewed,
             registry=[], glossary=[], library=[])


def U(key, **kw):
    text = S["ui"][key]
    return text.format(**kw) if kw else text


def icon(name):
    return ('<svg class="icon" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" '
            'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
            + ICONS[name] + "</svg>")


def strip_tags(text):
    text = re.sub(r"<[^>]+>", "", text)
    for entity, char in [("&ldquo;", "“"), ("&rdquo;", "”"), ("&amp;", "&"), ("&#8209;", "-"), ("&copy;", "(c)")]:
        text = text.replace(entity, char)
    return text


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", strip_tags(text).lower()).strip("-")


def anchor(no):
    return "rule-" + no.lower().replace(".", "-")


def rules_for(prefix):
    return [r for r in S["registry"] if r[0].startswith(prefix + ".")]


def asset(aroot, name):
    """URL of a file in assets/, with a content hash so a new version is never served from a stale cache."""
    version = VERSIONS.get(name)
    return f"{aroot}assets/{name}" + (f"?v={version}" if version else "")


def public_url(lang, path):
    """Full public address of a page, or '' while SITE_URL is not set."""
    if not SITE_URL:
        return ""
    if path == "index.html":
        path = ""
    return SITE_URL + ("id/" if lang == "id" else "") + path


# ------------------------------------------------------------------ shell

def breadcrumb(filename, root, crumb):
    if filename in ("index.html", "404.html"):
        return ""
    trail = [(f"{root}index.html", U("home"))]
    if crumb:  # a page inside the dossiers folder
        trail.append((f"{root}dossiers.html", S["labels"]["dossiers.html"]))
        last = crumb
    elif filename in S["guide_files"]:
        trail.append((f"{root}guides.html", S["labels"]["guides.html"]))
        last = S["guides"][S["guide_files"].index(filename)][2]
    else:
        last = S["labels"][filename]
    items = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in trail)
    return f"""    <div class="wrap">
      <nav class="crumbs" aria-label="{U('crumbs_label')}">
        <ol>{items}<li aria-current="page">{last}</li></ol>
      </nav>
    </div>
"""


def guide_tabs(filename, root):
    if filename not in S["guide_files"]:
        return ""
    items = []
    for href, no, label, *_ in S["guides"]:
        current = ' aria-current="page"' if href == filename else ""
        items.append(f'          <li><a href="{root}{href}"{current}><span class="g-no">{no}</span> {label}</a></li>')
    items = "\n".join(items)
    return f"""    <div class="wrap">
      <nav class="guide-tabs" aria-label="{U('tabs_label')}">
        <ul>
{items}
        </ul>
      </nav>
    </div>
"""


def lang_switch(path, aroot):
    """EN | ID switch. The current language is plain text; the other is a link to the same page."""
    parts = []
    for code in LANGS:
        short, name = LANG_NAMES[code]
        inner = f'<span aria-hidden="true">{short}</span><span class="visually-hidden">{name}</span>'
        if code == S["lang"]:
            parts.append(f'<span class="lang-current" lang="{code}" aria-current="true">{inner}</span>')
        else:
            href = aroot + ("id/" if code == "id" else "") + path
            parts.append(f'<a href="{href}" lang="{code}" hreflang="{code}" title="{name}">{inner}</a>')
    return f'<nav class="lang-switch" aria-label="{U("lang_label")}">{"".join(parts)}</nav>'


def seo_head(filename, title, desc, path, noindex, crumb=None):
    """Canonical, language alternates and link-preview tags. Needs SITE_URL; empty without it.
    Hand-written pages (crumb set, e.g. dossiers) carry none of these until they are generated here too."""
    lang = S["lang"]
    if noindex:
        return '\n  <meta name="robots" content="noindex">'
    if not SITE_URL or crumb:
        return ""
    other = "id" if lang == "en" else "en"
    tags = [f'<link rel="canonical" href="{public_url(lang, path)}">']
    tags += [f'<link rel="alternate" hreflang="{code}" href="{public_url(code, path)}">' for code in LANGS]
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{public_url("en", path)}">')
    tags += [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="SistemSehat">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{public_url(lang, path)}">',
        f'<meta property="og:image" content="{SITE_URL}assets/og-{lang}.png">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{U("og_alt")}">',
        f'<meta property="og:locale" content="{OG_LOCALE[lang]}">',
        f'<meta property="og:locale:alternate" content="{OG_LOCALE[other]}">',
        '<meta name="twitter:card" content="summary_large_image">',
    ]
    return "\n  " + "\n  ".join(tags)


READING_TIME = "{{reading-time}}"
WORDS_PER_MINUTE = {"en": 200, "id": 180}
SKIP_TAGS = {"a", "h1", "h2", "h3", "h4", "h5", "h6", "label", "button", "thead", "title", "script", "style", "summary"}


def reading_time(body):
    words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", body)))
    minutes = max(1, round(words / WORDS_PER_MINUTE[S["lang"]]))
    return U("reading_time", n=minutes)


def link_terms(body, root=""):
    """Link the first use of each glossary term on a page to its definition, with the definition as a
    tooltip. Text inside links, headings, labels and buttons is left alone. A term already linked still
    blocks shorter terms inside it (so "Info Alkes" never yields a link on "Alkes")."""
    entries = []
    for tid, term, definition, *rest in S["glossary"]:
        patterns = rest[0] if rest else [re.escape(strip_tags(term))]
        tip = strip_tags(definition).replace('"', "&quot;")
        for pat in patterns:
            entries.append((re.compile(pat), tid, tip))
    used = set()
    out, stack = [], []
    for part in re.split(r"(<[^>]+>)", body):
        if part.startswith("<"):
            m = re.match(r"<(/?)([a-zA-Z0-9]+)", part)
            if m and not part.endswith("/>"):
                name = m.group(2).lower()
                if m.group(1):
                    if name in stack:
                        while stack and stack.pop() != name:
                            pass
                elif name in SKIP_TAGS:
                    stack.append(name)
            out.append(part)
            continue
        if stack or not part.strip():
            out.append(part)
            continue
        i, text, pieces = 0, part, []
        while True:
            best = None
            for rx, tid, tip in entries:
                m = rx.search(text, i)
                if m and (best is None or m.start() < best[0].start()
                          or (m.start() == best[0].start() and m.end() > best[0].end())):
                    best = (m, tid, tip)
            if best is None:
                break
            m, tid, tip = best
            if tid in used:
                pieces.append(text[i:m.end()])
            else:
                used.add(tid)
                pieces.append(text[i:m.start()])
                pieces.append(f'<a class="term" href="{root}glossary.html#{tid}" title="{tip}">{m.group(0)}</a>')
            i = m.end()
        pieces.append(text[i:])
        out.append("".join(pieces))
    return "".join(out)


def finalize(html):
    """Last pass over every page.

    Tables: explicit roles keep their meaning for screen readers on phones, where CSS stacks the
    rows into blocks (Safari drops table semantics once rows are display: block).
    English pages: an <em> without a lang marks an Indonesian term, so screen readers switch voice."""
    html = (html.replace("<table>", '<table role="table">')
                .replace("<thead>", '<thead role="rowgroup">')
                .replace("<tbody>", '<tbody role="rowgroup">')
                .replace("<tr>", '<tr role="row">')
                .replace('<th scope="col">', '<th scope="col" role="columnheader">')
                .replace('<th scope="row">', '<th scope="row" role="rowheader">')
                .replace("<td data-label=", '<td role="cell" data-label='))
    if S["lang"] == "en":
        html = html.replace("<em>", '<em lang="id">')
    return html


def page(filename, title, desc, body, root="", crumb=None, path=None, noindex=False):
    lang = S["lang"]
    aroot = root + ("../" if lang == "id" else "")  # assets live once, at the site root
    path = path or filename
    guide_files = S["guide_files"]
    nav_items = []
    for href, label in S["nav"]:
        on_guides = href == "guides.html" and filename in guide_files
        current = ' aria-current="page"' if (href == filename and not crumb) or on_guides else ""
        if crumb and href == "dossiers.html":
            current = ' aria-current="true"'
        nav_items.append(f'            <li><a href="{root}{href}"{current}>{label}</a></li>')
    nav = "\n".join(nav_items)
    foot_guides = "\n".join(
        f'          <li><a href="{root}{href}">{question}</a></li>' for href, _, _, question, *_ in S["guides"])
    index_script = ""
    if filename == "search.html":
        index_script = f'\n  <script src="{asset(aroot, S["index_file"])}" defer></script>'
    preload = "".join(f'\n  <link rel="preload" href="{aroot}assets/fonts/{f}" as="font" type="font/woff2" crossorigin>'
                      for f in PRELOAD_FONTS)
    labels = S["labels"]
    if READING_TIME in body:
        body = body.replace(READING_TIME, reading_time(body))
    if filename not in ("glossary.html", "404.html") and S["glossary"]:
        body = link_terms(body, root)
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Content-Security-Policy" content="{CSP}">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">{seo_head(filename, title, desc, path, noindex, crumb)}
  <meta name="theme-color" content="#ffffff">{preload}
  <link rel="icon" href="{aroot}assets/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{aroot}assets/apple-touch-icon.png">
  <link rel="stylesheet" href="{asset(aroot, 'style.css')}">
  <script>{INLINE_JS}</script>{index_script}
  <script src="{asset(aroot, 'site.js')}" defer></script>
</head>
<body>
  <a class="skip" href="#main">{U('skip')}</a>

  <header class="site-header">
    <div class="wrap header-row">
      <a class="wordmark" href="{root}index.html">SistemSehat</a>
      <a class="search-link" href="{root}search.html" aria-label="{U('search')}">{icon("search")}</a>
      {lang_switch(path, aroot)}
      <button class="menu-button" type="button" aria-expanded="false" aria-controls="site-menu" hidden><span class="menu-icon" aria-hidden="true"></span><span class="menu-label">{U('menu')}</span></button>
      <div class="site-menu" id="site-menu">
        <nav aria-label="{U('nav_label')}">
          <ul class="main-nav">
{nav}
          </ul>
        </nav>
        <form class="search" action="{root}search.html" method="get" role="search" aria-label="{U('search_label')}">
          <label class="visually-hidden" for="header-search">{U('search_label')}</label>
          <input id="header-search" type="search" name="q" placeholder="{U('search_placeholder')}" aria-keyshortcuts="/">
          <button type="submit" aria-label="{U('search')}">{icon("search")}</button>
        </form>
      </div>
    </div>
  </header>

  <main id="main">
{breadcrumb(filename, root, crumb)}{guide_tabs(filename, root)}{body}
  </main>

  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div class="footer-about">
        <p class="wordmark">SistemSehat</p>
        <p>{U('footer_about')}</p>
      </div>
      <nav aria-label="{U('f_guides_label')}">
        <h2>{labels['guides.html']}</h2>
        <ul>
{foot_guides}
        </ul>
      </nav>
      <nav aria-label="{U('f_tools')}">
        <h2>{U('f_tools')}</h2>
        <ul>
          <li><a href="{root}checklist.html">{labels['checklist.html']}</a></li>
          <li><a href="{root}glossary.html">{labels['glossary.html']}</a></li>
          <li><a href="{root}library.html">{labels['library.html']}</a></li>
          <li><a href="{root}search.html">{labels['search.html']}</a></li>
        </ul>
      </nav>
      <nav aria-label="{U('f_about_label')}">
        <h2>{U('f_about')}</h2>
        <ul>
          <li><a href="{root}about.html">{U('f_about_site')}</a></li>
          <li><a href="{root}about.html#how">{U('f_independent')}</a></li>
          <li><a href="{root}dossiers.html">{U('f_dossiers')}</a></li>
        </ul>
      </nav>
    </div>
    <div class="wrap footer-legal">
      <p>{U('legal')}</p>
      <p>&copy; 2026 SistemSehat</p>
    </div>
  </footer>
</body>
</html>
"""
    return finalize(html)


# ------------------------------------------------------------------ building blocks

def clause(no, heading, paras, test, example=""):
    """One rule: what to do (paras), a concrete example, and the question to ask yourself (test)."""
    S["registry"].append((no, heading, paras, test, example))
    ps = "\n".join(f"          <p>{p}</p>" for p in paras)
    # label and text are two boxes, so links inside the text cannot break the line apart
    ex = f'\n          <p class="example"><strong>{U("example")}</strong> <span>{example}</span></p>' if example else ""
    return f"""        <section class="rule" id="{anchor(no)}">
          <h2><span class="rule-no">{no}</span> {heading}</h2>
{ps}{ex}
          <p class="test"><strong>{U('test')}</strong> <span>{test}</span></p>
        </section>"""


def reviewed(checklist_anchor):
    prefix = checklist_anchor.split("-")[1].upper()
    count = len(rules_for(prefix))
    return f"""        <ul class="meta">
          <li>{U('last_reviewed', date=S['reviewed'])}</li>
          <li>{U('n_rules', n=count)}</li>
          <li>{READING_TIME}</li>
          <li><a href="checklist.html#{checklist_anchor}">{U('checklist_for_guide')}</a></li>
        </ul>"""


def keypoints(prefix):
    items = "\n".join(
        f'          <li><a href="#{anchor(no)}"><span class="rule-no">{no}</span> {heading}</a></li>'
        for no, heading, *_ in rules_for(prefix))
    return f"""      <aside class="keypoints" aria-labelledby="keypoints-title">
        <h2 id="keypoints-title">{U('key_points', n=len(rules_for(prefix)))}</h2>
        <ol>
{items}
        </ol>
      </aside>
"""


def related(prefix):
    count = len(rules_for(prefix))
    labels = S["labels"]
    return f"""      <section class="related" aria-labelledby="related-title">
        <h2 id="related-title">{U('related')}</h2>
        <ul class="link-list">
          <li><a href="checklist.html#guide-{prefix.lower()}">{U('checklist_for_guide')}</a><span>{U('rel_checklist', n=count)}</span></li>
          <li><a href="glossary.html">{labels['glossary.html']}</a><span>{U('rel_glossary')}</span></li>
          <li><a href="library.html">{labels['library.html']}</a><span>{U('rel_library')}</span></li>
          <li><a href="dossiers.html">{U('f_dossiers')}</a><span>{U('rel_dossiers')}</span></li>
        </ul>
      </section>
"""


def pager(filename):
    guides = S["guides"]
    i = S["guide_files"].index(filename)
    parts = []
    if i > 0:
        href, no, _, question, *_ = guides[i - 1]
        parts.append(f'        <a class="pager-prev" href="{href}"><span>{U("prev_guide")}</span><strong><span class="g-no">{no}</span> {question}</strong></a>')
    if i < len(guides) - 1:
        href, no, _, question, *_ = guides[i + 1]
        parts.append(f'        <a class="pager-next" href="{href}"><span>{U("next_guide")}</span><strong><span class="g-no">{no}</span> {question}</strong></a>')
    else:
        parts.append(f'        <a class="pager-next" href="checklist.html"><span>{U("finished")}</span><strong>{U("open_checklist")}</strong></a>')
    inner = "\n".join(parts)
    return f"""      <nav class="pager" aria-label="{U('pager_label')}">
{inner}
      </nav>"""


def guide_card(g, heading="h3"):
    href, no, label, question, summary, icon_name = g
    return f"""          <li class="card">
            <div class="card-top"><span class="badge">{no}</span>{icon(icon_name)}</div>
            <{heading}><a href="{href}">{question}</a></{heading}>
            <p>{summary}</p>
            <p class="card-more">{U('guide_more', label=label, label_lower=label.lower())}</p>
          </li>"""


def tool_card(href, title, text, icon_name, heading="h3"):
    return f"""          <li class="card">
            <div class="card-top">{icon(icon_name)}</div>
            <{heading}><a href="{href}">{title}</a></{heading}>
            <p>{text}</p>
          </li>"""


def table(headers, rows):
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = []
    for r in rows:
        cells = f'<th scope="row">{r[0]}</th>' + "".join(
            f'<td data-label="{h}">{c}</td>' for h, c in zip(headers[1:], r[1:]))
        body.append(f"              <tr>{cells}</tr>")
    body = "\n".join(body)
    return f"""        <div class="table-wrap">
          <table>
            <thead>
              <tr>{head}</tr>
            </thead>
            <tbody>
{body}
            </tbody>
          </table>
        </div>"""


def checklist_groups():
    """The progress bar, then one group per guide, built from the rules already registered for this language.
    The bar is in the HTML (shown only with JavaScript) so its space is reserved from the first paint."""
    total = len(S["registry"])
    parts = [f"""        <div class="check-progress" id="check-progress">
          <p><strong id="check-count">{U('check_count', n=0, total=total)}</strong><small id="check-note">{U('check_note')}</small></p>
          <button type="button" class="button button-quiet button-small" id="check-clear" disabled>{U('check_clear')}</button>
        </div>"""]
    for href, key, label, question, *_ in S["guides"]:
        items = []
        for no, heading, paras, test, *_ in rules_for(key):
            cid = "c-" + no.lower().replace(".", "-")
            items.append(
                f'            <li><input type="checkbox" id="{cid}"><label for="{cid}">'
                f'<span class="check-no">{no}</span> {test}</label>'
                f'<a class="rule-link" href="{href}#{anchor(no)}">{heading}</a></li>')
        items = "\n".join(items)
        parts.append(f"""        <section class="check-group" id="guide-{key.lower()}">
          <h2><span class="g-no">{key}</span> <a href="{href}">{question}</a></h2>
          <ul class="checks">
{items}
          </ul>
        </section>""")
    return "\n".join(parts)


def glossary_list(terms):
    """terms: (anchor id, term, definition, patterns). Ids are shared across languages so links survive a
    switch. patterns are regular expressions that find the term in running text; the first match on each
    page becomes a link to its definition (see link_terms). Sorted by the term as shown in this language."""
    terms = sorted(terms, key=lambda t: strip_tags(t[1]).lower())
    S["glossary"][:] = terms
    letters, rows = [], []
    for tid, term, definition, *_ in terms:
        letter = strip_tags(term)[0].upper()
        first = letter not in letters
        if first:
            letters.append(letter)
        dt_id = f' id="letter-{letter.lower()}"' if first else ""
        rows.append(f'        <div id="{tid}"><dt{dt_id}>{term}</dt><dd>{definition}</dd></div>')
    az = "".join(f'<li><a href="#letter-{l.lower()}">{l}</a></li>' for l in letters)
    return az, "\n".join(rows), len(terms)


def library_group(title, rows):
    S["library"].extend(rows)
    return f"""        <h2>{title}</h2>
{table(S["ui"]["library_headers"], rows)}"""


# ------------------------------------------------------------------ writing

def short_hash(data):
    return hashlib.sha256(data).hexdigest()[:10]


def write_language(mod):
    """Write the search index, every page and the dossier template for the language just built."""
    lang = S["lang"]
    base = DOCS if lang == "en" else DOCS / lang
    base.mkdir(parents=True, exist_ok=True)

    index = []
    for href, no, label, question, summary, _ in S["guides"]:
        index.append({"t": question, "x": summary, "u": href, "k": U("k_guide")})
        for rno, heading, paras, test, example in rules_for(no):
            index.append({"t": f"{rno} {strip_tags(heading)}",
                          "x": " ".join(strip_tags(t) for t in (" ".join(paras), example, test) if t),
                          "u": f"{href}#{anchor(rno)}", "k": U("k_rule", label=label, label_lower=label.lower())})
    for tid, term, definition, *_ in S["glossary"]:
        index.append({"t": strip_tags(term), "x": strip_tags(definition),
                      "u": f"glossary.html#{tid}", "k": S["labels"]["glossary.html"]})
    for row in S["library"]:
        index.append({"t": strip_tags(row[0]), "x": f"{strip_tags(row[1])}. {strip_tags(row[2])}",
                      "u": "library.html", "k": S["labels"]["library.html"]})
    for fname, title, text in mod.INDEX_PAGES:
        index.append({"t": title, "x": text, "u": fname, "k": U("k_page")})
    name = "search-index.js" if lang == "en" else f"search-index-{lang}.js"
    data = ("window.SISTEMSEHAT_INDEX = " + json.dumps(index, ensure_ascii=False, indent=1) + ";\n").encode("utf-8")
    (DOCS / "assets" / name).write_bytes(data)
    VERSIONS[name] = short_hash(data)
    S["index_file"] = name

    for filename, title, desc, body in mod.PAGES:
        (base / filename).write_text(page(filename, title, desc, body), encoding="utf-8")

    title, desc, crumb, body, draft_name = mod.TEMPLATE
    DRAFTS.mkdir(parents=True, exist_ok=True)
    (DRAFTS / draft_name).write_text(
        page("dossiers.html", title, desc, body, root="../", crumb=crumb, path="dossiers/DEVICE-NAME.html"),
        encoding="utf-8")
    return len(mod.PAGES), len(index), len(S["registry"])


def write_404():
    """GitHub Pages serves 404.html for any missing address, at any depth, so its links are absolute
    when SITE_URL is known. Bilingual, because the visitor's language is not known."""
    root = SITE_URL
    body = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Page not found</h1>
        <p class="lead">The page may have moved, or the address may have a typo.</p>
        <p class="lead" lang="id">Halaman tidak ditemukan. Mungkin halaman sudah dipindahkan, atau ada salah ketik pada alamatnya.</p>
      </header>
      <div class="prose">
        <ul class="link-list">
          <li><a href="{root}index.html">Home</a><span>Start from the job in front of you</span></li>
          <li lang="id"><a href="{root}id/index.html">Beranda</a><span>Mulai dari pekerjaan yang sedang Anda hadapi</span></li>
          <li><a href="{root}guides.html">Guides</a><span>Five guides and their rules</span></li>
          <li lang="id"><a href="{root}id/guides.html">Panduan</a><span>Lima panduan beserta prinsipnya</span></li>
          <li><a href="{root}search.html">Search</a><span>Find a rule or a term</span></li>
          <li lang="id"><a href="{root}id/search.html">Pencarian</a><span>Cari prinsip atau istilah</span></li>
        </ul>
      </div>
    </div>"""
    html = page("404.html", "Page not found | SistemSehat",
                "The page you asked for is not on SistemSehat.", body, root=root, path="index.html", noindex=True)
    (DOCS / "404.html").write_text(html, encoding="utf-8")


def write_sitemap(paths):
    """sitemap.xml with language pairs. robots.txt only works at the root of a domain, so it is
    written only when the site has one (a custom domain), not for github.io/REPOSITORY/ addresses."""
    if not SITE_URL:
        return False
    rows = []
    for lang in LANGS:
        for path in paths:
            alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{code}" href="{public_url(code, path)}"/>'
                           for code in LANGS)
            rows.append(f"  <url>\n    <loc>{public_url(lang, path)}</loc>{alts}\n  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    (DOCS / "sitemap.xml").write_text(xml, encoding="utf-8")
    if re.match(r"^https?://[^/]+/$", SITE_URL):
        (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    return True
