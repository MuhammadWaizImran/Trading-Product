> Current checkpoint, 23 September 2026: Six Qwen3-8B PDF cloud fitting runs and diagnostic 003 are complete. No training is currently running. No adapter has demonstrated reliable improvement; earlier narrow approvals are withdrawn. Automatic retrieval development packets are prepared but not cloud-evaluated. Read [CURRENT_PROGRESS.md](CURRENT_PROGRESS.md) and [PDF_EVALUATION_003_RESULTS.md](PDF_EVALUATION_003_RESULTS.md). The dated plan/status statements below are historical where inconsistent.

# Training from the user's PDFs

Latest update: Diagnostic 002 completed and revealed no demonstrated adapter improvement. See `PDF_EVALUATION_002_RESULTS.md`. Diagnostic 003 (cloud inference with/without checked evidence) is submitted. No further fitting is currently running; earlier running-job statements are historical. The full project remains incomplete.

## Latest execution update

22 September 2026: Run 006 completed but is not promoted. Review and artifact checks are in `PDF_SFT_006_RESULTS.md`. An inference-only, private cloud diagnostic, `waizimran/crypto-qwen3-pdf-evaluation-002`, has been submitted to compare base/004/006 under old and neutral prompts. DP04 stays staged. Earlier RUNNING statements below are historical and superseded.

RUNNING: corrective DP03 run 006 was submitted privately at https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-006 . It restarts from accepted adapter 004, includes the 24 reviewed DP03 training examples plus four explicit corrections for NOBI, expected value, address/entity counting and invented numbers, and uses four fresh DP03 tests. It uses one epoch at learning rate 0.000025. Local preparation and validation only; cloud fitting is active.

COMPLETED BUT REJECTED FOR PROMOTION: DP03 run 005 completed privately at https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-005 . Only two of four fresh DP03 checks passed; it also invented NOBI significance and repeated an RSI answer. See [run 005 results](PDF_SFT_005_RESULTS.md). Do not use adapter 005 as a parent.

COMPLETED WITH NARROW PROMOTION: corrective DP01 run 004 completed privately on Kaggle at https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-004 . Three of four fresh DP01 checks passed and the repetition failure disappeared. One response invented `r = 0.75`, and old NOBI, holder-count and expected-value errors remain. See [run 004 results](PDF_SFT_004_RESULTS.md). It is acceptable only as a continuation parent, not a production model.

COMPLETED BUT REJECTED FOR PROMOTION: cumulative run 003 trained on DP01 for two epochs and reduced validation loss from 3.792656 to 3.089774, but human review found an unjustified price formula, incomplete address/entity reasoning and new repetitive truncation. It remains preserved at https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-003 and in `results/pdf_sft_003_v1`. See [run 003 results](PDF_SFT_003_RESULTS.md). It is not the parent of run 004.

COMPLETED: the first PDF-derived cloud run finished and its adapter was saved, reloaded and downloaded. See [the result and limitations](PDF_SFT_001_RESULTS.md). The separate inference-only diagnostic also completed, and all 16 responses were manually reviewed. Base and adapter each had three passes, one partial and four failures on eight post-inspection cases. No clear quality improvement was demonstrated. No claim of full-library coverage or expertise. Further dataset review and a fresh evaluation protocol are needed before another training run.

COMPLETED: continuation run 002 added 24 DP07 examples and replayed the earlier 24 training examples. See [run 002 results](PDF_SFT_002_RESULTS.md). It completed on Tesla T4, reloaded exactly, and reduced validation loss, but its four new checks showed three passes and one partial versus four parent passes. It expanded source coverage without demonstrating better overall answers.

The user completed account verification. The private PDF notebook version 1, kernel ID 135203929, run 351509199 completed on Kaggle: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-001 . Runtime and results confirm Tesla T4 execution and six optimizer steps on 24 PDF-derived examples. The earlier account blocker below is resolved. No local training.

## Authorization and scope

