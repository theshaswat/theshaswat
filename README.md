<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/header.svg"/><img src="assets/header.svg" alt="Shaswat Sharma — valuation, m&a, capital markets, applied economics"/></picture>

<a href="mailto:shaswatsharma.work@gmail.com"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/EMAIL-0d1117?style=flat-square&logo=maildotru&logoColor=ffffff"/><img src="https://img.shields.io/badge/EMAIL-ffffff?style=flat-square&logo=maildotru&logoColor=0f172a" alt="Email"/></picture></a>
<a href="https://www.linkedin.com/in/shaswatsharma49"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/LINKEDIN-0d1117?style=flat-square&logo=linkedin&logoColor=ffffff"/><img src="https://img.shields.io/badge/LINKEDIN-ffffff?style=flat-square&logo=linkedin&logoColor=0f172a" alt="LinkedIn"/></picture></a>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/toolkit.svg"/><img src="assets/toolkit.svg" alt="Toolkit — Excel, Python, pandas, NumPy, statsmodels, R, Stata, scikit-learn, SQL, Power BI, Jupyter"/></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s-work.svg"/><img src="assets/s-work.svg" alt="Selected work"/></picture>

<table>
<tr>
<td colspan="2">
<h3><a href="https://github.com/theshaswat/zepto-pre-ipo-valuation">Zepto — Pre-IPO Valuation</a></h3>
<b>$3.8bn base case against a $7.0bn private mark.</b> Built before the roadshow range was consulted; the resulting $2.7–5.5bn range brackets what institutions actually indicated ($3.0–3.5bn domestic, $4.5bn foreign).
<br/><br/>
Zepto, Blinkit and Instamart disclose on three incompatible bases — 1P inventory against 3P commission — making headline revenue comparisons wrong by roughly 4.3x. Restated onto net order value, the binding constraint was never store density: Zepto runs the highest orders per store per day of the three (1,618) and the weakest basket (₹388, against ₹518 and ₹508).
<br/><br/>
<code>relative valuation</code> <code>unit economics</code> <code>scenario &amp; sensitivity</code> <code>fx decomposition</code> <code>Excel</code> <code>Python</code>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/theshaswat/sunpharma-organon-merger-arbitrage">Sun Pharma / Organon — Merger Arbitrage</a></h3>
<b>Pass on the spread.</b> Standalone DCF puts Organon at $6.90 against a $14.00 offer — $1.86bn of synergy management never disclosed, requiring 3.87% revenue growth against an actual −0.38% two-year CAGR.
<br/><br/>
The spread implies 93.9% completion. A seeded 100,000-path Monte Carlo returns a mean annualised 0.07% against a 4.62% risk-free rate: not paid for the risk it carries.
<br/><br/>
<code>DCF &amp; reverse-DCF</code> <code>event study</code> <code>GARCH(1,1)</code> <code>Granger causality</code> <code>Monte Carlo</code> <code>Black-Scholes</code> <code>statsmodels</code>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/theshaswat/paypal-stripe-advent-ma-valuation">PayPal — Fairness Valuation</a></h3>
<b>$60.50 sits below the floor of all three methods.</b> DCF bear $73.85, trading comps $76.69, precedent floor $64.88. Agreeing with the offer needs a 13.4% discount rate against a calculated 9.67% WACC.
<br/><br/>
A reverse DCF makes the same point from the other side: the $47.37 unaffected close implies ~17%, or five straight years of −11.6% revenue decline — neither consistent with reported results.
<br/><br/>
<code>DCF</code> <code>trading comps</code> <code>precedent transactions</code> <code>sources &amp; uses</code> <code>football field</code> <code>Excel</code>
</td>
</tr>
</table>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s-method.svg"/><img src="assets/s-method.svg" alt="How it's built"/></picture>

One registry holds every externally-sourced figure, tagged by provenance tier; nothing else
contains a typed-in number, so the memo, the notebooks, the deck and the model cannot drift
apart. Each repository carries its own verification suite and runs it in CI on every push — the
Zepto build rebuilds all nine notebooks, the deck, the PDFs and the workbook from source and
re-audits the result, and the PayPal build asserts every committed output still reproduces
byte-for-byte. Primary sources are pinned by SHA-256 rather than redistributed, so a reader can
prove they hold the same document the figures were read from.

Limitations are written down rather than omitted, including corrections made mid-analysis where
an earlier draft was wrong. Two of the three recorded in the Zepto memo are errors a reader
working from secondary coverage would reproduce.

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s-next.svg"/><img src="assets/s-next.svg" alt="Next"/></picture>

Work in progress extends the same standard to a wider toolset: SQL-backed pipelines so the
registry is queried rather than typed, econometric work carried in R and Stata alongside Python,
and a reporting layer in Power BI. Each ships with the same verification suite and the same
written limitations as the three above.

<sub>Independent research. Not investment advice.</sub>
