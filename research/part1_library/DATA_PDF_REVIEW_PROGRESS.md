# Data PDF: ongoing critical review

Updated 2026-09-24. **The library review remains incomplete and is not a certificate that every PDF is training-ready.** Selected corrected examples have been used in separately documented, cloud-only Phase 2 runs; this ledger records source review rather than model performance.

Latest addition: [DP21 critical review](DP21_CRITICAL_REVIEW.md) records all 60 pages of extracted text read and 14 pages visually inspected. Formula verification and replication remain incomplete. DP22 is the identical copy, not additional independent evidence. Other rows below retain their earlier checkpoint unless explicitly updated; later module reviews (DP05, DP10, DP16 and DP17) add selected coverage. Historical rights-hold wording below predates the user's attestation of private training permission; it is not a new request for the same permission and does not authorize public redistribution.

## Scope and honest coverage

22 uploaded PDFs contain 2,194 physical pages. SHA-256 deduplication leaves 20 files and 2,020 pages. DP01/DP02 and DP21/DP22 are identical pairs. DP19/DP20 are near-duplicates: extracted text differs in author-line spacing and an acknowledgment adding Fabian Schär. They are not two independent studies.

Private review extracts and the complete inventory are in `tmp/pdfs/data_pdf_review/`. Extraction is NOT reading, checking diagrams, verifying claims, or approval for model ingestion. Source PDFs have not been modified. Page references below are PDF page numbers, including covers.

| ID | Document | Review coverage as of this checkpoint |
|---|---|---|
| DP01/02 | Cryptocurrencies and Blockchain, World Bank | Crypto chapter pages 35–63 read and selected visuals checked; exact duplicate DP02 excluded; other macro/country chapters not treated as crypto curriculum |
| DP03 | Crypto-currencies and the Future of Money | All 116 pages' extracted text read; pages 33–40, 74–78 and 86–94 rendered, with key diagrams/charts visually checked |
| DP04 | Future of Exchanging Value | All 68 pages' extracted text read; scenario matrix and key Bitcoin/XRP/reserve pages 22, 48, 49 and 51 visually checked; remaining visuals pending |
| DP05 | Crypto for Beginners: Technical Analysis | All 49 pages' extracted text read; visual verification pending |
| DP06 | Risk Management, Elisa Crypto | All 11 pages' extracted text read; visual verification pending |
| DP07 | Introduction to On-Chain Analysis, Patrick Scott | All 31 pages' extracted text read; visual verification pending |
| DP08 | Binary Options Trading Bible | SHA-256 matches earlier reviewed copy; earlier review and its visual limitations carried forward |
| DP09 | Sami Malik Sir Sureshots | All 8 image pages individually viewed and read; smallest text limited by source resolution |
| DP10 | Mastering Crypto Day Trading, Chino | All 306 pages' extracted text read; pages 174, 175, 193, 209, 264 individually rendered and checked; remaining visuals pending |
| DP11 | Waqar Zaka lectures | SHA-256 matches earlier reviewed copy; earlier review carried forward |
| DP12 | Advanced Liquidity Trading Concept, Daniel Stones | All 49 pages' extracted text read; chart verification pending |
| DP13 | Binary Sun | SHA-256 matches earlier reviewed copy; earlier review and its visual limitations carried forward |
| DP14 | Chart Pattern Urdu | SHA-256 matches earlier visually reviewed copy; original source-resolution limitations remain |
| DP15 | Bitcoin and Beyond | Extracted; substantive review pending |
| DP16 | Bitcoin and Cryptocurrency Technologies | Extracted; substantive review pending |
| DP17 | Binance Academy trading ebook | All 67 pages' extracted text read; visual verification pending |
| DP18 | Mastering Bitcoin | Extracted; substantive review pending |
| DP19 | Order Book Liquidity on Crypto Exchanges | All 29 pages' extracted text, tables and references read; pages 15, 17, 18 visually checked; other visuals/equations pending |
| DP20 | Same order-book paper | Full extracted-text comparison with DP19 performed; acknowledgment difference; visual comparison pending |
| DP21/22 | Economics of Cryptocurrencies | All 60 pages' extracted text read on 2026-09-24; pages 7, 8, 10, 12, 13, 29–34, 51, 53 and 54 visually inspected; equations/replication and remaining visuals not certified; see DP21_CRITICAL_REVIEW.md |