The user explicitly requested using their uploaded PDFs for Qwen3-8B training and then confirmed: "i have the permissions to use it for model training". Record this as a user attestation for the uploaded collection; it is not an independently verified publisher license. Private cloud training is authorized. No further permission request is needed for this scope. Attribution and source provenance are retained.

The earlier synthetic pilot is superseded as the requested training dataset. That earlier job failed before fitting and produced no adapter. The later PDF-derived job did produce an adapter.

## Preparation

Use reviewed PDF material to create source-traceable supervised question/answer examples. Preserve the original PDF files. Every example records source ID, filename, file hash and PDF page numbers, with any clarifications or corrections. This is PDF-derived instruction tuning, not blind repetition of the books and not a claim that every page is correct.

Deduplicate exact and near-duplicate documents before splitting. Keep different renditions of the same example in the same split. Hold unreviewed passages, unreadable chart details, known errors, advertisements and unsubstantiated performance claims out of the first batch. Expand the corpus as substantive review proceeds. Scanned charts need visual descriptions checked against their images; Qwen3-8B is text-only.

First batch: 32 selected reviewed question/answer examples from DP05 (Crypto Wealth Academy), DP06 (Elisa Crypto), DP17 (Binance Academy), and DP19 (Angerer, Gramlich and Hanke). There are 24 training, four validation and four test examples. This is a small initial subset, not coverage of all 22 files. Unused documents are not rejected as a whole. Full-library review remains unfinished. The example file is research/pdf_training_examples.json. The builder produces source hashes, page references, split files and an inclusion/hold ledger.

## Evaluation

Compare the same base model and adapter using held-out questions and completion loss. Questions test the supplied knowledge, uncertainty and correct formulas. Report generations for human review; do not substitute keyword matching for factual accuracy. Record exact source/dataset/model hashes and runtime versions. No trade performance, market forecasting or profitability is established by this test. No production or agent progression on training loss alone.

## Historical cloud blocker — resolved before the successful PDF run

The following entries preserve the earlier investigation. Their pending/sign-in/not-submitted statements describe that earlier state, not the current execution status above.

A separate Kaggle diagnostic completed. Despite requested GPU and internet flags, its actual runtime reports Python 3.12.13, CPU-only torch 2.10.0+cpu, no nvidia-smi, missing bitsandbytes, and DNS failures for PyPI, Hugging Face and Kaggle. The diagnostic is saved in results/qwen_cloud_check/cloud_check.json. This runtime cannot train the proposed Qwen3-8B setup. Do not repeat blind submissions or fall back to laptop training. Inspect account/runtime allocation and connectivity, or use another authorized cloud runtime. No paid resource is authorized.

The permission issue is resolved by the user's attestation. Cloud capability and corpus preparation are distinct outstanding issues.

Browser follow-up: Chrome is not signed in to Kaggle. The private notebook was inaccessible from that session, and the homepage exposed Sign In. The user has been asked to sign in to the account waizimran so runtime settings can be checked. No password or new API key was requested. Do not infer that the account lacks verification or quota: neither has been established.

LATEST browser evidence: the user signed in successfully as Waiz Imran. In the diagnostic notebook editor, Session options shows disabled Internet off and explicitly states that phone verification is needed to access GPU/TPU or turn on internet. The Get phone verified link opens the phone-number/SMS verification dialog, including a CAPTCHA. Left it open for the user to complete; no phone number, CAPTCHA or verification code was entered by the assistant. This establishes an account verification blocker, not a quota-reset problem.

Prepared and locally checked: data/pdf_sft_batch_001/{train,validation,test}.jsonl, manifest.json, ATTRIBUTION.txt; notebooks/pdf_sft_001/pdf_sft_001.ipynb. Source file hashes match the reviewed inventory and record-level page references are checked. Python syntax validation passed. These checks do not execute a model. The PDF notebook has not been submitted or trained. Its guard requires a hosted cloud GPU and connectivity before any fitting; it saves before/after generations for factuality review and a reloadable adapter if training succeeds.
