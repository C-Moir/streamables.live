#!/usr/bin/env python3
"""Generate LinkedIn card images (1200x627) matching the existing article-26
card design: mono type, white/cyan split headline, topic chip, node graph,
byline footer.

Usage: python3 make-cards.py [chromium_binary]
Output: images/NN.png for every articles/NN-*.html in the repo.
"""
import html
import math
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
ARTICLES = os.path.join(REPO, "articles")
OUT = os.path.join(HERE, "images")

CONSULTING = ["00", "01", "02", "03", "09", "16", "17", "20", "25", "26"]
BUILDLOG = ["28", "29", "31", "32", "33", "34", "35"]

SERIES = {}
SERIES.update({n: ("HOSPITALITY &amp; OPS", "FIELD NOTES") for n in CONSULTING})
SERIES.update({n: ("CLIPTIPS", "BUILD LOG") for n in BUILDLOG})
SERIES["26"] = ("SOVEREIGN AI", "FIELD NOTES")  # match the published card
SERIES["30"] = ("AI LITERACY", "FIELD GUIDE")

CHIP = {
    "00": "AI BASICS", "01": "REAL COSTS", "02": "FAILURE MODES",
    "03": "DATA VALUE", "04": "DATA ETHICS", "05": "ACCOUNTABILITY",
    "06": "REPUTATION", "07": "AUTONOMY", "08": "DATA RIGHTS",
    "09": "STRATEGY", "10": "TRUST SYSTEMS", "11": "MULTI-AGENT",
    "12": "OWNERSHIP", "13": "ON-CHAIN TRUST", "14": "KNOWLEDGE ECONOMY",
    "15": "ARCHITECTURE", "16": "KITCHEN SYSTEMS", "17": "OPERATIONS",
    "18": "CREATOR ECONOMY", "19": "AI ETHICS", "20": "OPERATIONAL DATA",
    "21": "IDENTITY", "22": "DATA DIVIDEND", "23": "REAL-WORLD ANCHORING",
    "24": "BEHAVIOUR CHANGE", "25": "REPORTING", "26": "PERSONAL INFRASTRUCTURE",
    "27": "AGENT STANDING", "28": "SOLO BUILD", "29": "SHIPPED",
    "30": "SPOTTING AI", "31": "LATENCY", "32": "UNIT ECONOMICS",
    "33": "ZERO BUDGET", "34": "PROVIDER PATTERN", "35": "HONEST LOGS",
}

# Per-card adjustments. Any key can be set for any article number:
#   white / cyan  - custom headline split (cyan renders on its own line, in cyan)
#   chip          - overrides CHIP
#   cat           - overrides SERIES, as ("LEFT PART", "CYAN PART")
#   desc          - overrides the meta-description subline
# Add or edit entries, rerun make-cards.py, done.
OVERRIDES = {
    "02": {"white": "Why Most AI Projects Fail", "cyan": "in Year One"},
    "20": {"white": "Hospitality Is a Data Goldmine", "cyan": "Nobody's Mining"},
    "22": {"white": "Universal Basic Income", "cyan": "Funded by Data, Not Taxes"},
    "28": {"white": "How I Built ClipTips", "cyan": "with Claude Code"},
    "32": {"white": "What I Actually Paid in 2026", "cyan": "to Run a Live Interpreter"},
    "33": {"white": "Building V1.5 for $0", "cyan": "While Waiting for Budget"},
    "35": {"white": "Mistakes,", "cyan": "Captured Honestly"},
}

