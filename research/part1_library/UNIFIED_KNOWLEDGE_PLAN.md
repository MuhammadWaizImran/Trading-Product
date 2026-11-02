# Unified knowledge and dataset plan — Part 1

This is an original research specification, not a trained model, completed corpus, or validated trading strategy. Source IDs refer to RESOURCE_CATALOG.csv. Model choices in the older blueprint remain provisional while research continues. All future fitting must take place on an authorized cloud platform; no training is performed in Part 1.

## How the materials serve different purposes

Books and lessons explain concepts. Rights-cleared documents can later support source-linked retrieval, so the product can consult and cite evidence. Restricted material stays a human reading reference. Price histories measure whether a proposed signal survives real outcomes. Original chart annotations connect visual shapes to numerical definitions. These are different datasets and should never be mixed into an indiscriminate training dump.

The eventual research output needs: asset, venue, observation time, forecast horizon, evidence for and against a hypothesis, information gaps, conditional invalidation, liquidity/cost assumptions, and a justified wait decision. A confident explanation is not evidence of predictive skill.

## Curriculum and coverage

| Module | Required concepts | Starting references | Required skepticism or missing evidence |
|---|---|---|---|
| Crypto foundations | Keys, custody, consensus, transactions, chains, tokens | R01, R02, R05, E01–E04 | Historical designs can differ from current implementation |
| Market mechanics | Spot, perpetuals, margin, funding, mark/index price, liquidation, CEX/DEX | D01, R25, R27; playlist named futures/exchange lessons pending | Current contract specifications and liquidation mechanics require separate official verification |
| Candlestick literacy | OHLC, bodies, wicks, doji, marubozu, hammer, engulfing, harami, multi-candle patterns | R06, R08, R13, R18, R21; price-action classes 1–3 pending | Shape labels require explicit thresholds; exchange timezone changes candles |
| Chart patterns | Double/triple tops and bottoms, head/shoulders, triangles, flags, pennants, wedges, rectangles | R10, R11, R15, R19 | Add failed breakouts and ambiguous shapes; no automatic transfer of stock statistics |
| Price action and structure | Swing highs/lows, trend/range, support/resistance, trendlines, breakout/retest | R06, R08, R19; price-action classes 4, 6, 10 pending | Swing confirmation can use future bars; specify availability time |
| Supply and demand zones | Zone boundaries, repeat tests, invalidation, overlap | Price-action classes 7–9 pending; cross-check R08, R19 | A drawn zone does not directly establish resting orders or institutional intent |
| Indicators | SMA/EMA, RSI, MACD, stochastic, ATR, Bollinger bands, ADX, OBV, VWAP | R06, R07, R09, R13 | Parameter and warmup definitions; lag; venue-specific volume; redundant signals |
| Fundamentals | Token utility, supply, emissions, unlocks, governance, fees/revenue, adoption, security | E01–E07, R25, R29; fundamentals video pending | Primary project disclosures and dated unlock histories still need asset-specific collection |
| Liquidity and execution | Spread, depth, impact, slippage, fragmented venues, MEV | D01–D03, R27–R30 | Candles cannot establish fill quality; sparse free order-book samples limit evidence |
| Manipulation and narrative | Pump/dump, wash trading, conflicts, misleading attention metrics | E09, E11, R26 | Do not make accusations about individual assets without direct evidence |
| Risk and abstention | Loss limits, leverage, liquidation, portfolio concentration, expected value, no-trade criteria | R16, R17, E13 | Reward/risk alone omits probability and transaction costs |
| Research discipline | Baselines, time splits, overfitting, multiple comparisons, uncertainty | E10–E13, R03, R04, R22–R24 | Favorable historical results require contrary evidence and independent replication |

## Consistent terminology

Use a canonical concept ID and retain each author's alternative names. Separate geometric observations from interpretations and return forecasts. A long lower wick is observable; a claim that buyers absorbed institutional selling is an interpretation requiring additional evidence. “Break of structure” and “change of character” need declared swing and confirmation rules, rather than assumed universal definitions.

