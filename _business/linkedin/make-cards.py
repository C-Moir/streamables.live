#!/usr/bin/env python3
"""Generate branded LinkedIn card images (1200x627) for every article.

Self-made cards: no stock photos, no licensing risk. Style matches the
streamables.live aesthetic (dark, cyan mono accents).

Usage: python3 make-cards.py [chromium_binary]
Output: images/NN.png for every articles/NN-*.html in the repo.
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
ARTICLES = os.path.join(REPO, "articles")
OUT = os.path.join(HERE, "images")

SERIES = {
    **{n: "CONSULTING &amp; OPERATIONS" for n in
       ["00", "01", "02", "03", "09", "16", "17", "20", "25", "26"]},
    **{n: "CLIPTIPS BUILD LOG" for n in ["28", "29", "31", "32", "33", "34", "35"]},
    "30": "FIELD GUIDE",
}

TPL = """<!doctype html><html><head><meta charset="utf-8"><style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html {{ background:#000; height:100%; }}
  body {{ width:1200px; height:620px; overflow:hidden;
    font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
    background:radial-gradient(circle at 15% 25%, rgba(0,255,255,.10) 0, transparent 45%),
               radial-gradient(circle at 85% 80%, rgba(0,229,255,.08) 0, transparent 45%),
               linear-gradient(135deg,#0a0a0f 0,#000 100%);
    color:#fff; display:flex; flex-direction:column; justify-content:space-between;
    padding:64px 72px; border:1px solid rgba(0,255,255,.18); }}
  .tag {{ font-family:'DejaVu Sans Mono',monospace; font-size:20px; letter-spacing:.18em;
    color:rgba(0,255,255,.75); }}
  h1 {{ font-size:{size}px; line-height:1.14; font-weight:800; letter-spacing:-.01em;
    max-width:1010px; text-wrap:balance; }}
  .sub {{ font-size:{subsize}px; line-height:1.3; font-weight:600; margin-top:18px;
    color:rgba(0,229,255,.85); max-width:940px; text-wrap:balance; }}
  .rule {{ width:96px; height:3px; background:#00e5ff; margin-top:28px; }}
  .foot {{ display:flex; justify-content:space-between; align-items:baseline;
    font-family:'DejaVu Sans Mono',monospace; font-size:22px; color:rgba(255,255,255,.55); }}
  .foot b {{ color:rgba(0,255,255,.9); font-weight:600; }}
</style></head><body>
  <div class="tag">// {series}</div>
  <div><h1>{title}</h1>{sub}<div class="rule"></div></div>
  <div class="foot"><span><b>streamables.live</b> · Cameron J. Moir</span><span>Brisbane, AU</span></div>
</body></html>"""


def find_chromium():
    if len(sys.argv) > 1:
        return sys.argv[1]
    # headless_shell renders the viewport exactly; full chromium loses ~87px to UI
    base = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    for root, _dirs, files in os.walk(base):
        for f in files:
            if f in ("headless_shell", "chrome") and os.access(os.path.join(root, f), os.X_OK):
                return os.path.join(root, f)
    for c in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        p = shutil.which(c)
        if p:
            return p
    sys.exit("No chromium binary found; pass one as argv[1]")


def glue_orphan(text):
    """Join the last two words with a non-breaking space so no line ends
    with a single orphan word."""
    words = text.rsplit(" ", 1)
    return " ".join(words) if len(words) == 2 else text


def split_title(title):
    """Two-part titles become headline + subline for impact.

    'X. Y.'  -> X. / Y.      'X: Y' -> X / Y      'X (Y)' -> X / Y
    """
    m = re.match(r"^(.{12,}?[.!?])\s+(.{8,})$", title)
    if m:
        return m.group(1), m.group(2)
    m = re.match(r"^(.{12,}?):\s+(.{8,})$", title)
    if m:
        return m.group(1), m.group(2)
    m = re.match(r"^(.{12,}?)\s+\((.{8,})\)$", title)
    if m:
        return m.group(1), m.group(2)
    return title, None


def main():
    os.makedirs(OUT, exist_ok=True)
    chromium = find_chromium()
    made = 0
    for f in sorted(os.listdir(ARTICLES)):
        m = re.match(r"^(\d\d)-.*\.html$", f)
        if not m:
            continue
        num = m.group(1)
        raw = open(os.path.join(ARTICLES, f), encoding="utf-8", errors="replace").read()
        t = re.search(r"<title>(.*?)</title>", raw, re.S)
        title = html.unescape(t.group(1)).split("|")[0].strip() if t else f
        main_line, sub_line = split_title(title)
        size = 76 if len(main_line) <= 34 else (66 if len(main_line) <= 48 else 56)
        sub_html = ""
        if sub_line:
            sub_html = '<div class="sub">{}</div>'.format(
                html.escape(glue_orphan(sub_line)))
        page = TPL.format(series=SERIES.get(num, "IDEAS &amp; RESEARCH"),
                          title=html.escape(glue_orphan(main_line)),
                          size=size, subsize=max(30, size // 2), sub=sub_html)
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as tmp:
            tmp.write(page)
            src = tmp.name
        dst = os.path.join(OUT, f"{num}.png")
        subprocess.run(
            [chromium, "--headless", "--no-sandbox", "--disable-gpu",
             "--hide-scrollbars", "--force-device-scale-factor=1",
             f"--screenshot={dst}", "--window-size=1200,627", f"file://{src}"],
            check=True, capture_output=True)
        os.unlink(src)
        made += 1
        print(f"{dst}  ({title[:60]})")
    print(f"\n{made} cards written to {OUT}")


if __name__ == "__main__":
    main()
