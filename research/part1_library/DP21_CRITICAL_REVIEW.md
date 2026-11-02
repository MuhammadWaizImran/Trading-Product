# DP21 critical review: payment economics, not a trading model

Reviewed 2026-09-24. Private project notes. Physical PDF page numbers include the added cover; printed page numbers are one lower.

## Identity and actual coverage

Jonathan Chiu and Thorsten V. Koeppl, *The Economics of Cryptocurrencies: Bitcoin and Beyond*. The uploaded work states September 2018 on PDF page 2 (first version March 2017). File: `Data PDF/the-economics-of-cryptocurrencies-bitcoin-and-beyond-jonathan-chiu-thorsten-v-koeppl-8301 (1).pdf`. SHA-256: `6c90164ec5cb84be4e7445ea6ab470e14207aa4f4735748125bf8c225a3765e3`. DP22 is an exact duplicate and adds no independent evidence.

All 60 pages of extracted text were read in page batches, including references and appendices. Truncated output for pages 43–50 was reread separately. Pages 7, 8, 10, 12, 13, 29–34, 51, 53 and 54 were individually viewed as rendered images (14 pages). These include the main introductory diagrams, calibration tables, numerical figures and selected appendix problems. **This does not certify every equation, every visual or the numerical replication.** Remaining equation/layout verification and independent reproduction are pending. Extraction scrambles fractions, exponents and sums, so raw extracted equations must not become training answers.

User-attested permission covers private training; no public redistribution or independently established open license is claimed. No new training records or model job were created in this review.

## What the paper contributes

The paper builds a stylized economic model of payments, mining incentives, costly delay and double spending. Its useful contribution to our knowledge base is reasoning about assumptions and trade-offs in network fundamentals. It supplies neither a candlestick strategy nor evidence of out-of-sample trading profitability.

| PDF pages | Material and project treatment |
|---|---|
| 1–5 | Identity, motivation and main results. Preserve the 2018 version and authorship; the views disclaimer means this is not an official Bank of Canada investment recommendation. |
| 6–13 | Ledger and double-spending explanation, mining/value/security feedback diagrams. Useful educational abstractions; clarify that protocol security does not guarantee asset price or custody safety. |
| 14–20 | Single-period model, independent mining contests, competitive-miner limit and attack incentives. Every formula requires the stated assumptions and units; do not translate a sufficient model condition into an operational guarantee. |
| 21–28 | General equilibrium, day/night markets, preferences, rewards and optimal funding. Day/night are model stages, not trading sessions. Zero fees as an optimum is conditional on this model, not a universal protocol-design rule. |
| 29–34 | Calibration and counterfactual numerical results. Uses 2015 Bitcoin inputs, a 2013 transaction-size source and 2014 payment-system inputs. Separate observed input summaries from simulated outputs. |
| 35–38 | Limitations, conclusions and references. The paper explicitly omits some infrastructure costs and scalability constraints. References are leads, not independently reviewed sources. |
| 39–55 | Mining microfoundation and proofs. Mathematical reading completed at extracted-text level; selected appendix issues checked visually. Independent proof/replication audit not completed. |
| 56–57 | Abstract balance-ledger formulation. Do not present its account-style notation as the literal Bitcoin UTXO implementation. |
| 58–60 | Stylized proof-of-stake extension. Long-range attacks are excluded by assumption and consensus problems remain outside the model. It is not a specification of present-day Ethereum or every PoS chain. |

## Corrections, caveats and unresolved checks

