# Latest: private training experiment022 submitted and running (2026-10-28)

Reviewed all32 run021 final answers. Strict grounded-answer review: base13/16, adapter14/16; format/status metrics concealed unsupported conclusions. These narrow author-reviewed diagnostic scores are not trading accuracy or independent acceptance. See research/PDF_TRANSFER_021_RESULTS.md.

Prepared190-example targeted correction experiment022 (166 retained+24 original paired exercises),6 validation probes,28 evaluation questions (16 exposed021+12 new correlated author-reviewed heldout questions). Same pinned Qwen3-8B fresh QLoRA adapter, two epochs, no017 overwrite. Same-run base/new/reload thinking-mode comparisons. Static payload/split/schema/cloud-guard checks passed. No local model execution.

Private Kaggle version1 submission succeeded; API status verified running: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-022 . Running does not prove the optimizer stage has started. No completion/quality claim yet. Source hash93c4146600806f673a7aa6cb5aadec7d4dd3041629c820c10596d001c8a57b90. See research/PDF_SFT_022_PLAN.md for exact recipe, limitations, review rules and manual download steps. No automatic successor or background monitor installed. The submitted cloud job can execute independently of this conversation; subsequent inspection is still required.

Next: inspect cloud artifacts on completion, verify actual fitting, evaluate all final responses and reload consistency. Reject unsupported source attribution or arithmetic regressions. Independent acceptance and trading evaluations remain outstanding; no model promoted and no live agents/orders enabled.

---
# Latest: model evaluation021 running (2026-10-28)

User requested completing the model. Prepared and submitted private Kaggle transfer-check-021 version1; API status verified running. Sixteen new author-reviewed paired diagnostic cases,32 generations comparing pinned base Qwen3-8B and SHA-verified adapter017, same020 prompt/settings. No fitting or local model execution. This is diagnosis using known passages, not independent acceptance or trading accuracy.

See research/PDF_TRANSFER_021_PLAN.md for predeclared decision rules and exact download/review commands. scripts/review_transfer_eval_021.py checks structure/status/citation while leaving semantic accuracy unset and promotion disabled. All final answers require evidence-based manual review. No automatic next training job or background monitor is installed. Run020 remains complete/unpromoted; TradingAgents integration remains separate and unverified with live credentials.

Next: retrieve021 when finished, inspect all32 answers and paired failures, then choose targeted correction training only if justified. Do not label the model complete or quote format scores as expertise. Independent review and broader product/trading evaluation remain outstanding.

---
# Latest: isolated TradingAgents/Groq setup (2026-10-28)

Installed upstream commit c4544913a14ed3df5f1ed7b9e8483270ce20682a in integrations/TradingAgents with a separate Python 3.11 environment. 88-package compatibility check, Python syntax, PowerShell syntax and offline graph import/config check passed. No local training or inference; no authenticated Groq call or agent research run was made. Chat-exposed key was not used/stored; replacement key must be entered locally through the secure launcher.

See integrations/TRADINGAGENTS_SETUP.md for exact manual steps. Starter Groq model: openai/gpt-oss-20b (account availability unverified). Launcher explicitly routes crypto and enables market/social/news analysts only: upstream company-fundamentals analyst excluded pending token-specific tools. Research-only partial reports, no orders, no automatic coin scanning or continuous monitoring. Original Qwen adapter is not connected. Dependency snapshot in integrations/tradingagents-dependencies.txt.

Run020 remains complete and unpromoted; no new training run started. Next integration step: secure Groq model-list check, then quota-controlled research smoke test and factual/data-coverage evaluation. This isolated setup does not satisfy the main product's Part3 acceptance gate.

---
# Latest: source guard implementation (2026-10-28)

Implemented workbench source-identity guard: explicit English unidentified-document cues request source clarification even when general scope or a stale document selection is supplied. Existing source-selection behavior retained. This is a conservative cue guard, NOT general intent detection or semantic entailment; paraphrases/languages not covered and quoted/negated cues may cause clarification.

Added workbench/response_review.py: standalone offline generated-response rejection module rejects malformed/duplicate-key JSON, invalid status, bad citation shape, missing/ambiguous IDs, wrong document and truncation. Passing checks ALWAYS remains needs_semantic_review and publishable=False, including abstentions. Not connected to a model endpoint; workbench still returns checked passages only. Existing IDs cannot prove claim support.

Verification:13 workbench HTTP/data tests,6 source-scope tests,5 response-review tests passed (24 total). Includes general-scope and selected-document bypass checks. No fitting/inference, deployment, real orders or cloud run performed. These are engineering regression tests, not independent model acceptance.

Next: collect independently reviewed question/evidence pairs for semantic acceptance and design source-confirmation handling for broader phrasing. Keep generation unapproved pending that evaluation. Run020 is complete, not currently training. Discovery/continuous monitoring/voice remain unimplemented.

---

# Latest: run020 complete and reviewed (2026-10-28)

Downloaded results/pdf_scope_020_v1; all100 final answers reviewed. Base contract46/50, adapter47/50. This is92%/94% format compliance, NOT trading or semantic accuracy. Source-identification objective failed: both attribute three unknown reports and cite unrelated cold-storage evidence for ownership. Calculations tested remain correct. No model promoted. See PDF_SCOPE_020_RESULTS.md.

Stop repeated prompt-only runs on the same exposed questions. Next: source-scope enforcement and independent testing, using existing checked-answer workbench. No new cloud run started. Product discovery/monitoring/voice still incomplete; maintain research/paper-only and no real orders. Current application: python -m workbench.server (localhost only, no model execution). No ongoing training implied.

---

# Latest: scope evaluation020 running (2026-10-28)

019 reviewed:100 records;41/50 base and42/50 adapter contract passes, source-identity errors persist; no promotion. See PDF_REASONING_019_RESULTS.md. User also asked about migration; MODEL_MIGRATION_GUIDE.md and hash manifest created, no target deployment performed.