## Findings recorded during reading

### DP04: historical payments analysis, not trading evidence

Copyright 2015 Deloitte (page 68). The filename attributes Nicholas Gruen, but he supplies the foreword; pages 65–66 identify Peter Evans-Greenwood, Ian Harper, Robert Hillard and Peter Williams as authors. Useful for trust, payment adoption, complementary currencies and the distinction between currency adoption and distributed-ledger adoption. Pages 20–24 present scenarios, not observed outcomes or trading targets. Many product, policy and adoption statements describe 2015 and must retain that date.

Pages 46–49 require technical verification: the Bitcoin/bitcoin capitalization convention is reversed from common usage; mining is described as signing, and additional miners are associated with near-instant transfers without explaining difficulty adjustment. Page 49 claims scarcity should cause XRP appreciation: scarcity alone does not establish future demand or returns. Historical XRP reserve/fee numbers must not become current protocol facts. Pages 51 and 64 contain a temporal inconsistency: the text anticipates renminbi inclusion in the SDR basket while the endnote cites its November 2015 approval. Pages 57–61 make strong forward-looking adoption and efficiency assertions; retain as dated author judgments, not universal facts. No open reuse/training license identified. Training ingestion on hold; potential historical background reference after correction. Charts not yet visually verified.

Visual review confirms page 22 is a generic two-axis scenario-planning matrix rather than observed evidence or a probability model. Page 48 visibly describes mining as bundling and signing transactions and implies more miners enable near-instant transfers; both need correction because mining proposes proof-of-work blocks and difficulty adjustment prevents added hash rate from linearly increasing long-run block frequency. Page 49 visibly states that XRP scarcity should cause appreciation, which is an unsupported price inference, and its protocol quantities are dated 15 September 2015. Page 51's foreign-reserve chart ends in 2014 and cannot support a current reserve-composition claim. These issues are in the rendered PDF, not extraction artifacts.

### DP03: full extracted text read; selected visuals checked

Pages 1–10 describe a 2019 interdisciplinary monetary report, including an eight-country public-perception survey later in the document. Early monetary definitions are explicitly a theoretical framework; do not label a particular theory as the only accepted definition. The extraction drops some initial letters and scrambles the page 5 money-flower diagram; visual checking is necessary before reusable text is produced. Survey methods, results, subsequent chapters and rights remain to be reviewed.

Pages 11–40 extend the monetary-history and balance-sheet discussion. Page 23 explicitly marks Venezuela 2018–2024 values as forecasts from an April 2019 source: these must never be ingested as realized historical inflation. Pages 26–28 present a mechanical deposit-multiplier story alongside a Bank of England quotation; verify the original monetary-creation explanation before reuse, particularly the assertion that declaring a loan bad destroys money in the same way as repayment. Page 29 calls Irving Fisher a Nobel laureate; flag for primary-source verification. Pages 31, 33–34 assert asset backing removes the need for trust and that blockchain security ensures value; these need correction to distinguish transaction validation from reserve custody, redemption and market-price risk. Page 33's extracted balance-sheet amounts show +100 financial assets versus +1000 Bitcoin; page 34's scenarios 6 and 7 repeat identical labels despite different transaction descriptions. Render those pages to determine source errors versus extraction artifacts. Page 37's cash/credit-card and broad-money taxonomy requires care: a payment instrument, credit facility and monetary asset are not interchangeable. Page 38's survey charts and pages 39–40's taxonomies require visual review. No final document verdict yet.

Pages 41–68 cover arguments for replacing cash, permissioned and permissionless ledgers, consensus, trust, supply, usage, mining concentration, security and pseudonymity. Useful concepts require corrections: a distributed ledger shifts rather than removes all trust; public source code, read access, transaction submission and validation authority are separate properties; governance is not inherently democratic; address counts are not person counts; and market figures, acceptance claims and network examples are dated around 2018–2019. Ethereum's consensus status in the proof-of-stake discussion must not be taught as current from this source.

Pages 69–78 distinguish retail and wholesale CBDCs and discuss design and financial-stability channels. Figures 23–24 visually confirm that the central-bank activity and issuance-likelihood results are survey evidence reported for 2017–2018, not current deployment facts. Page 78 presents rapid movement from commercial-bank deposits into a central-bank liability as a plausible stress mechanism, not an inevitable bank run.