1. **Version mismatch matters.** The [Bank of Canada publication page](https://www.bankofcanada.ca/2019/09/staff-working-paper-2019-40/) identifies a September 2019 working paper. Its abstract reports an optimal-design equivalent inflation around 45%; the uploaded 2018 draft's PDF page 33 reports 27.51%. Keep versions separate. The later PDF has not been fully compared; no cause of the change is asserted.
2. **Chain selection, page 8.** The book analogy and “longest” shorthand are useful only with qualification. Bitcoin selects a valid chain by accumulated work; block count alone is insufficient. The [Bitcoin RPC reference](https://developer.bitcoin.org/reference/rpc/getblockchaininfo.html) describes the most-work fully validated chain and its chainwork field. Miners cannot override transaction validity merely by proposing a block.
3. **Finality, pages 11–20.** Winning N+1 consecutive contests and the no-double-spending inequality describe this attack model. Economic deterrence of a modeled rational attacker is not impossibility of all attacks. [Bitcoin payment documentation](https://developer.bitcoin.org/devguide/payment_processing.html) retains double-spend risk considerations, including attacks and implementation bugs, despite confirmations. Do not offer a universal confirmation count or guarantee.
4. **Mining profits, pages 15–16.** Full reward dissipation is a limiting result with symmetric competitive miners and the specified costs. It does not establish that each actual miner has zero profit or identical equipment, energy prices and access to capital.
5. **Monetary policy, pages 27–28 and 50–55.** The model favors financing rewards through issuance instead of transaction fees. This is a conditional welfare result with a specific objective and constraints. It neither instructs a real network to change policy nor establishes which token will appreciate.
6. **Reused symbol, page 29, visually confirmed.** Tau labels both a transaction-fee fraction and average transaction size. The latter calculation is about 2.08666 BTC per transaction; it is not a fee fraction. Preserve separate semantic field names in any future dataset.
7. **Time-unit inconsistency, pages 29–30, visually confirmed.** Page 29 describes sigma=0.0178 as the fraction spent per day; Table 5.2 calls it velocity per ten-minute block. Using the listed daily volume divided by supply gives approximately 0.01777; dividing the per-block volume by supply gives approximately 0.0001234. This supports the daily reading for those inputs, but does not resolve the original implementation. Hold numerical replication until checked.
8. **Prose versus plotted consumption, pages 30 and 32, visually confirmed.** The prose says the effect on consumption and utility is positive. Figure 5.3's aggregate-consumption curve largely falls over the displayed range, while utility rises. Flag rather than silently teach a single directional claim. Page 30 also refers to Figure 5.2 where the money-growth plot is labeled Figure 5.3.
9. **Historical counterfactuals, pages 32–34.** Welfare losses, mining costs, equivalent inflation and equivalent fees are model estimates, not observed trading returns or current fee schedules. Equivalent fee is not simply mining cost divided by annual transactions; the prose defines it through welfare indifference. Address-based and entity-based transaction counts in page 31 are also distinct measures.
10. **Appendix editorial and mathematical flags, visually confirmed.** Page 51 retains an editorial COMMENT footnote and calls a constraint old-policy while displaying subscript 1. Page 53 equation A.36 introduces an extra sigma inside the consumption-cost term compared with A.35. Page 54 A.44 claims the expression exceeds mu_0−1 even though the preceding expression scales with an arbitrarily small positive xi; that stronger lower bound needs correction/verification. The underlying positivity argument may survive a corrected bound. These observations do not by themselves refute the full proposition.
11. **PoS scope, pages 58–60.** The appendix's zero-delay result depends on its particular participation/reward assumptions and exclusion of long-range rewriting. The authors themselves leave other consensus problems unresolved. No modern-chain security claim is accepted from this section without separate protocol evidence.

## Reusable knowledge notes

These are review notes, not new SFT examples or a passed evaluation.

| Question | Accepted project answer | Trace |
|---|---|---|
| Does more secure settlement guarantee price appreciation? | No. Settlement security and market valuation are different questions; the feedback mechanism here is a modeled relationship, not a return forecast. | DP21 pp. 11–13, 21 |
| What must accompany a numerical research claim? | Document/version, data period, variable definitions, units, assumptions and whether it is measured or simulated. | DP21 pp. 29–35 |
| Are day/night markets literal crypto market opening hours? | No; they organize stages of the theoretical economy. | DP21 pp. 21–24 |
| Are fees and currency issuance economically identical? | Both can fund rewards but can create different distortions in a given model; the paper's ranking is conditional. | DP21 pp. 27–28 |
| Can its settlement inequality be used as a universal safety rule? | No. It belongs to a specified strategic model and omits other failure modes. | DP21 pp. 14–20, 58–60 |
| Is a 2018 number interchangeable with a 2019 result? | No. Cite the actual version and investigate the change before merging results. | DP21 p. 33; linked 2019 abstract |
| Does this PDF provide multi-coin forecasting labels? | No. Payment-economics calibration is not a time-aligned asset-return training dataset. | DP21 pp. 29–35 |

## Disposition and next review steps

**Keep as a selective, dated fundamentals/research-methods source. Do not ingest wholesale.** Hold raw equations, unresolved numerical inconsistencies and universalized security/design statements. Before numerical curriculum use: render remaining relevant equations, compare against the official 2019 version, obtain or reproduce the calculation with correct units in an authorized cloud runtime if fitting/calibration is involved, and keep provenance for any correction.

For the broader library, DP15 and DP18 substantive reading and most of DP16 remain outstanding, along with unverified visuals in other works. The scope ledger and module-specific reviews must be read together; example counts are not page-review coverage. Reading these files builds an external project reference. It does not permanently modify the assistant's weights or certify trading expertise.