For crypto, define UTC or another explicit candle boundary, base/quote units, spot versus derivative instrument, and exchange. A 24/7 market does not inherit equity session-gap assumptions. Compare volume only after checking denomination, venue coverage and credibility. Keep live candle values separate from finalized candles. A retrospective pivot becomes available only after its confirming bars arrive.

## Dataset preparation specification

1. **Source intake:** assign ID; save exact URL, publisher, edition, retrieval time, content hash, rights reference, allowed use and access status. Unresolved permissions default to hold. Do not ingest third-party charts merely because their parent page is free.
2. **Educational text:** only after rights clearance, extract structure; preserve headings and page/timestamp references; remove navigation and promotions; deduplicate exact and near-duplicate explanations; retain attribution. Do not strip qualifications or convert a teacher's claim into an established fact. This phase has not extracted or indexed downloaded PDFs.
3. **Multilingual lessons:** preserve original Urdu/Hindi wording alongside an independently checked English concept mapping. Identify uncertain audio, financial terms and translation ambiguity. Do not generate plausible transcripts for inaccessible videos.
4. **Numerical history:** retain raw immutable files and checksums; normalize timestamps and units; check sortedness, duplicates, missing bars, OHLC consistency and nonnegative volumes. Flag missing data rather than fabricating price moves. Record listing/delisting dates and include failed assets when coverage permits.
5. **Original chart examples:** later generate our own views from permitted numerical data, with time and price axes, asset, venue, timeframe, and observation cutoff. Record candidate pattern bounds and rule version. Include positive, negative, failed and ambiguous examples, not only textbook successes. Synthetic diagrams teach geometry only and must be labeled synthetic.
6. **Ground truth:** distinguish a human pattern annotation from a future-return outcome. Define horizon and cost assumptions before inspecting outcomes. Preserve when each fact actually became public. Use event-time and availability-time separately for news, unlocks and on-chain revisions.
7. **Dataset partitioning:** keep adjacent and overlapping windows together; use chronological splits with horizon-aware purging. Reserve unseen periods and assets where feasible. Keep source-derived evaluation questions out of adaptation data. Training, tuning and evaluation execution belong to Part 2 in the cloud.

## Suggested record formats

**Knowledge claim:** claim_id, concept_id, short_original_paraphrase, claim_type (definition/hypothesis/empirical_result), source_id, locator, publication_time, retrieval_time, rights_status, applicable_market, counter_evidence, confidence_basis, review_status.

**Chart annotation:** example_id, asset, venue, instrument, timeframe, start/end, observation_cutoff, raw_data_hash, rule_version, pattern_candidate, geometry, trend_context, volatility_context, volume_context, annotation_confidence, annotator, ambiguity_reason, confirmed_at, future_outcome_separate_reference.

**Market record:** instrument_id, event_time, available_time, OHLCV, volume_units, venue, source_version, quality_flags. For derivatives add funding interval and contract details from verified provider specifications; missing fields stay missing.

## Initial selection and unresolved gaps

Prioritize licensed protocol documentation (E01–E04, R27 with item checks), source-linked human references for technical analysis, and transparent numerical definitions from TA-Lib. Treat downloaded PDFs as a reading shelf, not an ingestible corpus. Keep noncommercial resources outside a prospective commercial product unless a suitable license is obtained.

The current strongest missing pieces are complete spoken-content review of both user playlists; timestamped independent chart annotations; broad delisted-asset history; continuous multi-venue order-book history; dated funding/open-interest and token-unlock records; news publication-time datasets with clear rights; and permission-cleared modern technical-analysis text. A larger link count does not resolve these gaps.

Part 1 should close only after these requirements have a documented source, a feasible bounded alternative, or a clearly accepted limitation. No performance claim or transition to training follows from this catalogue alone.