Private020 version1 submitted and running verified: https://www.kaggle.com/code/waizimran/crypto-qwen3-scope-check-020
Evaluation only, no fitting. Same50 exposed cases, base/adapter017, thinking,seed217,sampling,2048 cap; only system prompt clarified.100 generations. Source in notebooks/pdf_scope_eval_020. No local model execution, public upload, paid service or real orders.

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-scope-check-020
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-scope-check-020 -p results/pdf_scope_020_v1
Get-Content results/pdf_scope_020_v1/pdf_scope_020/status.json
```
After completion review50 baseline_thinking and50 adapted_thinking final_response fields. Check ID coverage, truncation, JSON status, single exact evidence_id, source entailment, unknown documents, arithmetic and negative-answer support. Compare019 and same-run base; prompt gains are not learned gains. No background monitor/automatic successor configured. No model promotion until independent acceptance; library review and discovery/voice/continuous product remain unfinished.

---

# Latest: reasoning evaluation019 submitted (2026-10-25)

Run018 completed and all32 final answers reviewed. Thinking mode fixes several longstanding calculations in both base and adapter017, but unidentified source attribution fails. No learned advantage established or model promoted. See PDF_REASONING_018_RESULTS.md.

Private run019 version1: https://www.kaggle.com/code/waizimran/crypto-qwen3-reasoning-check-019
Full50 exposed development cases, base versus adapter017 with thinking enabled:100 generations. This is evaluation, NOT new fitting. Same seed217, sampling settings and2048 output-token cap. Static syntax/payload/private-GPU checks passed. Code SHA256:49779efa4e0d7df2b91cd2abd096afbc97e33cd5e4684d24aea924604e22eb32. Cloud-only; no model execution locally.

Manual continuation:
```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-reasoning-check-019
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-reasoning-check-019 -p results/pdf_reasoning_019_v1
Get-Content results/pdf_reasoning_019_v1/pdf_reasoning_019/status.json
```
After completed_diagnostic_human_review_pending, read50 final_response fields in baseline_thinking.json and50 in adapted_thinking.json. Check unique IDs, raw/final separation, JSON, entailment, polarity, calculations, source identification, abstention and token limits. Report missing/truncated final answers as failures/inconclusive, never silently omit. Compare same-run base before attributing learned gains. Exposed cases are not final acceptance. No019 background monitor/automatic successor configured. Independent acceptance, remaining PDF review and discovery/voice/24-hour product implementation still outstanding. No paid services, public data or real orders.

---

# Latest: reasoning diagnostic018 submitted (2026-10-21)

SFT017 completed and reviewed; no promotion.73.68 minutes fitting,50/50 JSON contract but serious semantic failures persist. Read PDF_SFT_017_RESULTS.md. Saved-adapter reload matches all50 answers.

Private next run018: https://www.kaggle.com/code/waizimran/crypto-qwen3-reasoning-check-018
This is inference diagnosis, NOT new fitting. Eight exposed cases, base/adapter017 crossed with thinking off/on,32 generations. Same sampling settings,seed217 and2048 output-token cap. Dataset/cases, cloud code and review protocol in notebooks/pdf_reasoning_eval_018. Thinking may exhaust the token budget; no final answer is a failure/inconclusive result, not proof of improved reasoning. Adapter was trained non-thinking. No local model execution.

Manual continuation:
```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-reasoning-check-018
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-reasoning-check-018 -p results/pdf_reasoning_018_v1
Get-Content results/pdf_reasoning_018_v1/pdf_reasoning_018/status.json
```
After completed_diagnostic_human_review_pending, inspect baseline_non_thinking.json,baseline_thinking.json,adapted_non_thinking.json,adapted_thinking.json. Each must have8 unique expected IDs. Evaluate final_response separately from raw response; require correct numeric answers, valid status/evidence_id and no unsupported claims. Compare within job; historical greedy results are not a controlled comparator. No018 background monitor or automatic successor. Do not repeat narrow fitting without evidence. Full-library review, independent acceptance and product discovery/monitoring/voice implementation remain incomplete. Cloud-only private research/paper scope; no paid services or real orders.

---

# Latest: SFT017 submitted (2026-10-21)

Diagnostic016 completed and all24 responses reviewed. Relevant-only evidence fixes several failures, but leverage remains wrong. See PDF_EVIDENCE_016_RESULTS.md. No model promoted.

Private SFT017 version1 submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-017
166 training exercises:108 retained plus58 mixed-evidence variants with existing training-only distractors; no new PDF coverage. Fresh pinned Qwen3-8B all-linear rank8 LR1e-5 two epochs;6 validation probes and50 exposed development tests. Source/provenance/hash/static checks passed. Code SHA256:739730d86a16eabc3fb6991330b5942849913fc9e92a919fce4c4d1fa4fe62ab. Cloud token-length guard remains active. No local fitting/inference.

Manual continuation:
```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-017
tmp\kaggle_client\Scripts\python.exe scripts/download_pdf_artifacts.py --batch 017 --dest results/pdf_sft_017_manual
python scripts/audit_pdf_run.py --batch 017 --results results/pdf_sft_017_manual/pdf_sft_017
python scripts/audit_structured_pdf_012.py --batch 017 --results results/pdf_sft_017_manual/pdf_sft_017
```
Download after completion, audit only after completed_training_human_evaluation_pending. Compare all base/adapted answers for evidence support, arithmetic, polarity and truncation; saved-model reload must match. Falling loss and JSON formatting are not correctness. No background monitor or automatic successor configured for017. No reliable overall completion percentage or ETA. If mixed-evidence training fails, diagnose numerical tooling and source selection before another fitting run. Independent acceptance/full-library review remain unfinished; Part3 gated. Product requirements remain in PRODUCT_MONITORING_REQUIREMENTS.md. No paid services, public sharing or real orders.

---

# Latest: evidence diagnostic016 submitted (2026-10-06)

SFT015 reviewed, not promoted; see PDF_SFT_015_RESULTS.md. Lower learning rate did not fix core errors. Next run is inference diagnosis, NOT additional fitting.24 generations compare six exposed questions with multi-passage versus manually selected evidence, base versus adapter015. Oracle retrieval condition must not be called autonomous coin discovery. No local model execution.

Actual Kaggle URL: https://www.kaggle.com/code/waizimran/crypto-qwen3-evidence-check-016 (server used title-derived slug; local metadata corrected afterward without resubmitting).

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-evidence-check-016
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-evidence-check-016 -p results/pdf_evidence_016_v1
Get-Content results/pdf_evidence_016_v1/pdf_evidence_016/status.json
```
Read12 base and12 adapted answers, compare each paired condition for correctness, evidence_id and truncation. Relevant-only success indicates distraction sensitivity; failures even there indicate application problems. Do not claim causal certainty from six exposed cases. No monitor or automatic successor configured. Review before further fitting. New product requirements saved in PRODUCT_MONITORING_REQUIREMENTS.md; implementation/hosting/voice providers not launched, Part3 gated. Overall training incomplete; no expertise/profit claim.

