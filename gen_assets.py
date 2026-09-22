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
    "ACC &#8212; a 20% profit miss moved the stock more than a 68% miss did",
    "Situational Awareness &#8212; put-linked exposure fell from 62% of gross to 0.03%",
    "Olist &#8212; 55% of won sellers never sold a single item",
    "Bank LCR &#8212; the lower ratio sits on the more retail-anchored funding base",
    "Campaign ROI &#8212; Display clears break-even at no level of spend",
    "Indirect Tax &#8212; 33.3% exceptions caught, matching the injected rate exactly",
    "Retail Media &#8212; one marketplace of three discloses the number that matters",
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
    "tableau": '<rect x="10.5" y="2" width="3" height="20" fill="{c}"/>'
               '<rect x="2" y="10.5" width="20" height="3" fill="{c}"/>',
    "matplotlib": '<path d="M3 3v18h18" fill="none" stroke="{c}" stroke-width="1.6" '
                  'stroke-linecap="round"/>'
                  '<path d="M6 17l4-6 4 3 5-9" fill="none" stroke="{c}" stroke-width="1.7" '
                  'stroke-linecap="round" stroke-linejoin="round"/>',
    "vba": '<path d="M9 3c-2.5 0-2.5 2.6-2.5 4.5S6.5 12 4 12c2.5 0 2.5 2.6 2.5 4.5S6.5 21 9 21" '
           'fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>'
           '<path d="M15 3c2.5 0 2.5 2.6 2.5 4.5S17.5 12 20 12c-2.5 0-2.5 2.6-2.5 4.5S17.5 21 15 21" '
           'fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>',
    "powerpoint": '<rect x="2.5" y="3.5" width="19" height="13" rx="1.2" fill="none" '
                  'stroke="{c}" stroke-width="1.6"/>'
                  '<path d="M12 16.5V20M8.5 20h7" stroke="{c}" stroke-width="1.5" '
                  'stroke-linecap="round"/>'
                  '<rect x="6" y="10" width="2.6" height="4" fill="{c}"/>'
                  '<rect x="10.7" y="7.5" width="2.6" height="6.5" fill="{c}"/>'
                  '<rect x="15.4" y="9" width="2.6" height="5" fill="{c}"/>',
    "xgboost": '<circle cx="12" cy="4" r="2.3" fill="{c}"/>'
               '<circle cx="6" cy="12" r="2.3" fill="{c}"/>'
               '<circle cx="18" cy="12" r="2.3" fill="{c}"/>'
               '<circle cx="3.5" cy="20" r="2.3" fill="{c}"/>'
               '<circle cx="9.5" cy="20" r="2.3" fill="{c}"/>'
               '<path d="M10.6 5.9L7.4 10.1M13.4 5.9l3.2 4.2M4.9 14.1L4.1 17.7M7.1 14.1l1.8 3.6" '
               'stroke="{c}" stroke-width="1.4" stroke-linecap="round"/>',
    "shap": '<rect x="11.4" y="2.5" width="1.3" height="19" fill="{c}"/>'
            '<rect x="3.5" y="4.6" width="7.9" height="2.7" rx="0.6" fill="{c}"/>'
            '<rect x="12.7" y="8.6" width="7.3" height="2.7" rx="0.6" fill="{c}"/>'
            '<rect x="5.8" y="12.6" width="5.6" height="2.7" rx="0.6" fill="{c}"/>'
            '<rect x="12.7" y="16.6" width="4.6" height="2.7" rx="0.6" fill="{c}"/>',
}

TOOLS = [
    ("excel", "Excel", None), ("python", "Python", "python"),
    ("pandas", "pandas", "pandas"), ("numpy", "NumPy", "numpy"),
    ("scipy", "SciPy", "scipy"), ("statsmodels", "statsmodels", None),
    ("r", "R", "r"), ("stata", "Stata", None),
    ("scikitlearn", "scikit-learn", "scikitlearn"), ("xgboost", "XGBoost", None),
    ("shap", "SHAP", None), ("pytorch", "PyTorch", "pytorch"),
    ("postgresql", "SQL", "postgresql"), ("powerbi", "Power BI", None),
    ("tableau", "Tableau", None), ("latex", "LaTeX", "latex"),
    ("vba", "VBA", None), ("powerpoint", "PowerPoint", None),
]


