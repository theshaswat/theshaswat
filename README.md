## Shaswat Sharma

Valuation and market-structure research on live transactions. Primary filings read directly,
numbers reconciled before they are interpreted, and models a reader can recalculate rather than
take on trust.

Three situations so far — a pre-IPO mark, a pending cross-border acquisition, and a reported
take-private bid. Each ships the way the work would ship on a desk: an investment memo, a
committee deck, and a live-formula model that moves when an assumption does.

---

### [Zepto — Pre-IPO Valuation](https://github.com/theshaswat/zepto-pre-ipo-valuation)

**$3.8bn base case against a $7.0bn private mark.** Built before the roadshow range was
consulted; the resulting $2.7–5.5bn range brackets the indications institutions actually gave
($3.0–3.5bn domestic, $4.5bn foreign).

Zepto, Blinkit and Instamart disclose on three incompatible bases — 1P inventory against 3P
commission — which makes headline revenue comparisons wrong by roughly 4.3x. Restated onto net
order value, the binding constraint was never store density: Zepto runs the highest orders per
store per day of the three (1,618) and the weakest basket (₹388, against ₹518 and ₹508). About
4 percentage points of the headline cut is rupee depreciation rather than fundamentals.

<sub>9 notebooks · 9-tab Excel model recalculated cell-by-cell against the Python engine · 8 primary sources read directly, including the 690-page DRHP · every figure traced to one registry</sub>

---

### [Sun Pharma / Organon — Merger Arbitrage](https://github.com/theshaswat/sunpharma-organon-merger-arbitrage)

**Pass on the spread.** Standalone DCF puts Organon at $6.90 against a $14.00 offer, implying
$1.86bn of synergy management never disclosed, and requiring 3.87% revenue growth against an
actual −0.38% two-year CAGR.

The spread implies 93.9% completion probability. A seeded 100,000-path Monte Carlo returns a
mean annualised 0.07% against a 4.62% risk-free rate — the position is not paid for the risk it
carries. Sun Pharma's own announcement CAR was +9.6% and statistically significant, which is the
evidence that cuts hardest against the standalone valuation.

<sub>Market-model event study · GARCH(1,1) volatility regimes · cross-market Granger causality built around non-overlapping NSE/NYSE hours · Black-Scholes priced from first principles after testing and rejecting the listed options chain</sub>

---

### [PayPal — Fairness Valuation vs. the Stripe/Advent Bid](https://github.com/theshaswat/paypal-stripe-advent-ma-valuation)

**$60.50 sits below the floor of all three methods.** DCF bear case $73.85, trading comps $76.69,
precedent-transaction floor $64.88. Making the base case agree with the offer requires a 13.4%
discount rate against a calculated 9.67% WACC.

A reverse DCF makes the same point from the other side: the $47.37 unaffected close implies ~17%,
or five straight years of −11.6% revenue decline — neither consistent with reported results or
guidance. That reads the pre-news price as a sentiment floor, not an intrinsic-value anchor.

<sub>Built in the 48 hours after Reuters broke the story · deal terms unconfirmed throughout, and treated as unconfirmed rather than assumed</sub>

---

### Toolkit

**Valuation and financial modelling**

![Excel](https://img.shields.io/badge/Excel-334155?style=flat-square)
![Python](https://img.shields.io/badge/Python-334155?style=flat-square&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-334155?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-334155?style=flat-square&logo=numpy&logoColor=white)

**Econometrics, inference and machine learning**

![statsmodels](https://img.shields.io/badge/statsmodels-334155?style=flat-square)
![R](https://img.shields.io/badge/R-334155?style=flat-square&logo=r&logoColor=white)
![Stata](https://img.shields.io/badge/Stata-334155?style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit--learn-334155?style=flat-square&logo=scikitlearn&logoColor=white)

**Data and reporting**

![SQL](https://img.shields.io/badge/SQL-334155?style=flat-square)
![Power BI](https://img.shields.io/badge/Power%20BI-334155?style=flat-square)

---

### How the work is built

Each project separates the analysis engine from everything that presents it. One registry holds
every externally-sourced figure, tagged by provenance tier; nothing else contains a typed-in
number, so the memo, the notebooks, the deck and the model cannot drift apart.

Each repository carries its own verification suite and runs it in CI on every push. The Zepto
build rebuilds all nine notebooks, the deck, the PDFs and the workbook from source and re-audits
the result; the PayPal build asserts every committed output still reproduces byte-for-byte.
Primary sources are pinned by SHA-256 rather than redistributed, so a reader can prove they are
holding the same document the figures were read from.

Limitations are written down rather than omitted, including corrections made mid-analysis where
an earlier draft was wrong. Two of the three recorded in the Zepto memo are errors a reader
working from secondary coverage would reproduce.

---

<sub><a href="mailto:shaswatsharma.work@gmail.com">shaswatsharma.work@gmail.com</a> · <a href="https://www.linkedin.com/in/shaswatsharma49">LinkedIn</a></sub>

<sub>Independent research. Not investment advice.</sub>

