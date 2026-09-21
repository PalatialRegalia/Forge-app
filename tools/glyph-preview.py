#!/usr/bin/env python3
"""Generate a glyph contact sheet from index.html.

No dependencies, no build step. Reads the GLYPHS and GLYPH_LABELS objects
straight out of index.html, so there is exactly one source of truth for the icon
set, and writes tools/glyph-preview.html - open that in any browser to see every
glyph at the sizes the app actually uses.

    python3 tools/glyph-preview.py

Use this after editing or adding a glyph: it catches ids that no longer resolve
and shows whether a shape still reads at 16px.
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIZES = (16, 24, 32)

TEMPLATE = """<!DOCTYPE html>
<meta charset="utf-8">
<title>Forge Kinetic - glyph set</title>
<style>
  body { background:#0a0a0a; color:#f4f4f5; margin:0; padding:32px;
         font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
  h1 { font-size:1rem; letter-spacing:1px; text-transform:uppercase; margin:0 0 4px; }
  p  { color:#b4b4bd; font-size:.85rem; margin:0 0 24px; }
  table { border-collapse:collapse; width:100%%; max-width:760px; }
  td { border-bottom:1px solid #2f2f34; padding:10px 0; vertical-align:middle; }
  .name { width:190px; font-size:.9rem; }
  .name small { display:block; color:#b4b4bd; font-size:.75rem; }
  .row { display:flex; gap:28px; align-items:center; }
  .cell { display:inline-flex; color:#f4f4f5; }
  .cell svg { width:100%%; height:100%%; }
</style>
<h1>Forge Kinetic - glyph set</h1>
<p>%d glyphs, drawn on a 24x24 grid with a 2px stroke and currentColor, shown at %s px.</p>
<table>%s</table>
"""


def extract(source):
    """Pull the glyph registry out of the app's inline script."""
    def obj(name):
        m = re.search(r"const %s = \{(.*?)\n        \};" % name, source, re.S)
        if not m:
            sys.exit("could not find %s in index.html" % name)
        return dict(re.findall(r"(\w+):\s*'([^']*)'", m.group(1)))

    return obj("GLYPHS"), obj("GLYPH_LABELS")


def main():
    with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as fh:
        source = fh.read()

    glyphs, labels = extract(source)
    print("found %d glyphs" % len(glyphs))

    rows = []
    for gid, body in glyphs.items():
        label = labels.get(gid, "MISSING LABEL")
        cells = "".join(
            '<span class="cell" style="width:%dpx;height:%dpx">'
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="%s">%s</svg>'
            "</span>" % (size, size, html.escape(label), body)
            for size in SIZES
        )
        rows.append(
            '<tr><td class="name">%s<small>%s</small></td><td class="row">%s</td></tr>'
            % (html.escape(gid), html.escape(label), cells)
        )

    dest = os.path.join(ROOT, "tools", "glyph-preview.html")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(TEMPLATE % (len(glyphs), "/".join(str(s) for s in SIZES), "".join(rows)))
    print("wrote %s" % dest)


if __name__ == "__main__":
    main()
