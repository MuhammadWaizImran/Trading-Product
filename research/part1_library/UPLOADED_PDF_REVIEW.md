# Review of the four uploaded trading PDFs

Reviewed 2026-09-20. Part 1 research only. No fitting, backtesting experiment, fine-tuning, or training was performed. Original PDFs were not modified. Page references below are PDF page numbers, counting the cover as page 1.

## Decision

These documents are worth reviewing selectively as educational references and as sources of hypotheses to investigate. None is ready for wholesale ingestion as authoritative training text. None supplies evidence that a model trained on it could trade profitably across crypto assets. Several contain errors that a model could reproduce with greater confidence if the files were ingested uncritically.

| Document | Pages | Educational value for our project | Main decision |
|---|---:|---|---|
| Binary Options Trading Bible | 119 | Some elementary candle and trend vocabulary; substantial repetition | Exclude from the core training/knowledge corpus; replace basic definitions with stronger references |
| Waqar Zaka Private Group Lectures, as named by uploader | 44 | Most directly related to crypto screening and research workflow; serious correctness and provenance issues | Keep only independently checked concepts and an original research-journal structure; do not treat the compilation as an authenticated instructor transcript |
| E-Book Binary Sun 7 | 70 | Useful visual setup/invalidation examples; wrong product emphasis and unverified performance claims | Research hypothesis reference only; exclude martingale and unsupported probabilities |
| Trading Chart Patterns in Urdu | 18 | Most useful compact visual glossary and Urdu terminology reference | Best candidate for a corrected educational companion; original diagrams and verified explanations preferred |

These are qualitative judgments about suitability, not measured model performance or numerical quality scores.

## Review method and limits

The four files contain 251 pages. I read the extracted text across the three text-bearing PDFs, inspected rendered overviews of all four files, and examined selected material at larger resolution to confirm important findings. The Urdu guide has no extractable text; its substantive pages were inspected individually as images, including its diagrams and risk tips. Tiny labels inside some broker screenshots remain difficult to read. Those screenshots are treated as illustrations, not independently authenticated trade records. No hidden market-data series, transaction logs, or out-of-sample performance evidence was recovered from these files.

This review assesses the uploaded editions. It does not establish that their named instructors authored or approved every passage, that scans match an original edition, or that the strategies have been empirically validated. PDF creation dates are file metadata, not reliable publication dates. Links within the documents were treated as references, not instructions to open accounts, join groups, or place trades.

## 1. Binary Options Trading Bible

**Identity:** cover credits The Illuminated Trader; file metadata author is ADMIN, with a November 2023 creation timestamp. The upload has 119 pages.

**Coverage:** pages 4–7 introduce fixed-expiry binary options; 8–16 discuss candles and interpretation; 17–23 support/resistance and trendlines; 24–27 market regimes; 28 money management; 29–117 thirty named/numbered setups; 118–119 indicator combinations. Many setup pages repeat the same precautions, so page count overstates unique content.

**Useful material:** basic OHLC anatomy, the distinction between candle bodies and wicks, trend/range vocabulary, and the idea of stating setup conditions. The book acknowledges on page 29 that patterns are not infallible and encourages checking them. These limited strengths do not rescue its definitions or evidence quality.

**Important findings:**

