# Product Brief: AI Crypto Research and Monitoring Assistant

## Product vision

I want a personal AI assistant that continuously researches cryptocurrency markets, discovers potential trading opportunities, evaluates them thoroughly, and explains its findings to me in plain language. It should feel like a knowledgeable research partner I can speak with naturally, rather than a dashboard that only displays indicators or sends fixed messages.

The product should support informed decisions, not promise guaranteed profits or claim that it can know which coin will pump.

## Intended user

The primary user is a retail trader with limited trading knowledge who uses Binance Futures and may have a small account. The assistant should explain unfamiliar concepts, distinguish potential profit from likely outcomes, and make the downside as clear as the upside. It must not pressure the user to trade or increase leverage to reach a financial target.

## What the product should do

### 1. Continuously discover cryptocurrency opportunities

- Monitor cryptocurrency markets around the clock and identify candidates worth investigating.
- Cover a broad range of coins, including smaller projects, rather than restricting research to Bitcoin and Ethereum.
- Clearly identify the markets and coins it actually covers; do not imply that every cryptocurrency is monitored.
- Consider market activity, price and volume changes, liquidity, new listings, project developments, news, upcoming events, and relevant on-chain activity.
- Look for developing opportunities, not simply lists of coins that have already risen sharply.
- Explain why a coin was shortlisted and what additional evidence is needed.

### 2. Perform fundamental research

Evaluate relevant aspects of a project, including:

- Purpose, utility, technology, and competitive position.
- Team, development activity, adoption, and verifiable partnerships.
- Token supply, distribution, emissions, unlocks, and concentration.
- Relevant announcements, catalysts, governance decisions, and major risks.
- Signs of manipulation, misleading promotion, or unreliable information.

Separate verified facts, project claims, and the assistant's interpretation. Distinguish proposed changes from approved or implemented changes.

### 3. Perform technical and futures-market analysis

- Assess price action, trend, market structure, candlestick and chart patterns, indicators, volume, and liquidity across relevant timeframes.
- Consider futures-specific conditions, including funding, open interest where available, leverage exposure, and liquidation risk.
- Use broader market conditions to put an individual coin's movement in context.
- Explain conflicting signals and avoid treating a pattern or indicator as a guarantee.

### 4. Present understandable opportunity assessments

When evidence supports a potential setup, provide:

- Coin, trading pair, venue, and analysis timestamp.
- A potential long or short scenario, or a clear no-trade conclusion.
- The reasoning and sources supporting the assessment.
- Entry conditions and the intended trading horizon.
- Invalidation conditions, a stop-loss scenario, and potential targets.
- Position-sizing and leverage-risk explanations appropriate to the account information available.
- Estimated profit and loss scenarios, with assumptions about fees, funding, spread, and slippage stated clearly.
- Important uncertainties, missing information, and circumstances that would cancel the setup.

Potential returns must be presented as conditional scenarios, not promised earnings. The assistant should ask for missing account or position information instead of inventing it. It should reject unsuitable setups rather than force a trade to produce an alert.

### 5. Remember and revisit coins

The assistant must not analyze a coin once and forget it.

- Maintain an ongoing watchlist and a history of previous assessments.
- Remember why a coin was shortlisted, rejected, or placed on hold.
- Reassess coins periodically and when relevant new information appears.
- Allow a previously rejected coin to become a candidate when conditions change.
- Explain what changed since the previous assessment.
- Withdraw or revise an earlier opportunity when its supporting conditions no longer hold.
- Let the user request continued monitoring of a particular coin.

### 6. Provide useful alerts and natural conversation

- Notify the user when an opportunity meets the agreed criteria after analysis.
- Support email and phone-call notifications in the intended complete product.
- Allow natural, two-way voice conversations about the latest findings, risks, assumptions, and previous assessments.
- Answer follow-up questions dynamically rather than reading a fixed script.
- Support English and Roman Urdu explanations.
- Track acknowledgements so reminders stop when the user responds.
- Provide user-controlled reminder intervals, retry limits, quiet hours, snooze, and opt-out options.
- Stop reminders when an opportunity expires or is invalidated, even if the user has not acknowledged it.
- Avoid presenting an old assessment as a fresh opportunity merely because the user answers a call later.

### 7. Make research transparent

- Show the source and age of consequential information.
- Identify stale, unavailable, contradictory, or insufficient data.
- Explain why an assessment changed.
- Keep previous alerts and assessments available for review.
- Make monitoring interruptions and coverage limitations visible.
- Do not present unsupported confidence percentages or invented facts.

## Educational material

The user has supplied cryptocurrency and trading PDFs covering beginner through advanced concepts. This material is intended to inform the assistant's educational understanding. It must not be treated as evidence of current market conditions or as proof of profitable forecasting ability.

The user has attested permission for private model training. This does not imply permission to publicly redistribute the documents. Private material should remain private.

## Scope and boundaries

- The initial product is for cryptocurrency research and simulated/paper trading.
- Binance Futures is the user's preferred context for trading assessments.
- Automatic real-money order placement is outside the authorized product scope.
- Continuous monitoring is a requirement for the intended complete product, not a claim about current capabilities.
- The assistant must be able to conclude that no suitable opportunity exists.
- It must not promise pumps, guaranteed profit, or a fixed return within a deadline.
- It should remain useful when opportunities fail by documenting invalidation, mistakes, and lessons rather than hiding unsuccessful assessments.

## Desired experience

The user should be able to say:

> “Monitor the market, find coins worth researching, explain the fundamentals and trading conditions, keep revisiting them, and notify me when there is a well-supported opportunity. When I answer, discuss it with me naturally and explain both the possible reward and what could go wrong.”

## Current project status

The complete product described above has not been built. Existing work consists of selected PDF-derived model-training experiments and development evaluations. Broad cryptocurrency expertise, reliable coin discovery, profitability, and readiness for deployment have not been established. Continuous monitoring and conversational phone/email alerts remain intended capabilities.

This document defines what the product should be. It intentionally does not prescribe an architecture, technology stack, model choice, or implementation method.