---

# Latest checkpoint: SFT015 submitted (2026-10-06)

SFT014 reviewed, not promoted; see PDF_SFT_014_RESULTS.md. SFT015 version1 submission succeeded. Same108 examples and all-linear adapter; only fitting change is learning rate2e-5 to1e-5. No new PDF coverage. Preflight passed. Overall readiness remains unapproved. No015 completion monitor configured: a combined documentation/background-launch command was blocked by execution policy. Cloud job was already submitted independently.

Follow the015 commands at the top of MANUAL_TRAINING_HANDOVER.md. Do not blindly repeat this recipe if severe errors persist.

---

# Current checkpoint: SFT014 running (2026-10-04)

SFT013 completed and reviewed; no promotion.108 examples,37.27 minutes fitting, loss2.96765 to1.65382.50 baseline plus50 adapted answers reviewed, reload equality verified. Format compliance48/50 both; severe arithmetic, source attribution and RSI regression remain. Read research/PDF_SFT_013_RESULTS.md.

Private SFT014 version1 submitted and Kaggle status verified running:
https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-014
Fresh pinned Qwen3-8B; identical108 examples,6 validation probes,50 exposed tests and prompt from013. Controlled change: LoRA target_modules from q_proj/v_proj to all-linear, rank8 alpha16 dropout0.05 LR2e-5 two epochs unchanged. Broader adaptation is an experiment, not established superiority. No new corpus coverage. Actual seven training-source counts corrected in014 manifest;013 historical source summary was stale. Code SHA256:17210ca2a2ee997a5141dfc3c93625ca752401c41cf99d28b751674c9b28801b. Structural/hash/provenance checks passed; no local model execution.

Bounded monitor scripts/monitor_pdf_run_014.py launched (initial PID9764). Polls every120 seconds for up to6 hours, downloads final artifacts with retries and runs artifact/JSON checks. Check research/PDF_SFT_014_MONITOR.json and tmp/monitor_pdf_014_stderr.txt. Laptop must stay awake/online for monitor; Kaggle training runs independently. Monitor does not automatically launch successor training or perform semantic review. No always-on assistant implied. Download helper intentionally excludes intermediate optimizer checkpoints; final adapter is included.

Manual continuation from project PowerShell:
```powershell
$env:PYTHONUTF8='1'
Get-Content research/PDF_SFT_014_MONITOR.json
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-014
tmp\kaggle_client\Scripts\python.exe scripts/download_pdf_artifacts.py --batch 014 --dest results/pdf_sft_014_manual
Get-Content results/pdf_sft_014_manual/pdf_sft_014/status.json
python scripts/audit_pdf_run.py --batch 014 --results results/pdf_sft_014_manual/pdf_sft_014
python scripts/audit_structured_pdf_012.py --batch 014 --results results/pdf_sft_014_manual/pdf_sft_014
```
Use monitor's recorded destination if it downloaded already. Run audits only after completed_training_human_evaluation_pending and complete downloads. Inspect all baseline/adapted answers for source support, polarity, unnecessary abstention and question-specific arithmetic; verify saved-model reload agreement. Compare014 against013 and same-run base; do not equate falling loss or valid JSON with correctness. Reject promotion if serious failures persist. Before further fitting, diagnose whether capacity helped; do not indefinitely repeat runs. Full-library review and independent acceptance remain incomplete. No claimed completion percentage or expert capability. No paid compute, public data, local fitting/inference or real orders authorized.

---

# Current checkpoint: SFT013 running (2026-10-01)

User requested the next cloud training run. SFT012 completed and reviewed; no promotion. See research/PDF_SFT_012_RESULTS.md. Fitting took16.76 minutes; structured contract44/50 versus base43/50, but arithmetic, source attribution and unnecessary abstention errors remain.

Private SFT013 version1 submitted successfully and Kaggle status verified running:
https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-013
Fresh pinned Qwen3-8B; rank8 QLoRA LR2e-5, two epochs.108 training examples (72 retained plus36 targeted applications),6 validation probes,50 exposed development cases. Seven training PDF sources in selected passages; not the entire library. Static provenance/hash/payload/cloud-guard checks pass. No local model execution. Code SHA256:6911c69e98a18b5aa969314c53e39bbf2e9a72454581747ae3fae8c3ad436943.

Manual continuation from project PowerShell:
```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-013
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-013 -p results/pdf_sft_013_v1
Get-Content results/pdf_sft_013_v1/pdf_sft_013/status.json
python scripts/audit_pdf_run.py --batch 013 --results results/pdf_sft_013_v1/pdf_sft_013
python scripts/audit_structured_pdf_012.py --batch 013 --results results/pdf_sft_013_v1/pdf_sft_013
```
Run audits only after cloud reports completed_training_human_evaluation_pending and files download completely. Read all baseline/adapted answers for support, unnecessary abstention, numeric correctness and unidentified-source handling. Compare equally prompted base before claiming training gains. Strict response format is not semantic accuracy. Require independent acceptance before promotion. Cloud pipeline automatically performs baseline, fitting, evaluation, saving and reload verification. No local completion monitor or automatic successor job configured for013. No precise completion ETA verified. Training may remain queued despite running status; no claim of completed optimizer steps yet.

---

# Latest direction: own Qwen training resumed; SFT012 submitted (2026-09-30)

User explicitly deferred the alternative-model option and authorized continued custom training. SFT011 recovered and reviewed:72 examples,8.48min fitting, loss5.79286 to5.33171; artifact/reload checks passed but semantic failures remain. See PDF_SFT_011_RESULTS.md. No model promoted.

Private SFT012 version1 submitted successfully: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-012 . This is actual training, distinct from earlier format diagnostic012. Fresh pinned Qwen3-8B,72 reviewed exercises serialized as status/answer/evidence_id JSON, two epochs, rank8 QLoRA LR2e-5;6 validation probes and50 development tests. No new corpus coverage. Static source/split/provenance checks passed. Training success and expert readiness not yet established.