Pages 80–97 report an eight-country survey and a hypothetical-currency conjoint experiment. The report states 1,000 respondents per country and varies five attributes: issuer/backer, acceptability, transaction cost, price stability, and digital/physical form. Figure 38 was visually checked: its estimates are country-specific effects relative to omitted baselines under the survey design, not market-return predictions. The survey is a dated stated-preference snapshot and does not represent every country or all crypto users. Page 86 is decorative photography and carries no analytical evidence. Pages 98–116 contain lists, references, annex country profiles, credits and license material. Page 103 declares CC BY-NC-SA 4.0; page 115 identifies the research team and recommended citation.

Visual inspection confirms that page 33's Bitcoin balance-sheet figure prints an internally inconsistent +100 asset versus +1000 money amount. Page 34's stablecoin diagram also presents amounts and liabilities that should not be converted into training targets without independent reconstruction. Figure 5 on page 40 is useful as a dated design taxonomy, not a complete modern classification. Decision: selected, corrected educational concepts are usable with attribution and the user's permission, while uncorrected absolute claims, inconsistent diagrams, forecasts and dated product/market statements are excluded. A reviewed 24-train/4-validation/4-test example set is stored in `research/pdf_training_dp03.json`; contribution of those examples will not mean every page was memorized.

### DP05: introductory TA, useful only with corrections

Covers charts, trends, volume, classical patterns, candlesticks, SMA, RSI and ADX. Many examples are stock-market oriented despite the crypto title. Page 19 discusses equity delivery percentage, which must not become a generic crypto feature. Pages 24–26 give conventional pattern durations, not universal duration constraints across crypto timeframes. Page 32 mixes bullish engulfing with the words bearish engulfing and describes engulfing a previous high rather than consistently distinguishing body from wick. Page 39 dates ADX to 1987; verify against Wilder's original publication before retaining. Formula descriptions need smoothing/initialization details for reproducibility. Pages 44–49 promote a signals community and testimonials; these are not verified performance data. Introductory claims that patterns work more often than fail are not substantiated by an outcome dataset.

### DP06: risk arithmetic is not a proven return distribution

Pages 4–7 teach risk-at-stop and position sizing, including the useful distinction between amount invested and amount at risk. The long-position reward/risk formula is not a universal formula for short positions. Page 8's break-even win rates assume fixed payouts and no fees/slippage. Page 9 compares selected chart entries without measured stop-hit probabilities. Page 10 calls a hypothetical 60% win rate, 3R payoff and 15 trades/month conservative: its 21R sum is arithmetic, not evidence of achievable monthly performance. Fixed-notional leverage does not change linear price P&L but can change margin/liquidation exposure. Stop placement ahead of a liquidation price is not an execution guarantee. Rights unresolved; no wholesale ingestion approval.

### DP07: wallet-research primer, not comprehensive on-chain analytics

Useful explorer, wallet, entity and new-pair workflows; includes warnings against blind copying and against treating scanners as guarantees. Page 5 oversimplifies the normal Transactions tab as ETH transfers only: contract calls also occur there. Pages 11–13 discuss holder counts and verified code; neither proves legitimate demand or safety. Pages 15–16 select a token after its successful 2023 rise and then a prior holder: this can introduce hindsight bias in a dataset. Page 26's transfer links are clues, not proof that wallets have one owner. Page 31 explicitly says on-chain analytics is outside the guide's scope. Tool availability, prices and UI are dated, not verified current facts. Rights unresolved.

### DP09: no defensible accuracy evidence

Pages 1–6 illustrate next-candle continuation/reversal ideas with schematic candles, no timestamps, symbols, exchange, outcomes, costs or reproducible selection rules. Page 3 labels different upper/lower-wick formations as green/red hammers without standard context distinctions. Page 7 lists additional named SNR types without defining them. Page 8 repeatedly asserts success above 95%, sometimes 75%, by regime; there is no test sample or methodology anywhere in the eight pages. Several table setup names lack accompanying definitions. Useful only as unverified hypotheses or examples of unsupported certainty. Not trusted target labels; rights unresolved.

### DP10: full extracted text read; substantial repetition and material numerical errors

