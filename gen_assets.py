"""
Generate the profile's SVG assets, light and dark.

Monospace throughout: it reads as a working document rather than a brochure,
which is the register the analysis itself is written in.

Motion: the header carries a ticker that cycles the three headline findings.
The technique is the one record-rotate uses - an animated SVG - but the file is
committed here rather than fetched from a worker, so no outside service can take
the page down or watch who loads it. A ticker is also the one form of motion
that belongs on this profile: it is what the subject matter actually looks like.

Tool marks: seven are real vendor logos (simple-icons, monochrome). Excel, Power
BI, Stata and statsmodels have no logo in any icon set - Microsoft's marks were
withdrawn on trademark grounds and Stata was never included - so they get drawn
marks at the same weight and size.
"""
import pathlib
import re

MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"
ROOT = pathlib.Path(__file__).parent
W = 1000

THEMES = {
    "light": dict(ink="#0f172a", mute="#5b6b7f", rule="#d7dee7", accent="#4b2e83",
                  card="#ffffff", cardline="#dde3ea"),
    "dark":  dict(ink="#e6edf3", mute="#8b98a5", rule="#2a3441", accent="#b39ddb",
                  card="#0d1117", cardline="#242c36"),
}

# The disciplines, named as work rather than as job titles. Between them these
# cover valuation, M&A, banking, strategy/consulting, operating analysis and
# economics without the page ever asking for a job.
DISCIPLINES = ["FINANCE", "VALUATION", "M&amp;A", "CAPITAL MARKETS",
               "STRATEGY", "OPERATIONS", "BUSINESS ANALYSIS", "ECONOMICS"]
DISC_COLS = 4

TICKER = [
    "Zepto &#8212; $3.8bn base case against a $7.0bn private mark",
    "Sun Pharma / Organon &#8212; pass on the spread at 93.9% implied completion",
    "PayPal &#8212; $60.50 below the floor of all three methods",
]


def logo_path(slug):
    m = re.search(r'\sd="([^"]+)"', (ROOT / ".icons" / f"{slug}.svg").read_text())
    return m.group(1)


DRAWN = {
    "excel": '<path d="M2 3h20v18H2z" fill="none" stroke="{c}" stroke-width="1.6"/>'
             '<path d="M2 9h20M2 15h20M9 3v18M16 3v18" stroke="{c}" stroke-width="1.2"/>',
    "powerbi": '<path d="M3 21h18" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>'
               '<rect x="4" y="13" width="4" height="6" fill="{c}"/>'
               '<rect x="10" y="8" width="4" height="11" fill="{c}"/>'
               '<rect x="16" y="3" width="4" height="16" fill="{c}"/>',
    "stata": '<path d="M3 19L21 6" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>'
             '<circle cx="6" cy="17" r="1.6" fill="{c}"/><circle cx="11" cy="15" r="1.6" fill="{c}"/>'
             '<circle cx="14" cy="10" r="1.6" fill="{c}"/><circle cx="19" cy="9" r="1.6" fill="{c}"/>',
    "statsmodels": '<path d="M2 19c5 0 4-13 10-13s5 13 10 13" fill="none" stroke="{c}" '
                   'stroke-width="1.6" stroke-linecap="round"/>'
                   '<path d="M12 6v13" stroke="{c}" stroke-width="1.1" stroke-dasharray="2 2"/>',
}

TOOLS = [
    ("excel", "Excel", None), ("python", "Python", "python"),
    ("pandas", "pandas", "pandas"), ("numpy", "NumPy", "numpy"),
    ("statsmodels", "statsmodels", None), ("r", "R", "r"),
    ("stata", "Stata", None), ("scikitlearn", "scikit-learn", "scikitlearn"),
    ("postgresql", "SQL", "postgresql"), ("powerbi", "Power BI", None),
    ("jupyter", "Jupyter", "jupyter"),
]


