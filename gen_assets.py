"""
Generate the profile's SVG assets, light and dark.

Palette is taken from the exhibit charts in the three project repositories - the
deep navy of a chart title, the indigo of the base-case marker, the grey of an
axis label. The header motif is a bear/base/bull range with a marker on it,
which is the literal shape of the Zepto result.

Tool marks: seven are real vendor logos (simple-icons, monochrome). Excel, Power
BI, Stata and statsmodels have no logo in any icon set - Microsoft's marks were
withdrawn on trademark grounds and Stata was never included - so they get drawn
marks at the same weight and size. A grid where four tiles are visibly missing
their glyph looks broken; a grid drawn to one standard looks deliberate.

No third-party widgets and no remote images: committed SVGs, swapped by
prefers-color-scheme, so the page cannot break when someone else's service does.
"""
import pathlib
import re

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
ROOT = pathlib.Path(__file__).parent
W = 1000

THEMES = {
    "light": dict(ink="#0f172a", mute="#5b6b7f", rule="#d7dee7", accent="#4b2e83",
                  band="#cfc6e4", card="#f4f6f9", cardline="#e3e8ee"),
    "dark":  dict(ink="#e6edf3", mute="#8b98a5", rule="#2a3441", accent="#b39ddb",
                  band="#4a3f6b", card="#161b22", cardline="#262d36"),
}


def logo_path(slug):
    """The 24x24 path from a cached simple-icons file."""
    m = re.search(r'\sd="([^"]+)"', (ROOT / ".icons" / f"{slug}.svg").read_text())
    return m.group(1)


# Marks drawn for the four tools with no logo anywhere. Each is built inside the
# same 24x24 box as the vendor logos so the grid stays on one visual standard.
DRAWN = {
    # spreadsheet: a grid of cells
    "excel": '<path d="M2 3h20v18H2z" fill="none" stroke="{c}" stroke-width="1.7"/>'
             '<path d="M2 9h20M2 15h20M9 3v18M16 3v18" stroke="{c}" stroke-width="1.3"/>',
    # report: ascending bars
    "powerbi": '<path d="M3 21h18" stroke="{c}" stroke-width="1.7" stroke-linecap="round"/>'
               '<rect x="4" y="13" width="4" height="6" fill="{c}"/>'
               '<rect x="10" y="8" width="4" height="11" fill="{c}"/>'
               '<rect x="16" y="3" width="4" height="16" fill="{c}"/>',
    # regression: a scatter with a fitted line
    "stata": '<path d="M3 19L21 6" stroke="{c}" stroke-width="1.7" stroke-linecap="round"/>'
             '<circle cx="6" cy="17" r="1.7" fill="{c}"/><circle cx="11" cy="15" r="1.7" fill="{c}"/>'
             '<circle cx="14" cy="10" r="1.7" fill="{c}"/><circle cx="19" cy="9" r="1.7" fill="{c}"/>',
    # inference: a distribution
    "statsmodels": '<path d="M2 19c5 0 4-13 10-13s5 13 10 13" fill="none" stroke="{c}" '
                   'stroke-width="1.7" stroke-linecap="round"/>'
                   '<path d="M12 6v13" stroke="{c}" stroke-width="1.2" stroke-dasharray="2 2"/>',
}

TOOLS = [
    ("excel",       "Excel",        None),
    ("python",      "Python",       "python"),
    ("pandas",      "pandas",       "pandas"),
    ("numpy",       "NumPy",        "numpy"),
    ("statsmodels", "statsmodels",  None),
    ("r",           "R",            "r"),
    ("stata",       "Stata",        None),
    ("scikitlearn", "scikit-learn", "scikitlearn"),
    ("postgresql",  "SQL",          "postgresql"),
    ("powerbi",     "Power BI",     None),
    ("jupyter",     "Jupyter",      "jupyter"),
]


