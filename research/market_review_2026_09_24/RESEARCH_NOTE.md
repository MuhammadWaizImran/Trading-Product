# Binance market review — 24 September 2026

Decision at snapshot: **wait; no immediate entry established**. Shortlist for an educational, conditional paper setup: SOLUSDT perpetual. Longer-term spot research watchlist: BTC; no spot entry recommendation established. This comparison covers BTC, ETH and SOL, not all listed coins. No order/account APIs were used. No model fitting or inference was used, and this note is not evidence that the project's model is an expert.

## Reproducible market evidence

Snapshot retrieved 05:54:21 UTC / 10:54:21 Pakistan time. Exchange server timestamp: 05:54:18 UTC. Raw payloads in `public_snapshot.json`, deterministic calculations in `summary.json`; fetch/indicator source: `scripts/public_market_review.py`. GET requests only to Binance public USD-M market endpoints: `/fapi/v1/time`, `/exchangeInfo`, `/ticker/24hr`, `/premiumIndex`, `/ticker/bookTicker`, `/openInterest`, `/klines`.

Fetched 250 candles for each of three intervals (1h, 4h, 1d) for each asset: 2,250 rows. Each series had 249 closed candles at retrieval; forming candles were excluded from indicators. Checked OHLC ordering, contiguous open times and interval-close timestamps. EMA uses an initial N-close SMA then alpha=2/(N+1); RSI/ATR use Wilder smoothing with 14-period initialization. ATR starts with the first prior-close-aware true range. Volume ratio compares latest closed bar with the preceding 20-bar mean. No strategy backtest was performed. EMA200 has limited warmup and is not used for the setup.

| Metric | BTCUSDT | ETHUSDT | SOLUSDT |
|---|---:|---:|---:|
| Last traded, USDT | 84,135.90 | 2,686.80 | 115.07 |
| Rolling 24h change | -2.721% | -2.630% | -2.780% |
| Rolling futures quote volume | 16.95bn | 11.42bn | 2.63bn |
| Closed 1h EMA20 / EMA50 | 84,612.92 / 84,894.27 | 2,691.06 / 2,705.49 | 115.43 / 115.88 |
| Closed 1h RSI14 | 36.81 | 42.05 | 47.24 |
| Closed 4h RSI14 | 50.70 | 49.11 | 51.91 |
| Closed daily RSI14 | 65.46 | 63.26 | 63.60 |
| Returned last funding rate | +0.004973% | +0.007853% | +0.005801% |
| Minimum order notional filter | 50 USDT | 20 USDT | 5 USDT |
| Quantity increment/minimum | 0.001 BTC | 0.001 ETH | 0.01 SOL |

Both quantity increments and minimum notional matter. At snapshot prices the smallest compliant opening quantities imply approximately 84.14 USDT BTC, 21.49 USDT ETH (0.008 ETH), and 5.75 USDT SOL (0.05 SOL). These are not margin requirements; leverage does not reduce the underlying exposure. Other venue/account filters and available balance can still prevent an order. Futures filters do not establish spot filters.

The 1h bars close at 04:59:59 UTC, 4h bars at 03:59:59 UTC, and daily bars at September 23 23:59:59 UTC. All three latest closed daily prices exceed their EMA20/EMA50, but latest 1h closes are below those shorter-timeframe averages. Interpretation: intraday weakness within a stronger daily structure, not a confirmed continuation in either direction. One open-interest snapshot cannot establish whether positions are increasing or decreasing. One positive funding observation cannot forecast price.

## Fundamental comparison and source register

Sources accessed September 24, 2026. Official project material is authoritative about intended mechanics, but adoption claims remain issuer-reported unless independently verified.

