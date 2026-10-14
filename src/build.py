"""Build the SistemSehat website from the sources in src/.

    python3 src/build.py

Writes the English pages to docs/, the Indonesian pages to docs/id/, and the dossier
templates to drafts/. docs/ is rebuilt from scratch every time, so never edit it by hand:
change the files in src/ and run this again. Python 3.9 or newer; nothing to install.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import engine  # noqa: E402
from engine import DOCS, SRC, VERSIONS, short_hash  # noqa: E402


def main():
    # start clean, so a page removed from the sources disappears from the site
    if DOCS.exists():
        shutil.rmtree(DOCS)
    shutil.copytree(SRC / "assets", DOCS / "assets")
    # hand-written pages (for example a dossier made from a template in drafts/) are copied as they are
    if (SRC / "static").exists():
        shutil.copytree(SRC / "static", DOCS, dirs_exist_ok=True)
    for name in ("style.css", "site.js"):
        VERSIONS[name] = short_hash((DOCS / "assets" / name).read_bytes())

    import content_en
    pages_en, index_en, rules_en = engine.write_language(content_en)
    engine.write_404()  # uses the English shell; the page itself is bilingual
    paths = [p[0] for p in content_en.PAGES]

    import content_id
    pages_id, index_id, rules_id = engine.write_language(content_id)

    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    has_sitemap = engine.write_sitemap(paths)

    print(f"English:    {pages_en} pages, {rules_en} rules, {index_en} search entries")
    print(f"Indonesian: {pages_id} pages, {rules_id} rules, {index_id} search entries")
    print(f"Written to {DOCS}")
    if not has_sitemap:
        print("Note: SITE_URL in src/config.py is empty, so search-engine language links, link previews "
              "and the sitemap were left out. Set it once you know the site's address.")
    if rules_en != rules_id:
        sys.exit(f"Error: English has {rules_en} rules but Indonesian has {rules_id}. Each rule needs both languages.")


if __name__ == "__main__":
    main()
