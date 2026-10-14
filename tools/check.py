"""Checks the built site. GitHub runs it after every build (see .github/workflows); to run it yourself:

    bundle exec jekyll build && python3 tools/check.py          # checks _site/
    python3 tools/check.py path/to/built/site

Exits with an error if anything is broken, and then the site is not published.
Python 3.9 or newer, standard library only.
"""
import base64
import hashlib
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

DOCS = Path(__file__).resolve().parent.parent / "_site"
MAX_TITLE, MAX_DESC = 70, 160


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.dupes, self.links, self.inline_scripts = [], [], [], []
        self.lang = self.title = self.desc = self.csp = None
        self.h1 = 0
        self.inline_styles = 0
        self._in = None
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            (self.dupes if a["id"] in self.ids else self.ids).append(a["id"])
        if "style" in a:
            self.inline_styles += 1
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "h1":
            self.h1 += 1
        elif tag == "meta" and a.get("name") == "description":
            self.desc = a.get("content", "")
        elif tag == "meta" and a.get("http-equiv", "").lower() == "content-security-policy":
            self.csp = a.get("content", "")
        elif tag == "style":
            self.inline_styles += 1
        for attr in ("href", "src"):
            if attr in a and not (tag == "link" and a.get("rel") in ("canonical", "alternate")):
                self.links.append(a[attr])
        if tag in ("title", "script") and not (tag == "script" and "src" in a):
            self._in, self._buf = tag, ""

    def handle_data(self, data):
        if self._in:
            self._buf += data

    def handle_endtag(self, tag):
        if tag == self._in:
            if tag == "title":
                self.title = self._buf.strip()
            else:
                self.inline_scripts.append(self._buf)
            self._in = None


def main():
    global DOCS
    if len(sys.argv) > 1:
        DOCS = Path(sys.argv[1]).resolve()
    if not DOCS.exists():
        sys.exit(f"{DOCS} does not exist. Build the site first: bundle exec jekyll build")
    problems = []
    pages = {p: Page() for p in sorted(DOCS.rglob("*.html"))}
    for path, parsed in pages.items():
        parsed.feed(path.read_text(encoding="utf-8"))

    for path, p in pages.items():
        rel = path.relative_to(DOCS).as_posix()
        def bad(msg):
            problems.append(f"{rel}: {msg}")

        if p.lang not in ("en", "id"):
            bad(f"<html lang> is {p.lang!r}")
        if p.h1 != 1:
            bad(f"{p.h1} <h1> elements (expected 1)")
        if not p.title or len(p.title) > MAX_TITLE:
            bad(f"title missing or longer than {MAX_TITLE} characters: {p.title!r}")
        if not p.desc or len(p.desc) > MAX_DESC:
            bad(f"description missing or longer than {MAX_DESC} characters")
        if p.dupes:
            bad(f"duplicate ids {sorted(set(p.dupes))}")
        if p.inline_styles:
            bad(f"{p.inline_styles} inline style(s); the security policy blocks them, use a class in style.css")
        if not p.csp:
            bad("no Content-Security-Policy")
        for code in p.inline_scripts:
            digest = "sha256-" + base64.b64encode(hashlib.sha256(code.encode()).digest()).decode()
            if digest not in (p.csp or ""):
                bad("inline script not allowed by the page's security policy (its hash is not listed)")

        for link in p.links:
            parts = urlsplit(link)
            if parts.scheme or link.startswith(("//", "mailto:")):
                continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path.resolve()
            if not target.exists():
                bad(f"broken link {link}")
            elif parts.fragment and target.suffix == ".html":
                twin = pages.get(target)
                if twin is not None and parts.fragment not in twin.ids:
                    bad(f"link to missing anchor {link}")

    # every English page has an Indonesian twin with the same anchors, so the switch keeps your place
    for path, p in pages.items():
        if path.parent != DOCS or path.name == "404.html":
            continue
        twin_path = DOCS / "id" / path.name
        twin = pages.get(twin_path)
        if twin is None:
            problems.append(f"{path.name}: no Indonesian page id/{path.name}")
            continue
        strip = lambda ids: {i for i in ids if not i.startswith("letter-")}  # A-Z jump letters differ by language
        missing, extra = strip(p.ids) - strip(twin.ids), strip(twin.ids) - strip(p.ids)
        if missing:
            problems.append(f"id/{path.name}: anchors only in English {sorted(missing)}")
        if extra:
            problems.append(f"id/{path.name}: anchors only in Indonesian {sorted(extra)}")

    sitemap = DOCS / "sitemap.xml"
    if sitemap.exists():
        locs = re.findall(r"<loc>([^<]+)</loc>", sitemap.read_text(encoding="utf-8"))
        if len(locs) != len([p for p in pages if p.name != "404.html"]):
            problems.append(f"sitemap.xml lists {len(locs)} pages; the site has {len(pages) - 1}")

    if problems:
        print(f"{len(problems)} problem(s):")
        for line in problems:
            print("  " + line)
        sys.exit(1)
    print(f"OK: {len(pages)} pages checked. Links, anchors, language twins, titles, descriptions and security policy are fine.")


if __name__ == "__main__":
    main()