Pages 1–70 cover blockchain, tokens, DeFi, exchanges/wallets, strategies, psychology and tools. Breadth does not establish depth. Page 15 implies every hard fork creates two persistent chains; continued chain splits require additional conditions. Page 23's description of impermanent loss as temporary is incomplete. Page 38's cold-wallet immunity wording is too absolute. Page 41 losing a seed backup is not identical to immediately losing access if a functioning wallet/key remains. Page 42 needs chain/network identity as well as asset/address checks. Pages 48–55 describe strategy families, not sufficiently specified and validated rules. Product recommendations and regulatory claims require date-specific checking.

All extracted text through page 306 has now been read, including repeated chapters. Psychology recurs in chapters 6, 11, 16, 23 and 27; advanced strategies in 10, 14, 18, 24 and 28; tools in 7, 15, 22 and 26; risk in 17, 20 and 25. These are not independent corroborating sources. No audited trade ledger, reproducible empirical outcome study, or full market dataset appears in the text. General backtesting advice (71) is useful but not an implemented leakage-controlled research protocol.

Visually confirmed corrections (not text-extraction artifacts):

- Page 174: a $40,000 entry stopped at $40,000 is break-even before costs, not profit locked in.
- Page 175: raw LaTeX and duplicated malformed formulas are visible in the PDF itself. The numerical $200/$500 = 0.4 BTC example is arithmetically correct under linear spot assumptions, but formatting needs reconstruction and notional/margin checks.
- Page 193: a retracement from $40,000 after a rise from $30,000 gives $36,180 at 38.2% and $35,000 at 50%; the book prints $38,000 and $35,500. These are arithmetic errors, not disagreements about whether Fibonacci trading works.
- Page 209: $100 risk and a 10% stop imply $1,000 notional before costs, not a computable number of coins without an entry price. The printed ten-unit result conflates percentage with dollar distance.
- **Page 264: ($10,000 × 1%)/$2 = 50 coins, not the printed 500. Following that example would risk $1,000, ten times its stated $100 budget, before costs.**

Additional textual issues: page 143 defines leverage as borrowed capital/own capital while its example uses total exposure/own capital; page 148's lower-DEX-fee generalization contradicts the opposite generalization on page 36. Page 128 implies ML accuracy improves automatically with time. Pages 105, 268 and 304 wrongly imply a favorable target reward/risk ratio ensures profitability: realized probabilities and costs are also required. Page 292's approximately 33% success at 2:1 reward/risk is not profitable: exact 1/3 is break-even before costs; 33% is slightly negative. Tax and product sections must be held as dated/unverified instead of taught as current universal rules. Page 160 contains an unfinished editorial placeholder. Author's claimed trading experience is self-reported, not independently verified.

Decision: not a trustworthy uncorrected training reference. Some introductory content may inform an independently verified curriculum; numerical-risk examples require rejection/correction before any reuse. Rights unresolved. Full visual review of all illustrations remains outstanding.

### DP12: distinguish hypothesized stops from observed order-book liquidity

Copyright page 3 explicitly reserves reproduction/distribution rights; hold from training/index ingestion unless appropriate rights are established. Pages 5–27 explain chart-based stop/liquidity narratives. Page 6 appropriately admits the stop locations are assumed, but later passages treat institutional intent and manipulation as established from the chart. Candles alone do not identify an institution, its intent, or hidden stop inventory. Pages 28–33 introduce tradability, FX sessions and liquidity; page 32 says forex is open every day of the week, and page 33 conflates ATR with volume/liquidity. Pages 36–44 repeatedly infer institutional fills without slippage; illustrated reversals do not establish this. Page 49 explicitly notes swing points are confirmed after lookback bars: backdated plots must never be treated as signals known at the pivot time. Chart review is still pending.

### DP17: useful broad primer; attribution does not remove the need to check errors

Good discussions of hindsight (11–12), liquidity/slippage (35–38), paper-trading costs (31–32), and RSI extremes persisting (54). Page 29 incorrectly names Charles Wyckoff; Binance's own current article names Richard Wyckoff. Page 34 calls selling an existing spot holding a short position: distinguish reducing a long holding from establishing negative exposure. Page 39 guarantees stop-market exit even under extreme conditions; liquidity, outages and exchange rules limit that claim. Page 40 correctly defines best bid/ask in the first paragraph but reverses buyer/seller extrema in the next. Page 65 describes all five Ichimoku lines as averages; the lagging line needs separate treatment. General claims about negligible fundamentals and greater signal reliability through confluence are not established evidence. Current product availability and rights remain unresolved.