TPL = """<!doctype html><html><head><meta charset="utf-8"><style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html {{ background:#000; height:100%; }}
  body {{ width:1200px; height:620px; overflow:hidden; position:relative;
    font-family:'DejaVu Sans Mono',monospace; color:#fff;
    background:
      radial-gradient(circle at 82% 45%, rgba(0,229,255,.10) 0, transparent 40%),
      linear-gradient(rgba(0,255,255,.028) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,255,255,.028) 1px, transparent 1px),
      linear-gradient(150deg,#07100f 0,#020606 55%,#03110f 100%);
    background-size:auto, 46px 46px, 46px 46px, auto; }}
  .top {{ display:flex; justify-content:space-between; align-items:center;
    padding:34px 56px 22px; }}
  .wordmark {{ font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;
    font-size:30px; font-weight:700; letter-spacing:.01em; }}
  .wordmark .slash {{ color:#00e5ff; font-weight:800; }}
  .cat {{ font-size:17px; letter-spacing:.28em; color:rgba(160,190,190,.85); }}
  .cat b {{ color:#00e5ff; font-weight:700; }}
  .hr {{ height:1px; background:rgba(0,255,255,.16); margin:0 56px; }}
  .main {{ position:absolute; top:118px; bottom:80px; left:56px; width:640px;
    display:flex; flex-direction:column; justify-content:center; }}
  .chip {{ display:inline-block; align-self:flex-start; border:1px solid rgba(0,229,255,.55);
    border-radius:4px; padding:7px 14px; font-size:15px; letter-spacing:.26em;
    color:#7fe8f2; margin-bottom:26px; background:rgba(0,229,255,.05); }}
  h1 {{ font-family:'DejaVu Sans Mono',monospace; font-size:{size}px; line-height:1.18;
    font-weight:800; letter-spacing:-.01em; text-wrap:balance; }}
  h1 .cy {{ color:#00e5ff; }}
  .desc {{ margin-top:22px; font-size:18px; line-height:1.55; color:rgba(160,185,185,.9);
    max-width:560px; }}
  .graph {{ position:absolute; right:30px; top:110px; }}
  .foot {{ position:absolute; left:0; right:0; bottom:0; height:62px;
    border-top:1px solid rgba(0,255,255,.14); display:flex; align-items:center;
    justify-content:space-between; padding:0 56px; font-size:15px;
    letter-spacing:.22em; color:rgba(150,175,175,.8); }}
  .foot b {{ color:#fff; font-weight:700; }}
</style></head><body>
  <div class="top">
    <div class="wordmark"><span class="slash">S</span>treamables.live</div>
    <div class="cat">{cat1} · <b>{cat2}</b></div>
  </div>
  <div class="hr"></div>
  <div class="main">
    <span class="chip">{chip}</span>
    <h1>{title}</h1>
    <div class="desc">{desc}</div>
  </div>
  {graph}
  <div class="foot">
    <span>BY <b>CAMERON J. MOIR</b> · BRISBANE</span>
    <span>ARTICLE {num} · 2026</span>
  </div>
</body></html>"""


def node_graph(seed, w=380, h=380):
    rng = random.Random(seed)
    cx, cy = w * 0.55, h * 0.5
    parts = [f'<circle cx="{cx}" cy="{cy}" r="{w*0.36:.0f}" fill="none" '
             'stroke="rgba(0,229,255,.14)" stroke-width="1"/>']
    nodes = []
    n = 8
    for i in range(n):
        a = (2 * math.pi * i / n) + rng.uniform(-0.25, 0.25)
        r = w * rng.uniform(0.30, 0.44)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        nodes.append((x, y))
    for x, y in nodes:
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" '
                     'stroke="rgba(0,229,255,.35)" stroke-width="1"/>')
    for i in range(n):
        if rng.random() < 0.5:
            x1, y1 = nodes[i]
            x2, y2 = nodes[(i + 1) % n]
            parts.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
                         'stroke="rgba(0,229,255,.18)" stroke-width="1"/>')
    for x, y in nodes:
        rr = rng.uniform(4, 7)
        parts.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rr:.1f}" fill="#0dd6e8"/>')
        parts.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rr*2.2:.1f}" '
                     'fill="rgba(0,229,255,.12)"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="rgba(0,229,255,.25)"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="14" fill="#19e6f5"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="#eafffe"/>')
    return (f'<svg class="graph" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">' + "".join(parts) + "</svg>")


def glue_orphan(text):
    words = text.rsplit(" ", 1)
    return "&nbsp;".join(html.escape(w) for w in words) if len(words) == 2 else html.escape(text)


def split_title(title):
    """'X. Y.' -> white X. / cyan Y.   Also ':' and '(...)' variants."""
    for pat in (r"^(.{12,}?[.!?])\s+(.{8,})$",
                r"^(.{12,}?):\s+(.{8,})$",
                r"^(.{12,}?)\s+\((.{8,})\)$"):
        m = re.match(pat, title)
        if m:
            return m.group(1), m.group(2)
    return title, None


def find_chromium():
    if len(sys.argv) > 1:
        return sys.argv[1]
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
        d = re.search(r'name="description" content="([^"]*)"', raw)
        desc = html.unescape(d.group(1)) if d else ""
        ov = OVERRIDES.get(num, {})
        desc = ov.get("desc", desc)
        if len(desc) > 210:
            desc = desc[:207].rsplit(" ", 1)[0] + "…"
        if "white" in ov:
            white, cyan = ov["white"], ov.get("cyan")
        else:
            white, cyan = split_title(title)
        longest = max(len(white), len(cyan or ""))
        size = 52 if longest <= 34 else (44 if longest <= 48 else 38)
        h1 = glue_orphan(white)
        if cyan:
            h1 += '<br><span class="cy">' + glue_orphan(cyan) + "</span>"
        cat1, cat2 = ov.get("cat", SERIES.get(num, ("SOVEREIGN AI", "FIELD NOTES")))
        page = TPL.format(cat1=cat1, cat2=cat2,
                          chip=ov.get("chip", CHIP.get(num, "FIELD NOTES")),
                          title=h1, size=size,
                          desc=html.escape(desc),
                          graph=node_graph(int(num)), num=num)
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
    print(f"{made} cards written to {OUT}")


if __name__ == "__main__":
    main()
