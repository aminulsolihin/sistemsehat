"""Content report: how readable the built site is, and where the writing breaks WRITING-GUIDE.md.

    bundle exec jekyll build && python3 tools/content_report.py     # reads _site/

Advisory: it lists things to look at and never fails a build, because good writing is a judgement.
Add --strict to fail when a rule has no example or an abbreviation is not in the glossary.
Python 3.9 or newer, standard library only.
"""
import html
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "_site"
# names everyone in the audience knows, and edition codes such as AMD1 in "IEC 60601-1:2005+AMD1:2012"
ALLOWED = {"EN", "ID", "US", "PLN", "NEST360", "BPJS"}
PAGES = ["index", "guides", "specification", "pricing", "process", "regulation", "technology",
         "checklist", "glossary", "library", "dossiers", "about", "search"]
LONG = 25  # words; sentences longer than this are listed

# Words and phrases the writing guide asks writers to avoid, with what to use instead.
AVOID = {
    "en": {
        r"\bvendors?\b": "supplier", r"\block-in\b": "tied to one supplier", r"\blike with like\b": "on the same basis",
        r"\bspread\b": "difference", r"\btrack record\b": "history in use", r"\bshuts? out\b": "keeps out",
        r"\bon purpose\b": "deliberately", r"\bin the open\b": "publicly", r"\bout of date\b": "outdated",
        r"\bfactory gate\b": "as it leaves the factory", r"\bmidpoint\b": "halfway point", r"\bstarter\b": "first supply of",
        r"\bsign-off\b": "approval", r"\bweighs\b": "is stronger than", r"\bhopeful\b": "(say what you mean)",
        r"\bleverage\b": "use", r"\butili[sz]e\b": "use", r"\bin order to\b": "to", r"\bvia\b": "through",
        r"\be\.g\.": "for example", r"\bi\.e\.": "that is", r"\betc\.": "(list the items)",
    },
    "id": {
        r"\bkaidah\w*\b": "prinsip", r"\bvendor\b": "penyedia", r"\bdsb\.?": "(sebutkan semuanya)",
        r"\bdll\.?": "(sebutkan semuanya)", r"\byaitu adalah\b": "yaitu",
        r"\bsangatlah\b": "sangat", r"\bdaripada\b(?= [a-z]+ (?:yang|untuk))": "(periksa: 'daripada' hanya untuk perbandingan)",
    },
}


def blocks(path):
    h = path.read_text(encoding="utf-8")
    m = re.search(r"<main[^>]*>(.*)</main>", h, re.S)
    h = m.group(1) if m else h
    h = re.sub(r"<(script|style|svg|noscript)[^>]*>.*?</\1>", " ", h, flags=re.S)
    h = re.sub(r"<nav[^>]*>.*?</nav>", " ", h, flags=re.S)
    h = re.sub(r"<strong>(Example|Contoh|Ask yourself|Tanyakan)</strong>", " ", h)  # labels are not prose
    out = []
    for tag, inner in re.findall(r"<(p|li|td|dd)[^>]*>(.*?)</\1>", h, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", " ", inner))
        t = re.sub(r"\s+", " ", t).strip()
        t = re.sub(r" ([,.;:?!])", r"\1", t)
        if t:
            out.append(t)
    return out, h


def sentences(texts):
    out = []
    for t in texts:
        for s in re.split(r"(?<=[.?!])\s+(?=[A-Z0-9“\"(])", t):
            if len(s.split()) >= 3:
                out.append(s)
    return out


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(1, n)


def grade(sents):
    words = [w for s in sents for w in re.findall(r"[A-Za-z][A-Za-z'-]*", s)]
    if not sents or not words:
        return 0.0
    return 0.39 * len(words) / len(sents) + 11.8 * sum(map(syllables, words)) / len(words) - 15.59


def main():
    global DOCS
    strict = "--strict" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if paths:
        DOCS = Path(paths[0])
    if not DOCS.exists():
        sys.exit(f"{DOCS} does not exist. Build the site first: bundle exec jekyll build")
    problems = 0
    for lang, base in (("en", DOCS), ("id", DOCS / "id")):
        gloss = (base / "glossary.html").read_text(encoding="utf-8")
        known = set(re.findall(r"\b[A-Z][A-Z0-9]{1,}\b", html.unescape(re.sub(r"<[^>]+>", " ", " ".join(re.findall(r"<dt[^>]*>.*?</dt>", gloss))))))
        print(f"\n=== {'English' if lang == 'en' else 'Indonesian'}")
        print(f"  {'page':14} {'sentences':>9} {'words/sentence':>15} {'over ' + str(LONG):>8}" + ("  grade" if lang == "en" else ""))
        all_s, longs, avoid_hits, no_example, unknown = [], [], [], [], {}
        for name in PAGES:
            texts, raw = blocks(base / f"{name}.html")
            s = sentences(texts)
            all_s += s
            lens = [len(x.split()) for x in s] or [0]
            over = [x for x in s if len(x.split()) > LONG]
            longs += [(len(x.split()), name, x) for x in over]
            print(f"  {name:14} {len(s):9} {sum(lens) / max(1, len(s)):15.1f} {len(over):8}" + (f"  {grade(s):5.1f}" if lang == "en" else ""))
            for rule in re.findall(r'<section class="rule" id="([^"]+)">(.*?)</section>', raw, re.S):
                if 'class="example"' not in rule[1]:
                    no_example.append(f"{name}#{rule[0]}")
            text = " ".join(texts)
            for pat, use in AVOID[lang].items():
                for m in re.finditer(pat, text, re.I):
                    avoid_hits.append(f'{name}: "{m.group(0)}" -> {use}')
            if name != "glossary":
                for a in re.findall(r"\b[A-Z][A-Z]{1,}[0-9]*\b", text):
                    if a not in known and a not in ALLOWED and not re.match(r"AMD\d", a):
                        unknown.setdefault(a, set()).add(name)
        lens = [len(x.split()) for x in all_s]
        print(f"  {'ALL':14} {len(all_s):9} {sum(lens) / len(lens):15.1f} {len(longs):8}" + (f"  {grade(all_s):5.1f}" if lang == "en" else ""))
        if longs:
            print(f"  Sentences over {LONG} words (split them):")
            for n, name, x in sorted(longs, reverse=True):
                print(f"    {n} words, {name}: {x}")
        if avoid_hits:
            print("  Words to replace:")
            for h in avoid_hits:
                print("    " + h)
        if unknown:
            print("  Abbreviations not in the glossary: " + ", ".join(f"{a} ({', '.join(sorted(p))})" for a, p in sorted(unknown.items())))
        if no_example:
            print("  Rules without an example: " + ", ".join(no_example))
        problems += len(no_example) + len(unknown)
    print()
    if strict and problems:
        sys.exit(f"{problems} problem(s) in --strict mode.")
    print("Report done. See WRITING-GUIDE.md for how to fix anything listed.")


if __name__ == "__main__":
    main()
