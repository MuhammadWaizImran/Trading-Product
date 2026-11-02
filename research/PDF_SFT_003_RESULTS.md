# PDF SFT 003 — cloud run result

Run 003 completed on Kaggle on 21 September 2026 and is preserved as a **failed quality-gate result**. Execution succeeded; promotion did not.

- Private Kaggle job: `waizimran/crypto-qwen3-pdf-sft-003`, version 1
- Model: `Qwen/Qwen3-8B`, exact revision `b968826d9c46dd6066d109eabc6255188de91218`
- GPU/runtime: Tesla T4, CUDA 12.8
- Parent adapter: run 002, SHA-256 `8e111a2cb193b246ca1fd1c6e4a1c181d8d439d636193a8a5b6c401f5ba561e2`
- Run 003 adapter: 15,354,512 bytes, SHA-256 `a2d3bc952bc6fc9816c351d7ca9ed50a65dee1789257368950b13925330db470`
- Data: 72 train, 12 validation, 12 test; 24 new DP01 training examples
- Training: two epochs, 36 optimizer steps, 447.0246 seconds
- Validation loss: 3.792656 before training to 3.089774 after training
- Adapted and reloaded answer files are byte-identical: SHA-256 `1569b629229f24a7f8dc49c74be3ebee2eaf3728598fd1fd20f412c4622eff61`
- The downloaded cloud manifest exactly matches the frozen local manifest.

## Human review

The four new DP01 checks did not provide a clean 3-of-4 pass:

1. Average block interval: **pass**. It correctly says a 24-minute block does not contradict an approximately ten-minute target, although it could explain stochastic intervals more precisely.
2. Fixed supply and falling demand: **partial/fail for promotion**. It correctly says the exact price is undetermined but introduces an unjustified rule that price equals the old price multiplied by a demand ratio and then incorrectly says the demand change was not given.
3. Oracle boundary: **pass**. It correctly separates ledger consensus from truth of a weather feed.
4. Addresses versus people: **partial**. It covers one person using multiple addresses but omits the equally important case where one custodial address represents many people.

Retention checks expose additional weaknesses. The adapter repeats an answer until the 192-token limit on the acquisition-cost question, invents a false expansion and formula for NOBI, and calculates expected value as `4R - 1R` without probabilities. The holder-count response also adds `400 + 5 = 405` as an address count even though the scenario describes one exchange address plus five addresses. Some of these errors existed in the parent, but the repetitive truncation is new.

The lower validation loss therefore does not justify promotion. This adapter is not approved as the parent for DP03. The next action is a corrective, lower-intensity DP01 run from adapter 002, evaluated with newly written held-out DP01 questions because the original four have now been inspected. This remains educational SFT evaluation; profitability and general crypto expertise have not been demonstrated.
