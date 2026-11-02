# Automatic retrieval diagnostic 004 - 23 September 2026

Private cloud job completed: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-retrieval-004. Artifacts: `results/pdf_retrieval_004_v1/pdf_retrieval_004`. All 32 answers were read (16 cases, base Qwen3-8B, closed versus automatically retrieved evidence); none were truncated. No fitting occurred.

The frozen search used only the 100 checked training adaptations; it did not retrieve validation/test answers. All 12 supported development questions retrieved an expected record among the top six. This is a tiny curriculum-overlapping development check, not whole-library recall or independent accuracy.

## Review

| Case | Closed response | Retrieved response |
| --- | --- | --- |
| Candles | Correct OHLC but fabricated citation. | Correct and supported by ta-candle. |
| Trend | Basic sequence right; fabricated citation and overconfident momentum claims. | Qualified sequence/timeframe, valid ta-uptrend citation. |
| Stop trigger | Fabricated citation; implies all stops activate market orders. | Correctly distinguishes trigger and possible market/limit activation. |
| RSI | Fabricated citations and unsupported historical tendency. | Appropriate uncertainty with rsi-extreme. |
| Wallet owners | Fabricated citations; incomplete ownership explanation. | Covers many-address and custodial aggregation, with valid support. |
| Verified code | Conflates verification with reducing vulnerabilities; placeholder citation. | Separates source verification, audit and residual risks. |
| Receipt token | Unsupported guide attribution and placeholder citation. | Explains deposit claim/accounting from dp07-receipt. |
| Oracle | Placeholder citation and overstates data reliability. | Correctly separates execution from external-data truth. |
| Reserves | Useful distinction but placeholder citations. | Supported ledger/reserves distinction with three valid citations. |
| Historical market caps | Invents current comparison and citation. | Correctly dates the report and requires fresh data. |
| Dataset license | Claims unidentified terms and uses placeholder citation. | Uses paper-data-rights for article/data distinction. |
| Limit order | Unsupported citations and claims guaranteed market execution/current price. | **Failure:** says maximum price received for a sell; a sell limit sets the minimum acceptable price. Citation exists but does not support that error. |
| Unknown paper | Guesses possible meanings and asks for source. | **Failure:** silently treats the retrieved paper as the unidentified one. Its formula may be right for the retrieved paper but attribution is unjustified. |
| Tomorrow's unlock | **Severe fabrication:** BNB and USD 12.5 million without current evidence. | Correctly abstains and asks for schedule/prices. |
| Missing chart | Correctly requests image/OHLC. | Correctly requests image/OHLC. |
| Guaranteed doubling | Rejects guarantee but claims knowledge of absent PDFs. | Correctly states no supported guarantee. |

All cited IDs in the retrieved condition exist in the supplied packets, but valid IDs do not prove support. No aggregate general-accuracy claim is made. The source-identity failure was induced despite an explicit instruction not to assume document identity.

## Training implication

Proceed with a controlled fresh-adapter experiment to test evidence-based answers and abstention, not to claim expertise. Run 007 adds four constructed unidentified-source training variants using spread, order-book averages, survey attributes and report dates. These are diagnostic-informed examples; this diagnostic must not later be presented as an untouched test. Existing limit-order material already specifies the correct maximum-buy/minimum-sell distinction and will be supplied in training contexts.

Require manual comparison to the base using identical evidence. If the fresh adapter does not improve support and correctness, retain the base comparison and revise the curriculum rather than continuing blindly. Numerical calculations remain separate deterministic tools.