def header(t):
    bx, bw, by = 622, 330, 108
    mx = bx + bw * 0.34
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="176" viewBox="0 0 {W} 176" role="img" aria-label="Shaswat Sharma">
  <g font-family="{FONT}">
    <text x="0" y="52" font-size="38" font-weight="600" letter-spacing="-0.4" fill="{t['ink']}">Shaswat Sharma</text>
    <text x="2" y="86" font-size="15.5" fill="{t['mute']}">Valuation, deal analysis and market structure &#8212; on transactions that are still live</text>
    <rect x="2" y="112" width="86" height="2.5" fill="{t['accent']}"/>
    <text x="2" y="146" font-size="12" letter-spacing="1.5" fill="{t['mute']}">PRE-IPO MARKS &#183; PENDING MERGERS &#183; CONTESTED BIDS &#183; UNIT ECONOMICS</text>

    <rect x="{bx}" y="{by}" width="{bw}" height="9" rx="4.5" fill="{t['band']}"/>
    <path d="M {mx} {by-7} L {mx+11} {by+4.5} L {mx} {by+16} L {mx-11} {by+4.5} Z" fill="{t['accent']}"/>
    <text x="{bx}" y="{by-16}" font-size="10.5" letter-spacing="1.2" fill="{t['mute']}">BEAR</text>
    <text x="{mx}" y="{by-16}" font-size="10.5" letter-spacing="1.2" fill="{t['accent']}" text-anchor="middle">BASE</text>
    <text x="{bx+bw}" y="{by-16}" font-size="10.5" letter-spacing="1.2" fill="{t['mute']}" text-anchor="end">BULL</text>
    <text x="{bx+bw}" y="{by+34}" font-size="10.5" fill="{t['mute']}" text-anchor="end">an independent range, built before the market&#8217;s was consulted</text>
  </g>
</svg>
"""


def toolkit(t):
    """One uniform grid of tool tiles. Deliberately the first thing after the name."""
    cols, tw, th, gap = 6, 160, 96, 6
    rows = (len(TOOLS) + cols - 1) // cols
    grid_w = cols * tw
    ox = (W - grid_w) / 2
    body = []
    for i, (key, label, slug) in enumerate(TOOLS):
        r, c = divmod(i, cols)
        in_row = min(cols, len(TOOLS) - r * cols)
        rx = ox + (grid_w - in_row * tw) / 2 + c * tw
        ry = r * th
        gx, gy = rx + tw / 2, ry + 26
        mark = (f'<g transform="translate({gx-14},{gy-14}) scale(1.17)">'
                f'<path d="{logo_path(slug)}" fill="{t["accent"]}"/></g>'
                if slug else
                f'<g transform="translate({gx-14},{gy-14}) scale(1.17)">'
                f'{DRAWN[key].format(c=t["accent"])}</g>')
        body.append(
            f'<rect x="{rx+gap/2:.1f}" y="{ry+gap/2:.1f}" width="{tw-gap}" height="{th-gap}" rx="7" '
            f'fill="{t["card"]}" stroke="{t["cardline"]}" stroke-width="1"/>'
            f'{mark}'
            f'<text x="{gx:.1f}" y="{ry+74}" font-size="12.5" fill="{t["ink"]}" '
            f'text-anchor="middle" font-family="{FONT}">{label}</text>')
    h = rows * th
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" '
            f'viewBox="0 0 {W} {h}" role="img" aria-label="Toolkit">'
            + "".join(body) + "</svg>\n")


def section(t, num, title):
    tw = 26 + len(title) * 8.7
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="44" viewBox="0 0 {W} 44" role="img" aria-label="{num} {title}">
  <g font-family="{FONT}">
    <text x="0" y="26" font-size="12.5" font-weight="600" letter-spacing="1.4" fill="{t['accent']}">{num}</text>
    <text x="34" y="26" font-size="12.5" font-weight="600" letter-spacing="1.9" fill="{t['ink']}">{title.upper()}</text>
    <rect x="{tw + 22}" y="21" width="{W - tw - 24}" height="1" fill="{t['rule']}"/>
  </g>
</svg>
"""


SECTIONS = [("01", "Selected work", "s-work"),
            ("02", "How the work is built", "s-method"),
            ("03", "Next", "s-next")]

for name, theme in THEMES.items():
    out = ROOT / "assets" / ("dark" if name == "dark" else "")
    out.mkdir(parents=True, exist_ok=True)
    (out / "header.svg").write_text(header(theme))
    (out / "toolkit.svg").write_text(toolkit(theme))
    for num, title, slug in SECTIONS:
        (out / f"{slug}.svg").write_text(section(theme, num, title))
print("wrote", len(list((ROOT / "assets").rglob("*.svg"))), "svg files")