Manual continuation:

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-012
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-012 -p results/pdf_sft_012_v1
Get-Content results/pdf_sft_012_v1/pdf_sft_012/status.json
```

On completed_training_human_evaluation_pending:

```powershell
python scripts/audit_pdf_run.py --batch 012 --results results/pdf_sft_012_v1/pdf_sft_012
python scripts/audit_structured_pdf_012.py --results results/pdf_sft_012_v1/pdf_sft_012
```

Read all baseline/adapted answers; validate evidence status, entailment, polarity, question premises, arithmetic and exact evidence ID. General audit's bracket-citation check does not validate JSON evidence_id; run the structured audit too. Neither proves semantic quality. Test references remain prose and are never fitted; validation loss now uses6 structured cases and cannot be compared directly to old42-case losses. Same prompt/format for base and adapter. Preserve no-promotion unless comparative evidence supports it, and require independent acceptance before calling model ready. No local model execution; no new paid/public/live-order scope. No monitor for012 currently configured; older011 monitor errored and its data was recovered manually.

---

# Latest direction: evaluate already domain-adapted models first (2026-09-30)

User prefers existing crypto-trained weights plus research agents, testing before further fine-tuning. Five supplied links investigated; Medium full text remains inaccessible (403/timeouts). Detailed findings and proposed tests: model_selection_2026_09_30/REVIEW.md. CryptoTrader-LM is a real BTC/ETH daily-decision adapter, but published test Sharpe is negative and base requires commercial licensing; adapter permission unclear. Frameworks are not pretrained weights. Fin-R1 is a financial-reasoning comparator, not certified crypto expertise. No new model execution or fitting launched in this research turn. Preserve SFT011 and prior artifacts; its completed results are still pending review. Prioritize license/compatibility verification and frozen comparisons before any new custom training. Research/paper-only and private cloud-only restrictions persist.

---

# Latest checkpoint: SFT011 running; completion monitor verified (2026-09-29)

Kaggle API confirms corrective SFT011 running. Bounded monitor scripts/monitor_pdf_run_011.py started (initial PID24972); its process and first successful status poll verified. It polls every120 seconds for up to6 hours, downloads completed/error outputs and runs the artifact-only audit after successful fitting. No local model loading/training, automatic successor job, publishing or real orders. Semantic answer review remains required.

Monitor state: research/PDF_SFT_011_MONITOR.json. Logs: tmp/monitor_pdf_011_stdout.txt and tmp/monitor_pdf_011_stderr.txt. Keep laptop awake and online for monitoring; the cloud training job runs independently. On downloaded_review_required use the destination and audit exit code recorded in the state file. On monitor timeout/error, check Kaggle manually using commands below; the cloud job is not stopped. Do not start duplicate monitor copies while its process is active.

```powershell
Get-Content research/PDF_SFT_011_MONITOR.json
```

No actual fitting percentage or completion time verified in this checkpoint. Same-run automatic stages are baseline evaluation, fitting, validation, adapted-answer generation and saved-adapter reload evaluation. Overall model readiness remains unapproved.

---

# Latest checkpoint: diagnostic012 reviewed; corrective SFT011 submitted (2026-09-29)

All24 diagnostic012 answers reviewed and audited with no truncations. Declarative evidence repairs two adapter errors (candle naming, offline-receiving polarity), but maker/taker, fixed-notional and irrelevant-source errors persist. Full report: PDF_FORMAT_012_RESULTS.md. No model promoted.

Actual corrective training SFT011 version1 successfully submitted to private Kaggle: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-011 . This is DIFFERENT from completed broad-check011 and format-check012, which were evaluation jobs.72 reviewed correction examples (48 retained explicit contrasts plus24 new applications),42 validation,50 development tests. Training sources: six PDFs; evaluation includes ten. Older230 mixed-evidence training records excluded from this small experiment; no new PDF coverage. Fresh pinned Qwen3-8B, rank8 QLoRA, one epoch LR2e-5. All model execution stays on cloud.

Same conditional prompt and declarative evidence for baseline, trained and reload evaluations. Local preflight passed PDF hashes, dataset splits, payload identity and cloud guards. Source code SHA256:afd4cfe7d2c7593f4bdabbe644a464b195f76c378737c1266c66b5d6d1bff2a4. Frozen preparation: scripts/prepare_pdf_run_011.py. Independent acceptance remains incomplete; these are exposed development tests. Submission does not prove completed fitting.

Manual continuation from project PowerShell:

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-011
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-011 -p results/pdf_sft_011_v1
Get-Content results/pdf_sft_011_v1/pdf_sft_011/status.json
```

After successful completion:

```powershell
python scripts/audit_pdf_run.py --batch 011 --results results/pdf_sft_011_v1/pdf_sft_011
```

Read all50 baseline/adapted answers and verify reload equality. Check polarity, exact evidence IDs, whether cited passages actually support claims, fixed-notional reasoning and source abstention. Compare against equally formatted base before attributing improvements to training. Do not claim success from loss alone or keep repeating identical runs. This job automatically performs baseline, training, validation, adapted and reload evaluation. No background completion monitor or successor-job launcher is configured for this new job; the010 monitor already finished.

---

# Latest checkpoint: evaluation011 reviewed; diagnostic012 submitted (2026-09-29)

The earlier usage-limit download block cleared on retry. Run011 outputs downloaded;100 generated answers read,200 records audited, zero truncations and100 total deterministic routes verified separately. Adapter010 still fails and regresses against base on candle naming and affirmative offline receiving; both fail maker/taker reasoning. Other unsupported details and wrong-source claims persist. No model promoted. Full review: PDF_BROAD_011_RESULTS.md.

Private diagnostic012 version1 submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-format-check-012 .24 total generations compare original Q&A evidence with declarative evidence on six selected failure scenarios for base and adapter010. This is a bounded inference diagnostic, not new fitting or final acceptance. It tests whether evidence formatting contributes to the failure before spending compute on more training.

