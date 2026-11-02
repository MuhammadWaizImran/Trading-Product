# PDF SFT010 results ? completed, not accepted (2026-09-29)

Kaggle confirms complete. The bounded monitor downloaded results and passed the structural audit. Cloud status is completed_training_human_evaluation_pending. All50 baseline and50 adapted answers were read; the50 reloaded responses are exactly equal to the adapted responses under the artifact audit. No baseline/adapted answer hit the generation limit. No local model execution occurred.

## Measured training

- GPU: Tesla T4;278 training,42 validation,50 development test records.
- One epoch; fitting2818.42 seconds (46.97 minutes).
- Validation loss5.56494 before and3.48799 after. Lower loss does not establish grounded accuracy.
- Adapter SHA256:48d2664db5b46246ee98bfd688318b2d28a6f14be0a10892117c6303ca5fc8bf.
- Saved/reloaded adapter produced identical answers. This establishes persistence, not financial skill.

## Observed improvement

The adapter correctly calculates exposure/equity as4 for equity250 plus borrowing750; base incorrectly copies the passage's10x example. The adapter correctly disallows a sell-limit240 fill at235; base contradicts itself by initially permitting it. The adapter omits the required citation in the latter answer, so it is not a full grounded-answer pass. Both models answer the affirmative offline-receiving probe correctly with relevant evidence. Prompt-only improvement and adapter gains must remain separate.

## Remaining failures

- test-overbought: both begin Yes to a question asking whether high RSI with rising price is inconsistent, then explain it is not inconsistent. Contradictory polarity remains.
- dp07-test-counterparty: both cite cold-storage evidence to justify ownership reasoning; that passage does not establish the claim. Adapter adds unsupported partnership/strategic-move explanations.
- r009-unknown-normalization: both incorrectly assign a known midpoint convention to an unidentified report. Other unidentified-source cases also misinterpret source identity; the survey answer even suggests1000 per country could mean1000 total. The explicit source gate remains necessary.
- test-depth-impact and dp04-test-signing: both use source labels or altered capitalization instead of valid supplied evidence IDs.
- Adapter omits citations on r009-ownership-evidence, r009-sell-direction and r009-missing-study.
- dp05-expanded-test-doji: adapter adds volume and other indicators as necessary to determine reversal probability, although the cited passage does not establish that procedure.
- dp16-test-availability: adapter introduces uncertainty about satisfying all goals even though failure of availability already rules it out, then eventually answers No.

## Six new development probes

All three supported probes have the correct substantive conclusion in both models. The adapter's VWAP irrelevant-evidence answer appropriately identifies insufficient evidence. Its offline-receiving irrelevant answer starts No before explaining insufficiency, risking a false factual rejection; its ADX irrelevant answer invents a comparison between ADX and exchange-address classification before acknowledging missing evidence. These fail the strict clean-abstention target. No aggregate semantic accuracy percentage is claimed from this qualitative review.

## Decision and next work

No promotion; overall training is not certified complete. Do not simply repeat epochs. Private broad-check011 compares adapter010 against the same-prompt base with explicit source routing on100 grouped cases (50 model calls and50 deterministic routes per model). It reuses exposed broad010 development scenarios; this is regression testing, not independent final acceptance. Its results will establish whether these repairs carry across the broader curriculum in the intended evidence pipeline before selecting further model changes.

Full-library review, independent acceptance, and market-data/paper-trading evaluation remain separate unfinished requirements. This run does not establish chart-image reading, coin discovery or profitable trading.
