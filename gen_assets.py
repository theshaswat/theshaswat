"""
Generate the profile's SVG assets, light and dark.

Everything here is drawn from the same palette as the exhibit charts in the
three project repositories - the deep navy of a chart title, the indigo of the
base-case marker, the grey of an axis label. The header motif is a valuation
range with a base-case marker on it, which is literally the shape of the Zepto
result. Nothing is decorative for its own sake.

No third-party widgets, no remote images, no fonts to load: two committed SVGs
per asset, swapped by prefers-color-scheme, so the page renders identically
offline and cannot break when someone else's service goes down.
"""
import pathlib

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

THEMES = {
    "light": dict(ink="#0f172a", mute="#5b6b7f", rule="#d7dee7",
                  accent="#4b2e83", band="#cfc6e4"),
    "dark":  dict(ink="#e6edf3", mute="#8b98a5", rule="#2a3441",
                  accent="#b39ddb", band="#4a3f6b"),
}

W = 1000


def header(t):
    """Name, positioning line, and a valuation-range motif."""
    bx, bw, by = 622, 330, 108          # range band geometry
    mx = bx + bw * 0.34                 # base-case marker position
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="176" viewBox="0 0 {W} 176" role="img" aria-label="Shaswat Sharma">
  <g font-family="{FONT}">
    <text x="0" y="52" font-size="38" font-weight="600" letter-spacing="-0.4" fill="{t['ink']}">Shaswat Sharma</text>
    <text x="2" y="86" font-size="15.5" fill="{t['mute']}">Valuation and market-structure research on live transactions</text>
    <rect x="2" y="112" width="86" height="2.5" fill="{t['accent']}"/>
    <text x="2" y="146" font-size="12.5" letter-spacing="1.7" fill="{t['mute']}">PRE-IPO MARKS &#183; PENDING MERGERS &#183; CONTESTED BIDS</text>

    <rect x="{bx}" y="{by}" width="{bw}" height="9" rx="4.5" fill="{t['band']}"/>
    <path d="M {mx} {by-7} L {mx+11} {by+4.5} L {mx} {by+16} L {mx-11} {by+4.5} Z" fill="{t['accent']}"/>
    <text x="{bx}" y="{by-16}" font-size="10.5" letter-spacing="1.2" fill="{t['mute']}">BEAR</text>
    <text x="{mx}" y="{by-16}" font-size="10.5" letter-spacing="1.2" fill="{t['accent']}" text-anchor="middle">BASE</text>
    <text x="{bx+bw}" y="{by-16}" font-size="10.5" letter-spacing="1.2" fill="{t['mute']}" text-anchor="end">BULL</text>
    <text x="{bx+bw}" y="{by+34}" font-size="10.5" fill="{t['mute']}" text-anchor="end">an independent range, built before the market's was consulted</text>
  </g>
</svg>
"""


def section(t, num, title):
    """A numbered section rule."""
    tw = 26 + len(title) * 8.7
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="44" viewBox="0 0 {W} 44" role="img" aria-label="{num} {title}">
  <g font-family="{FONT}">
    <text x="0" y="26" font-size="12.5" font-weight="600" letter-spacing="1.4" fill="{t['accent']}">{num}</text>
    <text x="34" y="26" font-size="12.5" font-weight="600" letter-spacing="1.9" fill="{t['ink']}">{title.upper()}</text>
    <rect x="{tw + 22}" y="21" width="{W - tw - 24}" height="1" fill="{t['rule']}"/>
  </g>
</svg>
"""


ROOT = pathlib.Path(__file__).parent
for name, theme in THEMES.items():
    out = ROOT / "assets" / ("dark" if name == "dark" else "")
    out.mkdir(parents=True, exist_ok=True)
    (out / "header.svg").write_text(header(theme))
    for num, title, slug in [("01", "Selected work", "s-work"),
                             ("02", "Toolkit", "s-toolkit"),
                             ("03", "How the work is built", "s-method")]:
        (out / f"{slug}.svg").write_text(section(theme, num, title))
print("wrote", len(list((ROOT / "assets").rglob("*.svg"))), "svg files")