Manual continuation:

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-format-check-012
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-format-check-012 -p results/pdf_format_012_v1
```

After completion read pdf_format_012/status.json, protocol.json and both conditional_evidence output files. Expect12 unique cases per model: six scenarios with qa/declarative suffixes, all model-invoked. Compare supported cases04,06,10,24 for correct conclusion and no invented details; irrelevant cases16,22 must identify insufficient relevant evidence without supplying unsupported answers. Check citations and truncation. This is exposed development evidence, not independent accuracy. Do not claim a prompt/format gain is learned improvement. No automatic monitor for012 is configured. The010 monitor has finished.

---

# Latest checkpoint: SFT010 completed and reviewed; broader evaluation011 submitted (2026-09-29)

SFT010 completed successfully.47 minutes of actual GPU fitting;278 examples,42 validation,50 development test cases. Validation loss5.56494 to3.48799. All50 baseline and50 adapted answers read;50 reload answers verified equal. Structural audit passed and no outputs truncated. Some arithmetic/limit-price corrections improved, but false source attribution, invalid/missing citations and contradictory polarity remain. No promotion or expert claim. Full review: PDF_SFT_010_RESULTS.md.

Private evaluation011 version1 submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-broad-check-011 . This is inference testing, not another fitting run.100 exposed grouped development cases, base versus adapter010, same conditional prompt, explicit source gate; deterministic routes reported separately. Frozen script/protocol in notebooks/pdf_broad_eval_011. Independent acceptance and remaining library review are not complete.

Manual continuation:

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-broad-check-011
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-broad-check-011 -p results/pdf_broad_011_v1
```

Download once complete and inspect status.json plus base_conditional_evidence.json and adapter010_conditional_evidence.json inside pdf_broad_011. Check all IDs, truncation,50 model-invoked answers per model and50 deterministic routes. Use PDF_BROAD_010_RUBRICS.json; these are exposed regression cases, not final exams. Require supported citations, correct polarity and appropriate abstention, and distinguish prompt gains from adapter gains. The old010 monitor has finished its download task; it does not monitor011. No automatic successor-training loop is configured.

---

# Latest verified live log: Run010 fitting in progress (2026-09-29)

Authenticated Kaggle Logs confirms GPU T4 x2 allocation (trainer uses GPU0), baseline evaluation completed, and training_pdf_examples started at958.3 elapsed seconds. Last inspected loss entry at1309.8 seconds reports epoch0.12: approximately12% of this single fitting epoch, not12% of the overall project. Last batch loss0.6734 does not establish answer quality. Roughly45?50 minutes of fitting remained at this observation if throughput stays similar, followed by validation and adapted/reloaded answer generation. This is an estimate, not a deadline.

Evidence recorded in PDF_SFT_010_LIVE_PROGRESS.json. Existing background monitor continues collecting completion status; no duplicate job submitted and no local model execution. Next dependent action remains downloading and reviewing completed baseline/adapted/reloaded answers. Do not start a successor run before evaluating this run's failures and advantage over base.

---

# Latest update: background result monitor active (2026-09-29)

SFT010 remains running on Kaggle; no downloadable artifacts were available at the latest check. A bounded local monitor is now active (initial PID1660), polling every120 seconds for up to6 hours. It only calls Kaggle status/output and the artifact-only audit; it never loads a model, fits locally, launches successor training, publishes data or places orders. When cloud execution ends it downloads results, checks artifacts if training succeeded, and records that semantic review is still required.

Monitor state: `research/PDF_SFT_010_MONITOR.json`. Script: `scripts/monitor_pdf_run_010.py`. Output/error logs: `tmp/monitor_pdf_010_stdout.txt` and `tmp/monitor_pdf_010_stderr.txt`. The initial running process and its first successful cloud poll were verified. Keep the laptop awake with internet for this local monitor; Kaggle training itself continues independently. The monitor stops after6 hours or repeated connection failures; that does not stop Kaggle.

Manual inspection:

```powershell
Get-Content research/PDF_SFT_010_MONITOR.json
```

If stage is downloaded_review_required, inspect the destination recorded there, cloud status, audit exit code and answers. A successful artifact audit is not semantic acceptance. Avoid starting another copy while its PID is still active. Existing manual download and audit commands below remain valid. No fully autonomous assistant or successor-run scheduler is configured; only result collection and structural checks are automated.

---

# Latest checkpoint: PDF training010 running (2026-09-29)

Private Kaggle SFT010 version1 submitted successfully; API status verified **running**. URL: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-010 . This job includes actual cloud fine-tuning, unlike broad010 diagnostics. Running is not proof that fitting has begun or completed; runtime artifacts must confirm stage and GPU.

278 training records (230 replay +48 grounding/polarity contrasts),42 validation,50 development test records. Selected reviewed material from ten PDFs; no new whole-PDF coverage. Same pinned Qwen3-8B, fresh rank8 QLoRA, one epoch, LR2e-5. Identical conditional prompt for base/adapted/reloaded comparisons. Static hashes, PDF provenance, citations, splits, privacy and cloud-only guards pass. The first upload exceeded Kaggle's1MB source limit and was rejected before execution; lossless payload compression fixed it. Uploaded code SHA256:371d87d002515cc95107e7a1844b6353b56f5b7ad90ae6f35c10d1454db3ac4b.

Broad010 completed:100 model-generated answers reviewed,200 records structurally checked, no truncations;50 deterministic routes per model reported separately. Both models fabricate support from unrelated evidence, invent tool results, and reverse the direct answer on offline receiving. See PDF_BROAD_010_RESULTS.md. No model is approved or certified expert. Training completion percentage is unknown. Prior009 fitting was46.2 minutes;010 has more examples and150 evaluation generations, so a reliable completion ETA is not yet available.

No repeat permission is required for authorized free private cloud model work. The submitted job runs independently; its internal baseline/training/evaluation stages proceed automatically. There is no unattended assistant or automatic successor submission configured. Review outputs and choose evidence-based next steps when an active session is available. Do not blindly loop training. Manual commands are at the top of MANUAL_TRAINING_HANDOVER.md. Part3 remains gated.

---

# Latest checkpoint: broader PDF stress assessment submitted (2026-09-28)

Private Kaggle broad010 version1 submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-broad-check-010 . 100 cases across25 concept families, four evidence conditions each, base versus adapter009 (200 responses). Review rubrics remain local outside uploaded code and inference prompts. Static syntax, cases, code hash and cloud guards passed without local model execution.

