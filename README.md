# Crypto research workbench

**Latest: checked-answer source selection and exact limit-price rules are integrated in the offline workbench;27 tests and browser checks passed. Model generation remains unapproved. See [integration and manual steps](research/CHECKED_ANSWER_INTEGRATION.md).**

**Part 2 is in progress. The full model and product are not complete.** Nine limited Qwen3-8B PDF fine-tuning runs finished on Kaggle, but evaluation found serious errors and no demonstrated reliable adapter improvement. No model is approved for research decisions or paper trading.

## Run the offline workbench

From this project directory in PowerShell:

```powershell
python -m workbench.server
```

Open http://127.0.0.1:8765. Stop the server with Ctrl+C. The workbench uses Python's standard library and existing private local files; it does not train or run a model. Keep the server bound to localhost.

- Search 100 checked PDF-derived adaptations from seven PDFs, with page references and source-file hash checks.
- Inspect historical BTCUSDT/ETHUSDT daily candles, using only observations through the selected UTC day.
- Calculate hypothetical position sizing, payoff break-even and explicitly defined order-book imbalance.
- Read the evaluation record and remaining limitations.

This is an offline evaluation interface, not the finished multi-coin agent product. Source coverage is incomplete, historical charts are not live signals, and there are no real-order tools. Raw data, PDFs, notebooks and outputs remain private.

## Verified progress and continuation

- [Current progress](research/CURRENT_PROGRESS.md)
- [Manual continuation guide](research/MANUAL_TRAINING_HANDOVER.md)
- [Latest evidence diagnostic](research/PDF_EVALUATION_003_RESULTS.md)
- [Base versus adapter diagnostic](research/PDF_EVALUATION_002_RESULTS.md)
- [Latest cloud training result](research/PDF_SFT_006_RESULTS.md)
- [PDF training plan and historical record](research/PDF_TRAINING_PLAN.md)
- [Research library](research/part1_library/RESOURCE_CATALOG.md) and [unfinished playlist review](research/part1_library/PLAYLIST_REVIEW.md)

Local checks below do not fit models:

```powershell
python -m unittest discover -s tests -p test_research_math.py -v
python -m unittest discover -s tests -p test_workbench.py -v
```

All model fitting, calibration and hyperparameter searches must run on Kaggle or another authorized cloud runtime. No local fallback. The original numerical `experiment_001` was a failed laptop experiment before the cloud-only restriction; its artifacts remain historical and must not be described as cloud execution.