def header(t):
    """Name, an animated findings ticker, and the disciplines strip."""
    n = len(TICKER)
    dur = n * 4
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


# (tag, title, headline, sub, methods, index label)
#
# The index label is what the reader scans; the rest is what the spotlight
# shows when it reaches that row. Both come from the same tuple so the list
# and the panel cannot drift apart.
CARDS = [
    ("ZEPTO", "Pre-IPO Valuation",
     "$3.8bn base case", "against a $7.0bn private mark",
     "relative valuation &#183; unit economics",
     "Zepto &#8212; Pre-IPO Valuation"),
    ("SUN PHARMA / ORGANON", "Merger Arbitrage",
     "Pass on the spread", "93.9% implied completion, 0.07% expected",
     "event study &#183; GARCH &#183; Monte Carlo",
     "Sun Pharma / Organon &#8212; Merger Arbitrage"),
    ("PAYPAL", "Fairness Valuation",
     "$60.50 below the floor", "of all three methods",
     "DCF &#183; comps &#183; precedents",
     "PayPal &#8212; Fairness Valuation"),
    ("ACC LIMITED", "Dividend Event Study",
     "Smaller miss, bigger move", "-5.7% CAR on a 20% miss vs +0.2% on a 68% miss",
     "event study &#183; market model &#183; Fama-French",
     "ACC Limited &#8212; Dividend Event Study"),
    ("SITUATIONAL AWARENESS", "Forced-Deleveraging Forensics",
     "62% of gross to 0.03%", "put-linked exposure, the quarter before the collapse",
     "13F reconstruction &#183; liquidity &#183; attribution",
     "Situational Awareness &#8212; Unwind Forensics"),
    ("OLIST MARKETPLACE", "Unit Economics &amp; Cross-Sell",
     "55% of won sellers never sold", "a single item. Winning is not activating.",
     "cohort LTV &#183; funnel &#183; propensity",
     "Olist &#8212; Unit Economics &amp; LTV"),
    ("HDFC / INDUSIND", "Bank LCR &amp; Funding Concentration",
     "Lower ratio, better funding", "126.66% LCR on 40.9% wholesale against 115.00% on 33.1%",
     "Basel III &#183; reconciliation &#183; funding mix",
     "Bank LCR &amp; Funding Concentration"),
    ("CAMPAIGN ROI", "Media Spend Simulator",
     "Display has no break-even", "0.94x incremental ROAS against Shopping's 4.29x",
     "funnel modelling &#183; break-even &#183; sensitivity",
     "Campaign ROI &amp; Media Spend Simulator"),
    ("INDIRECT TAX", "Classification &amp; Reconciliation",
     "33.3% caught, 33.3% injected", "20 sourced rules across 11 jurisdictions",
     "GST &#183; VAT &#183; sales &amp; use tax &#183; rules engine",
     "Indirect Tax Classification Engine"),
    ("RETAIL MEDIA INDIA", "Monetization Benchmark",
     "One of three discloses it", "the other two disclose ad spend, its mirror image",
     "public-disclosure benchmarking",
     "Retail Media Benchmark, India"),
]