This is a grouped stress assessment, **not the100 independent application questions required for final acceptance**. Its related variants and training-concept overlap are explicit. Per model,25 relevant and25 irrelevant cases invoke the model;25 empty and25 unidentified cases are routed by the system. Report those separately rather than inflate learned accuracy. No new fitting has started; results will decide whether targeted SFT has a defensible hypothesis. Frozen protocol: `notebooks/pdf_broad_eval_010/review_protocol.json`; local rubrics: `research/PDF_BROAD_010_RUBRICS.json`.

---

# Historical checkpoint: concise009 reviewed, candidate frozen (2026-09-28)

Kaggle concise009 complete. All52 outputs downloaded, read and structurally audited. Both concise conditions retain correct limit-price verdicts, supply citations on all10 generated answers and omit the earlier unsupported registration/documentation detail. Three source-identity cases per condition are routed without model invocation. Minor repetition, sentence-count and evidential precision issues remain. See [review](PDF_CONCISE_009_RESULTS.md).

No clear adapter009 advantage. Provisional development baseline is unmodified Qwen3-8B with concise instructions, explicit source scope and verified calculator context; preserved adapter remains a comparator. Frozen model revision/prompt/component hashes: `research/model_candidate_2026_09_28.json`. Not production-approved. No new training or cloud job started. Next is a broader100-question assessment with at least25 insufficient-evidence cases, not more replay of the same13 development questions. Assessment not yet constructed. Remaining PDF disposition and visual review still incomplete. Part3 is not started or authorized by this result.

---

# Historical checkpoint: 52 answers reviewed; next diagnostic submitted (2026-09-27)

Tool diagnostic008 completed and all52 responses were read. Artifact audit verifies13 distinct expected IDs per file, no truncated answers and three routed requests without model invocation per condition. UTF-8 retry recovered the cloud log successfully. See [results](PDF_TOOL_008_RESULTS.md).

Verified calculator context fixes the reversed sell-limit answer in both base and adapter009. The adapter still omits a chart citation and adds unsupported legal procedural claims; no advantage over the base is established. No model promoted and no new fitting claimed.

Private concise-answer diagnostic009 version1 submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-concise-check-009 . It compares original versus concise evidence-only instructions for base and adapter with identical calculator context. All52 outputs must be reviewed before deciding on further SFT. Frozen preparation and protocol: `scripts/prepare_concise_diagnostic_009.py`, `notebooks/pdf_concise_eval_009`. Static syntax and SHA checks passed. No local inference/training.

---

# Historical checkpoint: cloud model diagnostic submitted (2026-09-27)

User returned focus to model development. Private Kaggle job version 1 submitted successfully: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-tool-check-008 . This is inference/evaluation of Qwen3-8B versus existing adapter009, not another fitting run. It tests 13 development cases in two source-scoped conditions, with/without explicit verified calculator context (52 responses). Source identities and calculator arguments are supplied explicitly; no automatic parsing or learned tool selection is claimed.

Prepared `scripts/prepare_tool_diagnostic_008.py` and frozen `notebooks/pdf_tool_eval_008`. Static Python parsing, code hash, case counts, private/GPU metadata and cloud guards checked locally without model execution. Acceptance requires correct calculator semantics, no execution guarantees, supported citations and source-gate behavior; all outputs require manual review. Run009 remains unapproved and full-library coverage remains incomplete. No market-trade task is active.

Next: check Kaggle status, download outputs to a new `results/pdf_tool_008_v1` folder, inspect errors and read all responses. Do not call submission training completion. Use results to justify a targeted next curriculum or model change; do not automatically repeat fitting after a failed gate.

---

# Historical checkpoint: library analysis resumed (2026-09-24)

Latest user direction: analyze all supplied data and use it to improve the assistant's project-specific reasoning. Reading/reference use does not permanently train the assistant's own weights. Focus is document analysis; no new UI work or cloud model run was performed in this review.

DP21: all 60 pages of extracted text read; 14 selected pages visually inspected. Detailed findings, provenance, retained concepts and unresolved formula/version issues: [DP21 critical review](part1_library/DP21_CRITICAL_REVIEW.md). DP22 is an exact duplicate. Found a 2018/2019 version difference, a day/per-block unit inconsistency, a fee/transaction-size symbol collision, a prose/chart mismatch and appendix editorial/mathematical flags. This is payment-economics material, not trading-performance evidence.

The entire library is not yet deeply reviewed. Next: substantive review of DP15/DP18 and remaining DP16 sections, plus outstanding chart/equation checks in the other PDFs. Consult the [coverage ledger](part1_library/DATA_PDF_REVIEW_PROGRESS.md) together with the later module-specific reviews. Run009 remains completed but not accepted as a reliable expert model; no new job was launched here. Prior status sections below are historical.

---

# Historical checkpoint: checked-answer tools integrated

The offline workbench now has a Checked answers tab and /api/answer endpoint. Source-specific questions without a selected document request identification; selected-document searches filter before ranking and never borrow another PDF. General educational mode explicitly returns candidate passages without generated interpretation. The limit-price flow uses exact Decimal arithmetic and links the checked DP17 passage. It cannot submit orders or run a model.

Validation:12 workbench/HTTP tests,6 source-scope tests and9 arithmetic tests passed (27 total), with no local fitting or inference. Browser checks verified the missing-source response, sell240/fill235 rejection and DP19-only spread evidence with page links. The test server is running at http://127.0.0.1:8766 for this session. To restart later:

```powershell
python -m workbench.server --port 8766
```

Open Checked answers. Leave Document unidentified and submit a question: it should ask for a source. Select DP19 and search relative spread denominator: only DP19 passages should appear. Check Sell,240,235: the price constraint is not satisfied, with no execution guarantee. These are deterministic system improvements, not evidence of improved model weights.

The searchable library still contains100 checked adaptations from seven PDFs; model run009 used230 records from selected sections of ten PDFs. This distinction remains visible. No cloud fitting/evaluation job is currently active. Model-generated answers remain unapproved; Part3 remains gated.

Next work: expand the verified searchable corpus carefully, improve relevance/support evaluation, and assess a model-facing tool flow in the cloud before another training experiment. Independent assessment, remaining PDF coverage and separate market/paper validation remain unfinished.