def header(t):
    """Name, an animated findings ticker, and the disciplines strip."""
    n = len(TICKER)
    dur = 15
    step = 100 / n
    # each line fades up, holds, fades out inside its own slot
    keys = ("0%,{a}%{{opacity:0}} {b}%,{c}%{{opacity:1}} {d}%,100%{{opacity:0}}")
    css = []
    for i in range(n):
        s = i * step
        css.append(f".t{i}{{animation:k{i} {dur}s infinite}}")
        css.append("@keyframes k" + str(i) + "{" + keys.format(
            a=round(s + 0.1, 2), b=round(s + 2, 2),
            c=round(s + step - 4, 2), d=round(s + step - 2, 2)) + "}")
    cellw = W / DISC_COLS
    rowh = 30
    top = 118
    cells = []
    for i, d in enumerate(DISCIPLINES):
        r, c = divmod(i, DISC_COLS)
        cx = c * cellw + cellw / 2
        ry = top + r * rowh
        cells.append(f'<text x="{cx:.1f}" y="{ry+20}" font-size="11.5" letter-spacing="1.7" '
                     f'fill="{t["mute"]}" text-anchor="middle">{d}</text>')
        if c:
            cells.append(f'<rect x="{c*cellw:.1f}" y="{ry+4}" width="1" height="22" '
                         f'fill="{t["cardline"]}"/>')
        if r:
            cells.append(f'<rect x="{c*cellw:.1f}" y="{ry}" width="{cellw:.1f}" height="1" '
                         f'fill="{t["cardline"]}"/>')
    ticker = "".join(
        f'<text class="t{i}" x="2" y="76" font-size="14" fill="{t["mute"]}" opacity="0">{s}</text>'
        for i, s in enumerate(TICKER))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="180" viewBox="0 0 {W} 180" role="img" aria-label="Shaswat Sharma">
  <style>{"".join(css)}</style>
  <g font-family="{MONO}">
    <text x="0" y="44" font-size="36" font-weight="600" letter-spacing="-0.6" fill="{t['ink']}">Shaswat Sharma</text>
    {ticker}
    <rect x="0" y="98" width="{W}" height="1" fill="{t['rule']}"/>
    <rect x="0" y="118" width="{W}" height="1" fill="{t['rule']}"/>
    {"".join(cells)}
    <rect x="0" y="178" width="{W}" height="1" fill="{t['rule']}"/>
  </g>
</svg>
"""


def toolkit(t):
    cols, tw, th = 6, W / 6, 112
    rows = (len(TOOLS) + cols - 1) // cols
    H = rows * th
    body = [f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" fill="{t["card"]}" '
            f'stroke="{t["cardline"]}" stroke-width="1"/>']
    for i, (key, label, slug) in enumerate(TOOLS):
        r, c = divmod(i, cols)
        rx, ry = c * tw, r * th
        gx, gy = rx + tw / 2, ry + 44
        mark = (f'<g transform="translate({gx-21:.1f},{gy-21:.1f}) scale(1.75)">'
                f'<path d="{logo_path(slug)}" fill="{t["accent"]}"/></g>' if slug else
                f'<g transform="translate({gx-21:.1f},{gy-21:.1f}) scale(1.75)">'
                f'{DRAWN[key].format(c=t["accent"])}</g>')
        body.append(mark)
        body.append(f'<text x="{gx:.1f}" y="{ry+86}" font-size="12.5" fill="{t["ink"]}" '
                    f'text-anchor="middle" font-family="{MONO}">{label}</text>')
        if c:
            body.append(f'<rect x="{rx:.1f}" y="{ry}" width="1" height="{th}" fill="{t["cardline"]}"/>')
        if r:
            body.append(f'<rect x="{rx:.1f}" y="{ry}" width="{tw:.1f}" height="1" fill="{t["cardline"]}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" role="img" aria-label="Toolkit">' + "".join(body) + "</svg>\n")


def section(t, title):
    tw = len(title) * 8.6
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="34" viewBox="0 0 {W} 34" role="img" aria-label="{title}">
  <g font-family="{MONO}">
    <text x="0" y="20" font-size="12" letter-spacing="2.2" fill="{t['mute']}">{title.upper()}</text>
    <rect x="{tw + 18}" y="15" width="{W - tw - 18}" height="1" fill="{t['rule']}"/>
  </g>
</svg>
"""


SECTIONS = [("Selected work", "s-work"), ("How it's built", "s-method"), ("Next", "s-next")]

for name, theme in THEMES.items():
    out = ROOT / "assets" / ("dark" if name == "dark" else "")
    out.mkdir(parents=True, exist_ok=True)
    (out / "header.svg").write_text(header(theme))
    (out / "toolkit.svg").write_text(toolkit(theme))
    for title, slug in SECTIONS:
        (out / f"{slug}.svg").write_text(section(theme, title))
print("wrote", len(list((ROOT / "assets").rglob("*.svg"))), "svg files")
