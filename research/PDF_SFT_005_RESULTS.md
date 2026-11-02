# PDF SFT 005 — cloud run result

Run 005 completed on Kaggle on 21 September 2026 and is preserved as a **failed quality-gate result**. Execution succeeded; promotion did not.

- Private Kaggle job: `waizimran/crypto-qwen3-pdf-sft-005`, version 1
- Parent: run 004 adapter `ab4250c6d48025e12c16aec4e35e54b9bf6a7fab6fec46ce44bdc70e2659dda3`
- New adapter: 15,354,512 bytes, SHA-256 `66f06ca285084ea39ea4b66959a4305f591576651ce2b8b2f1fd094fb960fc89`
- Runtime: Tesla T4, CUDA 12.8; one epoch, 24 optimizer steps, 306.7699 seconds
- Validation loss: 3.371198 before to 3.189449 after
- Data: 96 train, 16 validation, 16 test; 24 new DP03 training examples
- Cloud and local manifests match. Adapted and reloaded answer files are byte-identical, SHA-256 `5ce25777bb5bc01deec343dd7e3d6a56749b51181a290b97338c31c1fa6482e7`.

## Predeclared fresh-test review

1. Address count: **partial**. It says one person can control multiple addresses but omits the required converse that a custodial address can represent multiple people.
2. Consensus versus reserves: **pass**. It correctly says transfer consensus is not proof of reserves or redemption capacity.
3. Conjoint survey versus return: **fail**. It rejects direct return prediction but invents an unstated `0.75` coefficient and does not explain the study baseline/design required by the rubric.
4. CBDC bank-run channel: **pass**. It treats the effect as conditional on design, accessibility, remuneration and integration rather than inevitable.

Only two of four answers pass, below the required three. Retention also worsened: the NOBI answer invents both a regression interpretation and statistical significance at 5%, and the RSI answer repeats itself. The adapter therefore is not an acceptable parent for DP04 despite lower validation loss.

The corrective run must restart from accepted adapter 004, add explicit training examples for the observed failure modes, and use a newly frozen DP03 test set. Run 005 questions are now exposed and cannot serve as independent promotion evidence again.