Earlier checkpoints below are historical where inconsistent.

---

# Latest update: source-scope evaluation reviewed

Diagnostic007 completed; all32 outputs were read. Explicit source selection correctly stops all three unidentified-document questions in each scoped condition. This is a system-rule improvement, not learned expertise. Both models still reverse a sell-limit constraint under the diagnostic prompt, so the full answer system remains unapproved. See [results](PDF_SOURCE_SCOPE_007_RESULTS.md).

Added an exact hypothetical limit-price checker to scripts/research_math.py; nine arithmetic tests and six source-scope tests passed without fitting or inference. This backend primitive is not yet connected to a model-facing tool flow. Next: integrate explicit numerical/source inputs with verified tools and evaluate end-to-end answer support before further SFT. No cloud job or fitting run is currently active. Run009 remains saved and rejected for promotion. Full-library coverage, independent assessment and market/paper validation remain unfinished.

User direction is recorded in AGENTS.md: take ownership of the training process and ask for additional data/access when a concrete need arises. No additional user input is needed for this immediate engineering work.

Earlier checkpoints below are historical where inconsistent.

---

# Latest checkpoint: run 009 reviewed; answering pipeline under test

Run009 completed and its artifact audit passed. All44 paired answers were read. Both base and adapter failed all three unidentified-source cases. The adapter is not accepted. Read [run009 findings](PDF_SFT_009_RESULTS.md). There is no fitting job currently running.

Following the decision fixed before009, the next work changes the answering pipeline rather than automatically repeating SFT. workbench/source_scope.py requires explicit source selection for document-specific requests and filters evidence to that source; six nonfitting tests passed. General educational scope is an explicit caller choice. This does not classify arbitrary free text or prove evidence support, and is not yet connected to public model answering in the offline workbench.

Private cloud diagnostic007 was submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-source-scope-007 . It compares base and adapter009 with and without source routing on eight development cases (32 responses). Scope metadata is manually assigned. A rule preventing a model call is a system improvement, not learned expertise. Frozen criteria are in notebooks/pdf_scope_eval_007/review_protocol.json.

## Remaining work

1. Review this pipeline diagnostic, including supported-answer preservation and citation quality.
2. Fix remaining retrieval/support errors; design further training only around an evidenced improvement hypothesis.
3. Complete broader PDF/source coverage and prepare an independent application assessment.230 records from selected sections of ten PDFs do not represent the whole library.
4. Separately develop and validate time-stamped multi-coin market analysis with realistic costs and prospective paper evaluation. PDF explanation does not demonstrate profitable prediction.

No reliable percentage or finish date for expertise exists. No real-order capability is authorized.

## Manual continuation

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-source-scope-007
```

After COMPLETE:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-source-scope-007 -p results/pdf_scope_007_v1
```

Read pdf_scope_007/status.json, protocol.json and the four base/adapter009 x unguarded/scoped answer files. Require eight matching IDs per file. The three unknown-source requests in scoped mode must have model_invoked=false, needs_source and no guessed details. The other five must still receive supported correct answers. Attribute deterministic abstention to routing, not model learning; inspect citations and meaning manually. Save a results report before further fitting. Do not execute any cloud evaluator/trainer locally or start duplicate jobs.

Previous checkpoints below are historical where inconsistent.

---

# Current checkpoint: run 009 submitted

Private Kaggle run009 has been submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-009 . It uses230 training examples from selected material in ten PDFs,36 validation and44 development-test cases. Submission does not prove optimizer completion. No local training was executed.

Diagnostic006 is complete and all32 answers were reviewed. Adapter008 corrected sell-limit direction but still assumes the identity of an unidentified paper and sometimes omits citations. It is not promoted. See [diagnostic findings](PDF_ADAPTER_006_RESULTS.md).

Run009 starts from the same pinned base with unchanged fitting settings, adding18 source-attribution contrasts. It is a controlled follow-up, not an unlimited retry loop. If identity failures persist, change the answering pipeline before further SFT. See [frozen plan and manual commands](PDF_SFT_009_PLAN.md). The coverage ledger distinguishes completed008 from submitted009. No whole-library, expertise, profitability or product-completion claim is made.

## Continue manually

Do not execute train.py locally. Check before submitting anything to avoid duplicate jobs:

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-009
```

Only after COMPLETE:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-009 -p results/pdf_sft_009_v1
python scripts/audit_pdf_run.py --batch 009 --results results/pdf_sft_009_v1/pdf_sft_009
```

Review all44 paired answers and supporting passages against the frozen criteria. Preserve both errors and gains in a new report before choosing further work. Check checkpoints/logs if ERROR; never use laptop fitting as a fallback. No automatic new training is scheduled after this job. Kaggle can execute the submitted job without the chat, but subsequent review requires active work here or manual continuation.

Earlier checkpoints below are historical where inconsistent.

---

# Latest verified status: run 008 complete

Run 008 completed all fitting, validation, answer generation and saved-model reload checks. Its artifacts are downloaded and verified. All 36 base/adapted answer pairs were read; unsupported reasoning remains, so the adapter is not accepted. Read [run 008 results](PDF_SFT_008_RESULTS.md).

No fitting job is currently active. Private diagnostic006 has been submitted for the required source-attribution and order-definition comparison. This is cloud inference, not additional training. Do not confuse completion of fitting with model acceptance. Older running-status notes below are historical.

## Next manual step

Check the diagnostic without submitting a duplicate:

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-adapter-diagnostic-006
```

After COMPLETE:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-adapter-diagnostic-006 -p results/pdf_adapter_006_v1
```

Read status.json, protocol.json, base.json and adapter008.json in the downloaded pdf_adapter_006 folder. Require 16 matching IDs in each answer file and no truncation. Compare every answer with the frozen evidence and rubric in notebooks/pdf_adapter_eval_006. Especially inspect minimum selling price, unidentified source identity, missing charts and unsupported current claims. Record the result before proposing another fitting run. Do not run the evaluator or trainer on the laptop.

---

Latest live check: all 53 optimizer steps of run 008 finished (one epoch; 35.9 minutes of fitting). Kaggle still reports running while post-training validation and answer/reload checks remain. The full job and quality review are not complete.

# Current status: run 008 is running