Verification: [Binance's Wyckoff article](https://www.binance.com/en/academy/articles/the-wyckoff-method-explained), updated 2026-08-11 and checked 2026-09-21, names Richard and frames the Composite Man as a mental model, not direct evidence of an identified operator. [Etherscan transaction documentation](https://info.etherscan.com/understanding-an-ethereum-transaction/) opened for the explorer correction; detailed comparison remains pending.

### DP19/20: valuable research methods, not the underlying dataset

Angerer, Gramlich and Hanke (2025), DOI 10.3390/jrfm18030124. Page 1 declares CC BY 4.0 for the article; distinguish article rights from its dataset. Pages 5–6 describe January–September 2019 data from Binance, Kraken, Huobi and OKEx and 1,086 exchange-pair series after filtering. Page 26 explicitly says underlying data are proprietary/confidential and purchasable from CryptoTick. It is not a free dataset supplied by the uploaded paper.

Useful material: reconstruction from snapshots/updates, UTC timestamps, invalid-spread/negative-quantity checks, delistings, relative spreads, depth, imbalance, transaction costs and exchange comparisons. The paper uses 'base' for the price-denomination currency; map terminology explicitly because common exchange APIs use quote currency for that role. Its imbalance sign is ask-minus-bid, opposite to some common implementations.

Verification questions before encoding the novel measure or numerical tables:

- Page 6 prose says Binance has 162 targets/515 pairs but Table 1 has 161/514.
- Page 15 calls correlations negative but one sentence says higher spreads accompany greater variation; its later explanation goes in the opposite direction.
- Page 17 calls the depth/spread relationship positive and then says lower spreads accompany higher depth.
- Page 5 states up to 20 levels, while page 18 reports mean maximum variation 39.4 for Huobi stablecoins. Equations 8–10 bounded by L need reconciliation with actual implementation.
- Page 17 has nonmonotonic cumulative bid-depth entries for OKEx/ETH (L10 57.5, L15 34.9). Check rendered table and possible changing sample definitions rather than silently correcting values.
- Page 24 lists 279 time dummies whereas the stated Jan–Sep 2019 period is 273 days. Check original version/data definitions.
- Fixed effects and a negative correlation do not by themselves establish causal direction. Contemporaneous regression is not an out-of-sample forecast or demonstrated profitable strategy. Significance is not the same as economic usefulness.

These are review flags, not accusations of fabricated research. Pages 15, 17 and 18 were individually rendered: the contradictory prose and noted table values are visible in the PDF, not extraction mistakes. Other checks and possible publisher corrections remain unresolved. Publisher web page returned HTTP 429 during this check; uploaded text remains the inspected evidence.

### DP01/02: crypto chapter reviewed and used selectively

Cover and copyright identify the World Bank's May 2018 Europe and Central Asia Economic Update. It includes substantial regional macroeconomics and country profiles in addition to the crypto chapter; do not count all 114 pages as trading education. Page 4 states CC BY 3.0 IGO, with attribution, adaptation/translation notices and third-party-content qualifications. The crypto chapter on pages 35–63 was read and converted into a reviewed 24-train/4-validation/4-test set in `research/pdf_training_dp01.json`. The examples preserve dates and uncertainty, correct the address/entity distinction, and avoid treating supply limits, collateral, or blockchain validation as guarantees. DP02 is an exact duplicate and was excluded.

## Provisional answer to 'is it enough?'

There is enough material to justify a serious educational-library review. There is not yet a basis to certify a complete, correct, rights-cleared training corpus. It is premature to say which educational topics are entirely absent while longer books remain unread.

For learning and evaluating market outcomes, documents cannot replace timestamped multi-coin observations, point-in-time asset identities and listings/delistings, fee/funding/liquidity records where relevant, reproducible labels, failed/ambiguous examples, and an untouched evaluation set. Books that explain these items do not supply those observations automatically. Broad crypto coverage needs a defined, measurable universe and explicit insufficient-data handling for new/illiquid coins; no claim of universal reliability for every coin.

Do not request another indiscriminate batch of PDFs yet. Finish the existing review, resolve corrections and any remaining specific rights issues, then request missing evidence precisely. Part 2 has already been authorized despite incomplete Part 1; any future fitting stays cloud-only. Full review, training completion and demonstrated model performance are separate milestones.