- **BTC:** fixed-issuance monetary design and a maximum supply under current rules; fractional ownership means a high unit price does not exclude a small spot investment. Supply limits alone do not ensure price appreciation. [Bitcoin FAQ](https://bitcoin.org/en/faq). Preference for BTC as the first spot research candidate here is a judgment based on its simpler monetary thesis and the largest observed futures turnover in this three-asset sample, not a forecast or comprehensive valuation.
- **ETH:** pays network gas and secures Ethereum through staking. [Ethereum's ETH overview](https://ethereum.org/what-is-ether/), marked updated August 6, 2026. Application activity has an economic use for ETH, but this review has not quantified current net issuance, fee capture, valuation or competitive effects. The futures minimum is unattractive for a 10 USDT unlevered experiment.
- **SOL:** transactions require SOL fees, and staking participates in network security. [Fee documentation](https://solana.com/docs/core/fees), [staking/inflation documentation](https://solana.com/staking). Ongoing issuance means staking yield is not pure economic profit. The exact current issuance rate and governance changes were not independently measured here.
- **Adoption context:** Solana's [August ecosystem roundup](https://solana.com/news/solana-ecosystem-roundup-august-2026), published September 4, reports growth in payments and tokenized assets. Useful contextual leads, not independently reproduced revenue or token-price evidence. No near-term bullish catalyst has been validated for the proposed setup.
- **Reliability:** the [status page](https://status.solana.com/) reported operational mainnet/RPC and no incident today when checked. The Foundation's [September 14 resilience article](https://solana.com/news/solana-building-trust-in-public) discusses an August infrastructure stress event and future improvements. Operational status is not a guarantee against outages; announced future upgrades are not already-delivered capabilities.
- **Trading costs:** [Binance fee explanation](https://www.binance.com/en/support/faq/detail/98488a516eb84e3eb34605683dffd554) explains commission on notional. The [account fee page](https://www.binance.com/en/fee/futureFee) returned no rate table to this session; the user's actual fee tier is unverified. Calculations below use an explicit illustrative 0.05% per side, not an authenticated account rate.
- **Funding:** [Binance funding glossary](https://www.binance.com/en/academy/glossary/funding-fees) distinguishes positive funding (longs pay shorts) from negative. Rates and settlement intervals must be refreshed before interpreting future carrying cost.
- **Market source:** [Binance exchange information](https://fapi.binance.com/fapi/v1/exchangeInfo), [SOL ticker](https://fapi.binance.com/fapi/v1/ticker/24hr?symbol=SOLUSDT). These links change; retained JSON is the evidence for this snapshot. An earlier web-cached ticker differed slightly; final numbers consistently use the directly fetched synchronized snapshot.

Missing for complete investment due diligence: independently checked unlock/concentration data, current circulating valuation, protocol revenue, event calendar, cross-venue liquidity and account-specific fees/eligibility. No claim that SOL is the best coin across the crypto market or that this is a complete valuation.

## SOL technical map

1h EMA20 115.43, EMA50 115.88, RSI14 47.24 and ATR14 1.1642. Latest hour's volume was 0.345 times the previous 20-hour mean: no strong breakout confirmation. The recent local low is 114.01, with the broader pullback low 112.80. Recent highs 117.68 and 118.28 are intermediate resistance; the recent daily/4h high is 119.99.

4h EMA20 115.09 and EMA50 111.26, RSI14 51.91 and ATR14 2.2096: mixed/neutral near-term structure. Daily EMA20 106.51, EMA50 97.70 and RSI14 63.60 support the interpretation of a pullback within a stronger daily trend. These indicators describe history; no calibrated probability is available.

## Conditional paper-only long example — inactive

Hypothesis: a recovery through 116 followed by a held retest could revisit the earlier highs. The preference for a long after confirmation avoids assuming that an intraday decline has already reversed. It is not a tested trading edge.

All conditions must hold:

1. A future fully closed 1h SOL candle closes above 116.20, with base volume at least 1.2 times its preceding 20 closed hourly bars' average. This threshold is an unvalidated research rule, not an empirically optimal parameter.
2. The latest closed 4h SOL candle is above its freshly calculated EMA20. BTC must not have subsequently closed a 1h candle below 83,450.10; otherwise discard this scenario and reassess the market.
3. Within the next two hourly bars, price retests 115.90–116.10 and the retest hour closes at or above 116.00. Only after that confirmation, simulate a limit entry at 116.00 if price returns again. No fill is assumed from a mere touch. If the following hour does not supply a fill, cancel. Do not chase a higher price using the same reward/risk calculation.

| Paper parameter | Value |
|---|---:|
| Side | Long, conditional only |
| Assumed entry | 116.00 USDT |
| Stop trigger | 114.40 USDT |
| Single take-profit | 119.80 USDT |
| Quantity | 0.05 SOL |
| Entry notional / simulated 1x margin | 5.80 USDT |
| Remaining theoretical 10 USDT balance before costs | 4.20 USDT |
| Gross stop loss | 0.0800 USDT |
| Gross target gain | 0.1900 USDT |
| Stop loss including illustrative fees | 0.08576 USDT |
| Target gain after illustrative fees | 0.184105 USDT |
| Gross / fee-adjusted reward:risk | 2.375 / approximately 2.147 |

Funding and slippage are excluded, so actual outcomes could be worse, including a stop fill beyond the trigger. Initial stop distance is about 1.37 hourly ATR; it may still be hit in ordinary volatility and sits above the recent 114.01 swing low. This tighter stop is a retest-failure hypothesis, not protection below the whole swing. 117.68/118.28 resistance can prevent target attainment. Do not widen the stop or add to losses. One full-position TP avoids assuming very small partial exits satisfy exchange rules.

Invalidate the untriggered snapshot setup six hours after retrieval (11:54 UTC / 16:54 Pakistan time on September 24). An entered paper position has a maximum 24-hour holding window; record a simulated market exit and costs if neither level occurs. No automatic monitoring is active. If both stop and target lie inside a historical bar, do not invent favorable ordering; obtain finer data or mark the outcome ambiguous.

With 10 USDT, even this successful illustration produces roughly 18 cents before funding/slippage. A 10% unlevered gain on the full 10 USDT is only 1 USDT before costs. Seeking several dollars per trade from this balance requires much larger percentage exposure and loss risk. The present recommendation is to preserve the balance and paper-test; no personal live futures order is recommended.