Private cloud run008 has been submitted with212 training examples from selected material in ten PDFs. GPU T4 x2 allocation was verified, and optimizer logs now confirm training reached epoch0.25 (about25% of this run's single epoch). This is run progress, not25% of total project completion. Diagnostic005 has completed and failed its quality gate: sell-limit direction and unidentified-source attribution remain wrong. See [diagnostic findings](PDF_ADAPTER_005_RESULTS.md). The60 previously staged training records are now included in run008. See [latest checkpoint and manual commands](CHECKPOINT_008.md) and [frozen run plan](PDF_SFT_008_PLAN.md). All older checkpoints below are historical where inconsistent.

---

# Latest checkpoint â€” 23 September 2026

**Run 007 completed on Kaggle; the full model and product remain unfinished.** All downloaded artifact checks passed, including identical answers after adapter reload. Fitting took 22.6 minutes on a Tesla T4. Read [the results and quality decision](PDF_SFT_007_RESULTS.md).

The 136 training records cover selected material from eight PDFs, not the complete library. Twenty paired development answers were reviewed: source identification and citation-support errors remain, and there is no clear reliable advantage over the base model. The adapter is saved for diagnosis and is not promoted.

Private diagnostic 005 was submitted to compare base and adapter007 on the same 16 frozen retrieval cases (32 answers). It performs cloud inference only, with no fitting. Its URL is https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-adapter-diagnostic-005 . Submission is not completion; check its live status. Do not duplicate the job.

Another 60 training and 32 development-evaluation records across DP05, DP10, DP17 and DP16 are reviewed and staged, but unfitted. See [coverage](PDF_COVERAGE_LEDGER.md) and [acceptance criteria](PDF_MODEL_ACCEPTANCE_PROTOCOL.md). Remaining work includes unresolved PDF coverage, stronger training examples based on diagnosed failures, independent assessment, and separate market/paper-trading validation. There is no defensible completion date for the whole product yet.

---

Earlier instructions/status below are historical where inconsistent.

Staged curriculum update: 60 additional training and 32 development-evaluation records are prepared across DP05, DP10, DP17 and DP16. They are not part of the running job. See [coverage ledger](PDF_COVERAGE_LEDGER.md) and [completion criteria](PDF_MODEL_ACCEPTANCE_PROTOCOL.md).

# Historical checkpoint before run 007 completed

Private Kaggle run **007 is submitted and running at the latest checked status**. It starts a fresh Qwen3-8B adapter from the fixed base revision and uses 136 examples from selected material in eight PDFs. No laptop fitting. Submission/running status does not prove that the optimizer has finished; inspect the saved cloud artifacts before claiming completion.

Automatic retrieval diagnostic 004 completed and all 32 answers were reviewed. Evidence improved many answers, but an unidentified-source attribution failure and a sell-limit explanation error remain. Read `PDF_RETRIEVAL_004_RESULTS.md`. The next training design is recorded in `PDF_SFT_007_PLAN.md`.

An additional DP05 technical-analysis batch is staged: 24 train, four validation and four development-test records in `pdf_training_dp05_expanded.json`. It is **not** included in run 007. See `DP05_EXPANSION_REVIEW.md` for reviewed pages, corrections and exclusions.

No adapter is approved as an expert or finished trading model. Full-library coverage, independent model assessment, market prediction and paper-trading validation remain unfinished. Earlier status statements below are historical where inconsistent.

---

# Previous checkpoints

# Project progress ? 23 September 2026

**Full training objective and product: incomplete. No training is currently running.**

Six limited PDF-derived fine-tuning runs completed on Kaggle using Qwen/Qwen3-8B. The latest cumulative dataset contains 100 reviewed training examples from seven PDFs (DP01, DP03, DP05, DP06, DP07, DP17, DP19). This is selected material, not every page of those PDFs or the whole library. The collection contains 22 files representing 19 distinct works; full review and playlist review remain unfinished.

## What has finished

- Cloud fitting runs 001?006; adapters and execution records are saved locally. This proves the cloud workflow executes, not that the resulting model is reliable.
- Diagnostics 002 and 003; all 72 and 32 respective answers were reviewed. See [diagnostic 002](PDF_EVALUATION_002_RESULTS.md) and [diagnostic 003](PDF_EVALUATION_003_RESULTS.md).
- An offline evaluation workbench: checked source search with PDF-page links, historical BTC/ETH charts, deterministic calculators, and experiment reports. Launch with `python -m workbench.server`, then visit http://127.0.0.1:8765.
- Fifteen backend/calculation tests passed without fitting a model. Browser checks verified source search, historical snapshot rendering and all three calculators.

## Why training is not accepted as complete

The adapters still make serious arithmetic and reasoning errors, and have not demonstrated reliable improvement over the base model. Run 004's earlier narrow promotion is superseded. No adapter is approved for the product.

Diagnostic 003 showed that supplying checked evidence corrects specific failures, including notional sizing and a reversed imbalance sign. Evidence was manually matched, often including the correct answer, so this is not proof of automatic retrieval, independent accuracy or profitable trading.

## Work now prepared

A 16-case automatic retrieval diagnostic is prepared locally using the actual workbench search over reviewed training adaptations. All 12 supported development questions retrieved an expected example among the six results. Four additional questions test missing sources, missing charts, current information and unsupported profit claims. This is a small development check, not model-answer accuracy. The cloud inference job for this diagnostic has **not** been submitted. No model was fitted during this preparation.

## Remaining

1. Evaluate the automatically retrieved context on Kaggle and check every answer and citation; compare with the base without retrieved context.
2. Broaden reviewed PDF coverage and fix dataset/training design before further fitting. Text examples do not teach the original chart images.
3. Freeze and pass a broader independent assessment before accepting the educational model.
4. Prepare point-in-time multi-coin data and evaluate prediction with costs, liquidity and market regimes. Two-coin historical data does not meet whole-market coverage.
5. Pass the separate gate before building live research/paper-trading agents. No real-order capabilities.

Small fitting runs took about 1?8 minutes each, excluding setup, downloads and evaluation. Those timings do not predict completion of the full product. A defensible completion date is not available while quality and coverage remain unresolved.

All fitting stays on authorized cloud compute. The offline workbench performs no model fitting or inference. Read [the manual handover](MANUAL_TRAINING_HANDOVER.md) for continuation steps.