def showcase(t):
    """A spotlight panel that cycles the work, beside an index of all of it.

    A grid that shows every project at once stops scaling somewhere around
    six: ten cards at a readable type size is a wall roughly five times the
    height of the text it sits above, and a reader has to get past all of it
    to reach the writing. Ten cards narrow enough to fit in fewer rows clip
    their own headlines instead.

    So the two jobs are split. The panel on the left holds one project at a
    time and rotates, which is where the motion and the detail go. The column
    on the right lists every project permanently, with the current one marked,
    which is where completeness goes - a reader who never waits for a full
    cycle can still see the whole body of work and count it. The index label
    and the panel content come from the same tuple, so the list can never
    fall out of step with what the panel is showing."""
    n = len(CARDS)
    pad, row_h, gap = 22, 21, 16
    left_w = 610
    rule_x = left_w + gap
    idx_x = rule_x + gap
    H = max(236, n * row_h + 2 * pad)
    dur = n * 4
    step = 100 / n

    css = []
    for i in range(n):
        s = i * step
        hold_in, hold_out, fade_out = s + 1.2, s + step - 2.4, s + step - 1.2
        css.append(f".p{i}{{animation:p{i} {dur}s infinite}}"
                   f".r{i}{{animation:r{i} {dur}s infinite}}"
                   f".m{i}{{animation:p{i} {dur}s infinite}}")
        # the spotlight panel and its row marker share one opacity curve
        css.append(f"@keyframes p{i}{{0%,{s+0.1:.2f}%{{opacity:0}}"
                   f"{hold_in:.2f}%,{hold_out:.2f}%{{opacity:1}}"
                   f"{fade_out:.2f}%,100%{{opacity:0}}}}")
        # the index row itself never disappears - it only takes the accent
        css.append(f"@keyframes r{i}{{0%,{s+0.1:.2f}%{{fill:{t['mute']}}}"
                   f"{hold_in:.2f}%,{hold_out:.2f}%{{fill:{t['ink']}}}"
                   f"{fade_out:.2f}%,100%{{fill:{t['mute']}}}}}")

    body = [f'<rect x="0.5" y="0.5" width="{left_w-1}" height="{H-1}" rx="7" '
            f'fill="{t["card"]}" stroke="{t["cardline"]}" stroke-width="1.5"/>',
            f'<rect x="{rule_x}" y="{pad}" width="1" height="{H-2*pad}" '
            f'fill="{t["cardline"]}"/>']

    for i, (tag, title, head, sub, meth, label) in enumerate(CARDS):
        body.append(
            f'<g class="p{i}" opacity="0">'
            f'<text x="{pad}" y="40" font-size="10.5" letter-spacing="1.6" '
            f'fill="{t["accent"]}">{tag}</text>'
            f'<text x="{pad}" y="64" font-size="15" font-weight="600" '
            f'fill="{t["ink"]}">{title}</text>'
            f'<text x="{pad}" y="114" font-size="21" font-weight="600" '
            f'fill="{t["ink"]}">{head}</text>'
            f'<text x="{pad}" y="138" font-size="12" fill="{t["mute"]}">{sub}</text>'
            f'<rect x="{pad}" y="158" width="34" height="1.5" fill="{t["accent"]}"/>'
            f'<text x="{pad}" y="182" font-size="10.5" fill="{t["mute"]}">{meth}</text>'
            f'<text x="{pad}" y="{H-20}" font-size="10.5" letter-spacing="1.2" '
            f'fill="{t["mute"]}">{i+1:02d} / {n:02d}</text>'
            f'</g>')
        ry = pad + i * row_h
        body.append(
            f'<rect class="m{i}" x="{idx_x}" y="{ry+2}" width="2" height="13" '
            f'rx="1" fill="{t["accent"]}" opacity="0"/>'
            f'<text class="r{i}" x="{idx_x+12}" y="{ry+13}" font-size="10.5" '
            f'fill="{t["mute"]}">{label}</text>')

    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" role="img" aria-label="Selected work">'
            f'<style>{"".join(css)}</style>'
            f'<g font-family="{MONO}">' + "".join(body) + "</g></svg>\n")


def section(t, title):
    tw = len(title) * 8.6
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="34" viewBox="0 0 {W} 34" role="img" aria-label="{title}">
  <g font-family="{MONO}">
    <text x="0" y="20" font-size="12" letter-spacing="2.2" fill="{t['mute']}">{title.upper()}</text>
    <rect x="{tw + 18}" y="15" width="{W - tw - 18}" height="1" fill="{t['rule']}"/>
  </g>
</svg>
"""


SECTIONS = [("Selected work", "s-work"), ("How it's built", "s-method"),
            ("Next", "s-next"), ("Activity", "s-activity")]

for name, theme in THEMES.items():
    out = ROOT / "assets" / ("dark" if name == "dark" else "")
    out.mkdir(parents=True, exist_ok=True)
    (out / "header.svg").write_text(header(theme))
    if (ROOT / ".icons").is_dir():
        (out / "toolkit.svg").write_text(toolkit(theme))
    (out / "showcase.svg").write_text(showcase(theme))
    for title, slug in SECTIONS:
        (out / f"{slug}.svg").write_text(section(theme, title))
print("wrote", len(list((ROOT / "assets").rglob("*.svg"))), "svg files")