| PDF page(s) | Finding | Consequence |
|---|---|---|
| 12 | Hanging man is described as bullish after a downtrend; inverted hammer is described as bearish after an uptrend | The context/name mapping is wrong under standard terminology. A hanging man is a potential bearish warning after an uptrend; an inverted hammer is a potential bullish reversal after a downtrend. See the [Binance Academy comparison](https://www.binance.com/en/academy/articles/how-to-trade-with-hammer-candlestick-patterns). These are conditional interpretations, not guaranteed forecasts |
| 21 | The trendline-break sentence gives above an uptrend line / below a downtrend line as the reversal break | For the lines the book itself draws, the usual loss-of-trend observation is below rising support or above falling resistance. Text and intended geometry need correction |
| 21, 23 | States that the market does not respect a trendline after the third touch | Unsupported universal rule; a touch count cannot establish the next outcome |
| 24 versus 26 | Claims trends usually have lower volatility than ranges, then says ranges have lower volatility than trends | Internal inconsistency. Directional regime and volatility must be measured separately |
| 28 | Suggests a 10% daily target and permits a 20% daily capital loss | Not an evidence-based capital-preservation policy. Five successive 20% loss days leave 0.8^5 = 32.768% of starting capital; this is arithmetic, not a forecast |
| 29, 118 | Claims up to 90% accuracy and labels later strategies as working every time | No corresponding trade ledger, sample size, confidence interval, or held-out test is supplied. The latter wording conflicts with page 29's disclaimer |
| 31 onward; especially 109–112 | Repeated one-step and some two-step MTG instructions | Loss escalation must not be imported as the product's default risk policy. The precise stake multiplier is not fully specified throughout |
| 37 | Says either one of two related setups will work and asks readers to identify which works that day | Potential hindsight selection. A rule for choosing must be fixed using only information available before the next trade |
| 47 | Sell-setup page contains text directing an up trade | Label inconsistency would contaminate instruction/answer pairs |
| 54–58 | Minimum candle count varies between prose and illustrations | Requires a single reproducible specification before testing |
| 68–73 | Gap logic assumes subsequent candles fill the gap | Hypothesis, not a market obligation; binary/OTC illustrations do not establish behavior on 24/7 crypto venues |
| 103–106 | Named rising/falling-three-method sections use unusual counts and contain a red/green wording mismatch | Do not merge automatically with standard candlestick labels |
| 3 | Explicit reservation of reproduction and retrieval-system rights without prior written permission | The file's fair-use disclaimer is not an affirmative training or retrieval license. This review is not permission clearance |

**Verdict:** not worth using as a core teaching source for the model. A few hypotheses could be rewritten independently and studied later, but more reliable sources already cover its elementary concepts with less correction work.

## 2. Waqar Zaka Private Group Lectures compilation

**Identity:** the filename attributes private-group lectures to Waqar Zaka, but metadata names Mudassar Ali. Page 17 visibly includes a user prompt and a ChatGPT-response label. This demonstrates at least some AI-conversation content; it does not prove the entire document was AI-generated. Authorship and authorization of the compilation remain unverified. Page 44 is a Lecture 08 heading with no lesson body; page 27 is blank.

**Coverage:** pages 2–4 onboarding and promotional links; 5–7 spot screening; 8–22 futures terminology and repeated religious arguments; 23–26 scalping; 28–30 a paper-trade checklist; 30–36 screening/indicators and further derivatives discussion; 37–43 RSI scalping, exits, divergence and context.

**Useful material:** a discover → inspect → record-reasoning workflow; research of a project's use case; attention to volume; a journal containing timeframe, entry assumptions, invalidation and outcomes; demo-first practice; and later warnings that divergence may fail and that waiting is sometimes sensible. These ideas fit our research product after independent rewriting and correction.

**Important findings:**

| PDF page(s) | Finding | Required treatment |
|---|---|---|
| 5–7 | Prioritizes the week's biggest losers and implies a stronger bounce opportunity | Treat mean reversion as a testable hypothesis. Falling tokens can continue falling or fail; discovery must also allow momentum and no-trade cases |
| 6 | Presents high-volume green/red candles as determining subsequent direction and low volume as implying stable prices | Overconfident. Volume is activity, not a guaranteed forecast or a count of unmatched buyers versus sellers; units also need specifying |
| 10 | Says a limit order executes when price reaches it | Omits queue position, available size and partial/non-fills. [Fidelity's order explanation](https://www.fidelity.com/bin-public/060_www_fidelity_com/documents/learning-center/Transcript_Investing%20101_v2.pdf) distinguishes limit price from guaranteed execution |
| 17 | Includes ChatGPT conversation markers | Separate attributed source claims from generated commentary; neither gets authority from the filename |
| 19 versus 20 | Correctly says negative funding means shorts pay longs, then reverses this in the worked example | Definite internal error. [Bybit's funding documentation](https://www.bybit.com/en/help-center/article/Funding-fee-calculation) confirms the payment direction; positive funding is longs paying shorts |
| 20 | Implies the funding sign determines subsequent market direction | Funding mechanics are not a deterministic price forecast |
| 26 | Labels $1,490 as 1% below $1,500 | It is about 0.667%; 1% below is $1,485 |
| 26 | Calls RSI 35 oversold despite using a below-30 threshold elsewhere | Inconsistent unless a different threshold is explicitly declared |
| 29 | Gives liquidation price as entry minus entry/leverage without qualification | At best an idealized long-position bankruptcy approximation. It omits maintenance margin, fees, added margin, contract type, cross-account effects and short direction. [Bybit's liquidation process](https://www.bybit.com/en/help-center/article/UTA-Trading-Rules-Liquidation-Process?tabIndex=2) explains maintenance-margin and account-mode dependencies |
| 29–30 | Uses a long-style P&L formula and below-entry stop convention in a wider long/short workflow | Specify position direction and instrument. A linear short reverses the price difference; inverse contracts need different formulas. Net results also include costs |
| 31–32 | Treats a volume threshold as high liquidity and a market-cap band as safer | Missing units/time window, spread/depth, concentration and observed execution quality; market cap alone does not establish safety |
| 35 | Says exchanges retain liquidated money as their profit model | Overgeneralized and unsupported; settlement, counterparties, fees and insurance mechanisms are not interchangeable |
| 37 versus 38 | Mentions 200x after practice, then advises a 5x–10x maximum for beginners | Material risk-policy inconsistency. For a simple linear exposure, a 0.5% adverse move at 200x equals the initial margin before maintenance and fees; actual liquidation may happen earlier |
| 38 versus 40, 42 | Advises no stop loss, then requires stops | Cannot produce a coherent risk policy from these instructions without choosing and justifying a corrected policy |
| 38 | Labels selling under a spot strategy as a short trade | Selling owned tokens is not the same as opening a short exposure. Borrowing/margin/derivative mechanics must be explicit |
| 40 | Adds trade price-return percentages to state an account-level profit | Assumes a sizing/base convention and ignores fees, compounding and leverage. Price return, margin return and portfolio return need separate fields |
| 12–22, 33–36 | Presents religious permissibility conclusions | Keep as attributed opinions outside model market-fact labels. This review does not issue a religious ruling or authenticate the cited religious sources |

RSI thresholds alone are not proof of reversal. [Fidelity's RSI guide](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/RSI) explicitly describes persistence in extreme zones during strong trends. Later contextual cautions in the compilation are more useful than its early automatic-signal language.

**Verdict:** useful for identifying user-facing research questions and Roman Urdu vocabulary; unsuitable as uncorrected ground truth. The trade journal is worth redesigning. Its trading recipes need independent evidence, and repeated religious/promotional/AI-conversation material should not enter the market knowledge corpus.

## 3. E-Book Binary Sun 7

**Identity:** visible Binary sun7 branding and @binarysun7 handle. No verified real-name authorship or affirmative reuse license was established. Filename says 2023; metadata contains an April 2023 modification timestamp, not a verified publication date.

**Coverage:** pages 1–10 trendline-touch setups using one/five-minute candles and five-minute expiry; 11–25 wide-range bars and invalidations; 26–30 two-candle breakout; 31–37 engulfing breakout; 38–48 full-fill-left-candle setups; 50–56 wick breakout; 57–62 color sequences; 63–70 support/resistance role reversal and retests. Pages 5, 10 and 49 are essentially watermark-only separators.

**Useful material:** this document does include invalid/avoid examples, particularly pages 16–25, and explicitly discusses confirmation, nearby opposing levels, market context and avoidance. The distinction between a body break and a wick touch is useful to formulate precisely. It is a better source of annotation questions than an authenticated performance dataset.

**Problems:** page 31 claims more than 90% accuracy, while pages 27, 32, 39 and 41 assign approximate retracement/error frequencies without a documented sample or calculation. One-step martingale is repeatedly suggested (for example pages 29, 32, 45, 48, 52, 58 and 65). The wide-range-bar definition on page 12 refers to recent candle sizes without a fixed lookback and has an unclear cutoff around three times normal size. Terms such as healthy market, momentum, proper breakout and margin-of-safety entry need numerical definitions.

The figures include outcome candles and arrows marking entries. Giving a vision model an image that already shows the future and then asking it to predict that future would leak the answer. Cropped screenshots also lack a consistent asset/venue/date/timeframe record. Some contain losing/error examples, but they do not establish their frequency among all eligible signals. Binary expiry payouts and broker quotation rules differ from spot/perpetual returns and exchange execution.

**Verdict:** selectively useful for designing positive/invalid/ambiguous annotation categories and later hypotheses. Not sufficient for predicting crypto returns. Exclude performance percentages and loss-escalation instructions from accepted knowledge.

## 4. Trading Chart Patterns in Urdu

**Identity:** back cover credits Maher Abdullah. Eighteen scanned image pages; no searchable text layer. The PDF software's AGPL label concerns its producer software, not a license to the book or illustrations. No affirmative content-reuse license was found in the visible pages.

**Coverage:** page 2 practical tips; 3 a candle-pattern collage; 4 double bottom; 5 double top; 6 triple top; 7 pennant; 8 cup and handle; 9 flag; 10 head and shoulders (including an inverse schematic); 11–12 rising/falling wedges; 13 diamond; 14–16 ascending/descending/symmetrical triangles; 17 descending channel; 18 authorship/back cover.

**Strengths:** concise Urdu explanations paired with geometry, breakout/neckline locations, suggested invalidation areas and target illustrations. Page 16 explicitly allows a symmetrical triangle to break either way. Page 2 encourages research, discipline and avoiding concentration/scams. These fit an educational glossary and explanation interface.

**Corrections and limits:**

- Page 8 categorizes cup and handle as a trend-changing pattern. The usual classification is bullish continuation, although context can produce a base/reversal interpretation. Preserve that distinction rather than teaching one universal label. See [Binance Academy's definition](https://www.binance.com/en/academy/glossary/cup-and-handle).
- The general 2% capital wording on page 2 and other pages does not clearly separate capital allocation from loss at invalidation. Those are different quantities, especially with leverage.
- Pattern heights are presented as targets; these are conventions to test, not promised destinations or calibrated probabilities.
- Trend, breakout distance, equality of peaks, lookback, retest timing and invalidation tolerances are not specified rigorously enough for consistent machine labels.
- Most examples show the expected outcome; the collection needs failed formations, false breakouts and genuinely ambiguous cases.
- Screenshot axes, asset identity, dates and venue are not consistently recoverable. The pictures cannot substitute for auditable OHLCV data.
- Scanned Urdu and tiny chart text require human-checked transcription before any permitted ingestion. A vision model's plausible transcription alone is insufficient.

**Verdict:** worth keeping as the most useful visual teaching companion of these four, after corrections. Build original examples and a bilingual glossary; do not use its target arrows as return labels.

## Why binary-options success rates do not transfer

Binary options settle according to a specified yes/no outcome with a fixed payout structure; the [SEC's educational explanation](https://www.investor.gov/protect-your-investments/fraud/types-fraud/binary-options-fraud) describes this distinction. Our product instead needs conditional crypto research, uncertainty, costs and abstention.

For an illustrative binary contract with an 80% net win and a 100% loss, expected profit per unit staked is 0.8p - (1-p), so break-even is p = 1/1.8 = 55.56%, before additional charges and assuming no ties. This is an illustrative assumption, not a payout verified for a platform in the uploads. With that payout, losing stakes 1 and 2 and then winning stake 4 produces -1 -2 +3.2 = +0.2; three losses produce -7. Stake escalation does not establish a forecasting edge or eliminate losses. A capped martingale limits escalation but still changes drawdowns and capital requirements.

For spot/perpetual research, a correct directional forecast can still lose after fees, spread, slippage, funding or a bad exit. We need distributions of outcomes and drawdowns, not just attractive screenshots or win percentages.

## What we should use, and how

1. Preserve these PDFs privately as reviewed references, with the correction record beside them. No wholesale embedding, fine-tuning upload, or redistribution is approved by this review.
2. Create original, independently corroborated concept notes: OHLC geometry, trend/range, support/resistance, breakout confirmation, volume units, funding mechanics and uncertainty. Keep links and page references to disagreeing sources.
3. Use a pretrained language model later to explain verified evidence through retrieval where source rights permit. These 251 pages do not justify training a language model from scratch. Whether fine-tuning adds value remains a later evaluation question.
4. For numerical learning, use timestamped market records with measurable future outcomes. For chart understanding, pair original rendered charts with underlying OHLCV, cutoff time, reproducible pattern labels and separate outcome records.
5. Keep failed and ambiguous examples, not just successful formations. Use separate labels for shape recognition, conditional hypothesis and realized net outcome.

## What else is needed for the broad crypto scope

| Priority | Missing ingredient | Why these PDFs cannot supply it |
|---|---|---|
| Essential | Coin/instrument directory: chain, contract identity, venue, pair, listing/delisting dates | Coin names in teaching examples are not a coverage universe |
| Essential | Multi-coin historical OHLCV with exact timestamps, quality flags and provenance | Screenshots cannot establish complete chronological histories or failures |
| Essential | Fees, spreads and conservative execution assumptions; depth/trades where available | Short-horizon results depend on actual trading friction |
| Essential for derivatives | Contract specifications, mark/index prices, funding histories and available open interest | General descriptions and incorrect formulas are insufficient |
| Essential | Original chart examples across many assets/regimes with success, failure and ambiguity labels | The PDFs contain selected illustrations and often visible future candles |
| Important for coin selection | Dated supply/unlocks, project disclosures, security events, liquidity/concentration and news | These books mostly teach chart vocabulary, not point-in-time coin fundamentals |
| Essential | Held-out time periods and unseen-coin evaluation design | Source agreement does not demonstrate generalization |
| Essential for corpus ingestion | Document provenance and intended-use permissions | Upload access alone does not settle downstream product rights |

Not every field must exist for every coin before useful research can begin. Define capability tiers: insufficient coverage, price/volume research only, and richer fundamentals/derivatives coverage. Discover broadly and report missing evidence rather than implying that a small sample represents all coins. New tokens and illiquid markets may merit a wait/insufficient-data answer.

The highest-value next input from the user is the original publisher/download links and any licenses or permissions that came with the PDFs. If an instructor provides a real strategy-results dataset, request the complete dated trade ledger including losses, instrument/venue, precise entry/exit rules, costs and all selection criteria. The user does not need to purchase or collect a large pile of additional books; broader legitimate market-data research remains our project work.

These uploads do not resolve the earlier playlist-access blocker, and this review does not mark Part 1 complete. The immediate recommendation is a corrected knowledge library plus a multi-coin data-coverage inventory. All eventual model training stays on authorized cloud compute after the Part 1 gate is satisfied.
