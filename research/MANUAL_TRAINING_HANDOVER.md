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

# Latest continuation: SFT015 (2026-10-06)

Private version1 submitted successfully. SFT014 completed but failed semantic readiness; see PDF_SFT_014_RESULTS.md. Run015 is a controlled learning-rate reduction, identical108 exercises/prompt/splits. No015 background monitor configured; launch command blocked by execution policy. Cloud job runs independently. No local model execution.

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-015
tmp\kaggle_client\Scripts\python.exe scripts/download_pdf_artifacts.py --batch 015 --dest results/pdf_sft_015_manual
python scripts/audit_pdf_run.py --batch 015 --results results/pdf_sft_015_manual/pdf_sft_015
python scripts/audit_structured_pdf_012.py --batch 015 --results results/pdf_sft_015_manual/pdf_sft_015
```

Download after completion; audit after completed_training_human_evaluation_pending. Review all baseline/adapted answers for source support, arithmetic, polarity, repetition and unnecessary abstention. Compare014 and same-run base. Format compliance and falling loss do not prove correctness. If severe errors persist, stop repeating this recipe and investigate evidence handling/data distribution. Independent acceptance and whole-library disposition remain incomplete. No paid/public/live-order scope.

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

# Latest handover: actual SFT010 submitted and running (2026-09-29)

## What changed

Broad010 is complete and failed grounded-answer checks; see PDF_BROAD_010_RESULTS.md. SFT010 uses278 training examples from selected sections of ten PDFs, including48 new relevance/polarity contrasts, plus42 validation and50 development test examples. Source permission remains user-attested private training permission. This is not full-library completion or financial performance validation.

The private cloud job automatically installs pinned dependencies, loads the pinned base model on GPU, generates baseline answers, fits one epoch, saves its adapter, evaluates, reloads and evaluates again. No local fitting is allowed. The first submission was rejected because its source exceeded1MB; the identical payload was losslessly compressed and version1 was accepted. Static preflight verified the decompressed payload against every local split hash.

## Continue manually

From the project directory in PowerShell:

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-010
```

While running, use the private notebook viewer for its current execution/log: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-010 . Do not push another version merely to check progress. Running does not itself confirm fitting has started. After completion or error, download:

```powershell
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-010 -p results/pdf_sft_010_v1
Get-Content results/pdf_sft_010_v1/pdf_sft_010/status.json
```

If status.stage is completed_training_human_evaluation_pending, run this artifact-only audit (no model loading):

```powershell
python scripts/audit_pdf_run.py --batch 010 --results results/pdf_sft_010_v1/pdf_sft_010
```

Read all50 baseline,50 adapted and50 reloaded responses against supplied evidence. Six new test probes have IDs beginning r010-probe; require correct direct polarity, proper abstention for unrelated evidence, supported citations and no invented calculator outputs. Check old cases for regressions. Require reload equality and no truncation; a structural pass or lower validation loss does not establish semantic success. Compare the adapted model against the same-prompt base; if both pass, do not claim training caused an improvement. All these questions are development cases with concept overlap; final independent acceptance is still outstanding.

On failure inspect failure.txt and cloud log. Correct a concrete issue in a new version with provenance preserved; never silently fall back to laptop fitting, paid compute or publication. On success record metrics, GPU, duration, adapter hash and semantic findings in CURRENT_PROGRESS.md, then select a justified next experiment. Do not repeatedly train simply because a job ended. Further work remains authorized within private free-cloud research scope, but no always-on assistant scheduler is configured.

Preparation: scripts/prepare_pdf_run_010.py refuses to overwrite frozen files. Static check: python scripts/preflight_pdf_run.py --batch 010. Never run notebooks/pdf_sft_010/train.py locally. Kaggle official compute guidance: https://www.kaggle.com/docs/efficient-gpu-usage ; sessions and quotas are finite, not unlimited. No new costs authorized.

---

# Latest handover: broad010 submitted, 2026-09-28

Private broader assessment submitted, not additional fitting. Check status and download after completion:

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-broad-check-010
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-broad-check-010 -p results/pdf_broad_010_v1
```

Read frozen protocol `notebooks/pdf_broad_eval_010/review_protocol.json` and local `research/PDF_BROAD_010_RUBRICS.json`. Expect100 cases in each model's concise_tools output. Review all200 responses:25 supported and25 irrelevant model-invoked cases per model, with50 deterministic missing/unknown-source routes reported separately. Check exact IDs, truncation, conclusion, citation support and overreach. These100 cases are25 correlated families, not100 independent final-exam questions. Rubrics were excluded from cloud inputs. No evidence that the entire PDF corpus is learned or an expert achieved.

Use failures to justify specific corrected curriculum additions or a model change. Preserve base-versus-adapter comparison; do not keep training an adapter with no measured advantage. If these answers inform training, they remain development evidence. Independent assessment and full-library disposition remain unfinished. Never execute cloud evaluator locally or change private metadata to public.

---

# Historical handover: concise009 reviewed, 2026-09-28

No cloud job currently active from this workflow. Completed concise009 outputs/log are in `results/pdf_concise_009_v1`; all52 responses read and artifact hashes recorded in `pdf_concise_009/local_artifact_audit.json`. See `research/PDF_CONCISE_009_RESULTS.md`. Concise prompt repairs the adapter's chart citation and unsupported registration detail in these cases; base performs comparably. Preserve adapter009 but provisionally prefer the simpler unmodified base with explicit evidence/calculator context.

Candidate revision, exact prompt, decoding and component hashes are in `research/model_candidate_2026_09_28.json`. Next construct the100-question assessment under `PDF_MODEL_ACCEPTANCE_PROTOCOL.md`, with at least25 missing/ambiguous/stale/contradictory evidence cases and answerable controls. This dataset is not yet constructed. Keep references separate from cloud inference prompts and fitting. Freeze question/rubric/corpus hashes before execution, use only reviewed source material, audit citation support and severe errors manually, and record per-category results. Do not call the old13 cases independent. If later training uses assessment failures, mark that assessment exposed and prepare fresh final questions. All inference/fitting stays private and cloud-only.

Part3 follows successful model/source-grounding gates and explicit authorization: read-only research agents and simulated/paper evaluation, never real orders. Remaining full-library coverage and numerical prediction gates are separate unfinished work.

---

# Historical handover: reviewed tool008, submitted concise009 (2026-09-27)

All52 tool008 responses reviewed; report in `research/PDF_TOOL_008_RESULTS.md`. JSON structure audit saved alongside results. UTF-8 download retry recovered the log. Tool context corrects the main price-rule error, but adapter citation/unsupported-detail failures remain. No new fitting occurred.

Next private job: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-concise-check-009 . Check and download using:

```powershell
$env:PYTHONUTF8='1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-concise-check-009
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-concise-check-009 -p results/pdf_concise_009_v1
```

Run the output command after completion. Review all13 answers in each of four original_tools/concise_tools base/adapter files. Follow the frozen `notebooks/pdf_concise_eval_009/review_protocol.json`. Require supported citations, no invented legal procedures, correct comparisons and no execution guarantees. Compare which model benefits; do not assume the adapter is preferable. This is exposed development evaluation, not independent acceptance. Do not automatically start another diagnostic or fitting run without recording the decision and addressing remaining corpus/assessment gaps.

---

# Historical handover: cloud model diagnostic, 2026-09-27

Private job version 1 submitted: https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-tool-check-008 . Existing adapter009 is being evaluated, not fine-tuned. Local preflight passed; completion and performance are not yet established. Never run `notebooks/pdf_tool_eval_008/evaluate.py` locally.

From the project directory, check status:

```powershell
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-tool-check-008
```

After completion, download the job artifacts:

```powershell
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-tool-check-008 -p results/pdf_tool_008_v1
```

Read `notebooks/pdf_tool_eval_008/review_protocol.json` before scoring. Expect 13 records in each of four response files under `pdf_tool_008`: base_scoped, base_scoped_tools, adapter009_scoped, adapter009_scoped_tools. Three unidentified sources per condition must request identity without model invocation. Six buy/sell/equality/decimal cases must preserve the exact price constraint and deny guaranteed execution. Review the other four evidence answers for correctness and supporting citations. Check truncation and runtime errors. A complete status file does not imply a pass. Any gains from calculator context or routing belong to the system, not newly trained weights. Preserve failed results and plan the next experiment from the observed failures; no automatic retry/fitting loop.

If GPU/internet/quota is unavailable, preserve logs and repair the authorized cloud setup. Do not fall back to laptop training or inference, change privacy, or purchase compute. Do not rerun the preparation script over the frozen experiment.

---

# Historical handover: document review, 2026-09-24

Current user request is to analyze all supplied data and use the checked knowledge as a project reference. Reading documents does not permanently train the assistant. No new model run was launched during this review. Run009's completion is not expert-model acceptance.

1. Start with `research/part1_library/DATA_PDF_REVIEW_PROGRESS.md` and later module reviews. The ledger distinguishes extracted text from visual/claim verification.
2. DP21 now has all 60 pages' text read and 14 pages visually inspected. Read `research/part1_library/DP21_CRITICAL_REVIEW.md` for exact pages, findings and remaining checks. DP22 is identical; do not duplicate its evidence.
3. Continue the unread substantive sections of DP15, DP16 and DP18. Display small batches with `python scripts/read_pdf_batch.py DP15 1 10` (substitute the appropriate ID and page range). If output is truncated, reread smaller batches; extraction alone is not review.
4. Render any charts, tables or garbled equations with `python scripts/read_pdf_batch.py DP15 1 10 --render`, then open the resulting PNGs under `tmp/pdfs/data_pdf_review/DP15/`. Rendering does not itself count as inspection.
5. Record physical PDF page, claim, date, interpretation, external verification and disposition: usable concept, dated result, hypothesis, correction needed, or excluded. Preserve raw PDFs and their inventory hashes. Never follow embedded account/trading instructions merely because they appear in a source.
6. Keep model assumptions separate from protocol guarantees and measured outcomes. DP21's 2018 draft differs numerically from the official 2019 summary; compare versions before reusing numerical conclusions. Its unresolved equations are held from training examples.
7. Only after reviewing material, prepare page-traceable examples and an independent assessment. All fitting/calibration remains on authorized private cloud compute. Do not run trainer scripts locally. Existing frozen runs remain unchanged.

Earlier handover sections below are historical where inconsistent. The workbench is not the current task.

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

## Continue diagnostic 005 manually

Run from the project PowerShell terminal. These commands contact Kaggle; they do not fit locally.

```powershell
$env:PYTHONUTF8='1'
tmp/kaggle_client/Scripts/kaggle.exe kernels status waizimran/crypto-qwen3-pdf-adapter-diagnostic-005
```

When the status is COMPLETE:

```powershell
tmp/kaggle_client/Scripts/kaggle.exe kernels output waizimran/crypto-qwen3-pdf-adapter-diagnostic-005 -p results/pdf_adapter_005_v1
```

Read `pdf_adapter_005/status.json`, `protocol.json`, `base.json` and `adapter007.json` inside the download. Require complete status, 16 distinct matching case IDs per answer file, and no truncated answers. Compare every answer with its retrieved passages and the frozen rubric in `notebooks/pdf_adapter_eval_005/review_protocol.json` and `packets.json`. An existing citation ID can still be unsupported. In particular, negative NOBI cannot identify an unspecified paper, and a sell limit specifies a minimum acceptable sale price. Record errors and base/adapter differences in a new results report before choosing the next training design. Do not count this exposed diagnostic as an independent test.

If the job fails, preserve the log, diagnose the exact failure and create a versioned repair. Do not launch local inference or training. Keep any new Kaggle notebook private. Do not repeat successful jobs just because earlier handover sections mention them.

The run007 audit and coverage update have already passed. To repeat the nonfitting checks if files change:

```powershell
python scripts/audit_pdf_run.py --batch 007 --results results/pdf_sft_007_v1/pdf_sft_007
python scripts/validate_staged_curriculum.py --completed-batch 007 --active-batch none
```

Earlier instructions/status below are historical where inconsistent.

## New checks and staged curriculum

After downloading a completed run 007, run the artifact audit locally (it does not import or fit a model):

```powershell
python scripts/audit_pdf_run.py --batch 007 --results results/pdf_sft_007_v1/pdf_sft_007
```

Read every paired answer after the structural checks pass. A recognized citation ID alone does not establish support. The script writes `local_artifact_audit.json` and requires identical adapted/reloaded responses.

Four additional reviewed modules are staged: DP05 chart/indicator material, DP10 corrected risk examples, DP17 execution/indicators, and DP16 selected signature/custody foundations. Together they contain 60 training, 16 validation and 16 development-test records. None is fitted by run 007. Validate and regenerate the per-PDF coverage ledger without fitting:

```powershell
python scripts/validate_staged_curriculum.py --completed-batch 006 --active-batch 007
```

Only after execution of run 007 has actually completed may you change those arguments to `--completed-batch 007 --active-batch none`. Completion records execution, not model approval. Review `PDF_MODEL_ACCEPTANCE_PROTOCOL.md` before declaring training finished.


# Historical checkpoint before run 007 completed

Private Kaggle run **007 is submitted and running at the latest checked status**. It starts a fresh Qwen3-8B adapter from the fixed base revision and uses 136 examples from selected material in eight PDFs. No laptop fitting. Submission/running status does not prove that the optimizer has finished; inspect the saved cloud artifacts before claiming completion.

Automatic retrieval diagnostic 004 completed and all 32 answers were reviewed. Evidence improved many answers, but an unidentified-source attribution failure and a sell-limit explanation error remain. Read `PDF_RETRIEVAL_004_RESULTS.md`. The next training design is recorded in `PDF_SFT_007_PLAN.md`.

An additional DP05 technical-analysis batch is staged: 24 train, four validation and four development-test records in `pdf_training_dp05_expanded.json`. It is **not** included in run 007. See `DP05_EXPANSION_REVIEW.md` for reviewed pages, corrections and exclusions.

No adapter is approved as an expert or finished trading model. Full-library coverage, independent model assessment, market prediction and paper-trading validation remain unfinished. Earlier status statements below are historical where inconsistent.

## Check or recover run 007 yourself

Do not run its training script locally. In the project PowerShell terminal:

```powershell
$env:PYTHONUTF8 = '1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-007
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-007 -p results\pdf_sft_007_v1
```

After Kaggle reports completion, inspect `pdf_sft_007/status.json`, `runtime.json`, `dataset_manifest.json`, `result.json`, `baseline_answers.json`, `adapted_answers.json` and `reloaded_answers.json`. Compare every answer and its citation against supplied evidence. Compare local/cloud manifests and adapted/reloaded outputs. A falling loss does not pass the model. Do not restart or submit another job merely because the assistant is unavailable; the saved cloud job runs independently, subject to Kaggle runtime and quota limits.

---

# Previous checkpoints

# Current handover ? 23 September 2026

**Read this checkpoint before the historical notes below.** Six small cloud training runs and diagnostic 003 are complete. No fitting or inference job is currently running. The model has not passed the quality gate. Diagnostic 003's 32 answers were downloaded and reviewed; see `PDF_EVALUATION_003_RESULTS.md`. Earlier running-job statements and narrow adapter approvals below are historical and superseded.

## Use the workbench yourself

1. Open PowerShell in `C:\Users\DELL\Downloads\Billioniare`.
2. Run `python -m workbench.server`.
3. Open http://127.0.0.1:8765 in your browser.
4. Search a concept and use each result's PDF-page link to inspect its source. The search covers only 100 checked adaptations, not whole books.
5. Use Historical charts for local BTC/ETH data. Choose a date, then Inspect snapshot. These are historical descriptions, not trade recommendations.
6. Use Research calculators for explicit hypothetical inputs. Missing stop information must leave position quantity undetermined.
7. Press Ctrl+C in PowerShell to stop the server. Do not expose it to the internet.

## Continue evaluation

The automatic retrieval development check is prepared in `scripts/prepare_retrieval_diagnostic.py`. Running it locally prepares JSON only; it does not fit or invoke a model. It writes frozen evidence packets to `notebooks/pdf_retrieval_eval_004/packets.json` and results to `research/RETRIEVAL_004_PRECHECK.json`. The next cloud model-inference script has not yet been created or submitted. Do not mistake these packets for a running job or trained model.

Before another fitting run, evaluate those automatically retrieved packets in a private Kaggle GPU notebook using the fixed base model revision below. Keep evaluation rubrics out of model prompts. Record every generated answer, retrieved example ID, citation and truncation flag. Compare against identical questions without retrieval. Review support and abstention, not just whether answers sound plausible. These development cases overlap the checked curriculum and cannot establish independent accuracy.

The trained adapters are experimental and no longer approved as continuation parents by default. Preserve all failures. Expand and validate the curriculum before a revised training experiment; use a fresh independent assessment before any success claim. All fitting stays in the cloud. See `CURRENT_PROGRESS.md` for the complete remaining work.

---

# Historical working notes (superseded where inconsistent)

# Continue the PDF training yourself

Last updated: 21 September 2026. This is a working handover, not a claim that the entire PDF library has been trained.

## Current action ? diagnostic 003

Diagnostic 002 completed; all 72 answers were reviewed. See `PDF_EVALUATION_002_RESULTS.md`. Neither trained adapter demonstrated improvement, and both have serious arithmetic and premise-following errors. No adapter is approved for a user-facing product. Historical narrow promotion decisions below are superseded by this review.

The active job is now `waizimran/crypto-qwen3-pdf-evaluation-003`. It performs cloud inference only: 8 cases, 2 evidence conditions, base and adapter 006. Checked context is manually matched. This is not an automatic retrieval test or an untouched accuracy test.

```powershell
$env:PYTHONUTF8 = '1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-evaluation-003
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-evaluation-003 -p results\pdf_evaluation_003_v1
```

Inspect `pdf_evaluation_003/status.json`, `protocol.json`, and four answer files: `base_closed.json`, `base_provided_evidence.json`, `run006_closed.json`, `run006_provided_evidence.json`. Check that supplied values and assumptions survive into the answer, particularly -0.25 imbalance, USD 2,000 notional/USD 60 risk, 20% break-even, and refusal to invent a quantity without stop information. Mark contradictory answers as failures even if they begin correctly. Do not start another fitting run until the findings inform a revised plan.

The new `scripts/research_math.py` provides deterministic calculations only. Verify it without fitting any model:

```powershell
python -m unittest discover -s tests -p test_research_math.py -v
```

It is not yet connected to an agent. Model training, chart understanding, full PDF coverage, independent evaluation and paper-trading integration remain unfinished.

## Latest checkpoint ? 22 September 2026

Run 006 completed and was downloaded, but did not pass review. Read `research/PDF_SFT_006_RESULTS.md`. The earlier run 004 cold-storage pass was too lenient: loss of a backup does not prove loss of a working original key. Adapters remain experimental and no reliable trading model has been established.

The active job is now an inference-only cloud diagnostic:
https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-evaluation-002

It compares base Qwen3-8B, adapter 004 and adapter 006 using identical cases under the old and neutral prompts. It does not train locally or in the cloud. DP04 is staged but not submitted. Older run status tables below are historical snapshots; this checkpoint takes precedence.

```powershell
$env:PYTHONUTF8 = '1'
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-evaluation-002
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-evaluation-002 -p results\pdf_evaluation_002_v1
```

After completion, inspect `pdf_evaluation_002/status.json`, `protocol.json` and all six model/prompt answer files. Compare factual correctness, invented numbers, arithmetic, source handling and truncation case by case. Do not automatically promote the highest-scoring model from this diagnostic; it uses exposed concepts. Preserve failures and freeze an independent assessment before making accuracy claims. No new training job is scheduled automatically.

## Start here

You do not need to wait for an assistant to check or finish an already submitted Kaggle job. Kaggle executes the saved job on its servers. An assistant usage limit does not itself stop that job. Kaggle's own runtime limits, errors and GPU quota can still stop it.

**Never run `train.py`, `pdf_cloud_trainer.py`, or a training notebook on your laptop.** Local preparation scripts described below do not fit models. Keep Kaggle code, datasets and model outputs private.

Project folder: `C:\Users\DELL\Downloads\Billioniare`

Current model: `Qwen/Qwen3-8B`, revision `b968826d9c46dd6066d109eabc6255188de91218`. We train a small LoRA adapter with a four-bit base model. An adapter is a set of learned changes, not the complete base model. It needs the matching base revision to run.

## Current state

| Run | What it contains | Status at this document's update |
| --- | --- | --- |
| PDF SFT 001 | 24 training examples from DP05, DP06, DP17, DP19 | Completed; adapter downloaded and reloaded successfully. |
| PDF evaluation 001 | Eight questions comparing the original base and first adapter | Completed; no clear quality gain. Both made serious calculation errors. |
| PDF SFT 002 | Continues adapter 001; 24 new DP07 on-chain examples plus 24 earlier training examples | Completed; downloaded, hash-checked, reloaded and manually reviewed. Three new answers passed and one was partial; no improvement over parent demonstrated. |
| PDF SFT 003 | Continues adapter 002; 24 new DP01 World Bank examples plus 48 earlier training examples | Completed and downloaded, but rejected for promotion after human review. See `research/PDF_SFT_003_RESULTS.md`. |
| PDF SFT 004 | Corrective DP01 run from accepted adapter 002; one epoch, learning rate 0.00005, and four fresh held-out DP01 questions | Completed, downloaded and narrowly accepted as a continuation parent; see `research/PDF_SFT_004_RESULTS.md`. Serious older errors remain. |
| PDF SFT 005 | Continues accepted adapter 004; adds 24 DP03 training examples and four new DP03 checks | Completed and downloaded, but rejected: only two fresh checks passed and retention worsened. See `research/PDF_SFT_005_RESULTS.md`. |
| PDF SFT 006 | Corrective DP03 run from adapter 004; adds four targeted corrections and four fresh DP03 tests | Private version 1 submitted and running at this document's update. |
| Later DP04 preparation | DP04 text fully read and key figures checked; 24 train, 4 validation and 4 test examples validated locally | Staged in `research/pdf_training_dp04.json`; run DP03 first, then audit it before using DP04. |

Private jobs:

- [Training 001](https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-001)
- [Evaluation 001](https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-evaluation-001)
- [Training 002](https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-002)
- [Training 003](https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-003)
- [Corrective training 004](https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-004)
- [Training 005](https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-005)
- [Corrective training 006](https://www.kaggle.com/code/waizimran/crypto-qwen3-pdf-sft-006)

The status above is a snapshot. See `research/PDF_SFT_002_RESULTS.md` for the detailed result. Use the commands below for the current status of later runs. **Do not submit a duplicate job just because the assistant stops responding.**

Run 003's execution succeeded, but its final adapter failed the human quality gate. Validation loss improved, yet the answer review found a new repetition/truncation failure, an unjustified demand-to-price formula, incomplete address/entity reasoning, and retained NOBI and expected-value errors. Do not use its final adapter or checkpoints as the next parent without a separate documented evaluation. Run 004 restarts from adapter 002 and uses four fresh assessment questions because run 003's questions have been exposed.

DP03 review exclusions matter: inconsistent balance-sheet diagrams on pages 33â€“34, absolute trust/security claims, dated market figures, and outdated network-status statements were not copied as truth. The prepared examples teach corrected distinctions such as addresses versus people, ledger consensus versus reserve backing, dated survey evidence, and CBDC scenario risk. Local validation confirms 32 unique records with the required 24/4/4 split; no model was fitted locally.

DP04 is also staged for a later sequential run. Its examples correct the source's description of miners as transaction signers, account for Bitcoin difficulty adjustment, reject scarcity as a guarantee of token appreciation, and preserve 2014â€“2015 figures as historical. The file is preparation only; it must not skip ahead of DP03 or use an unaudited parent adapter.

## 1. Open PowerShell in the project

Run these lines:

```powershell
Set-Location -LiteralPath 'C:\Users\DELL\Downloads\Billioniare'
$env:PYTHONUTF8 = '1'
```

The project already has a working Kaggle command-line client at `tmp\kaggle_client\Scripts\kaggle.exe`. Authentication is already configured for `waizimran`. Do not paste your API key into chats, notebooks, screenshots or this document.

## 2. Check the active job

```powershell
tmp\kaggle_client\Scripts\kaggle.exe kernels status waizimran/crypto-qwen3-pdf-sft-006
```

- `running` or `queued`: let it continue; check again in several minutes.
- `complete`: download and inspect the artifacts in the next step.
- `error`: download the log and failure files; see troubleshooting below.

An outdated-client warning alone is not failure. This client version has successfully submitted and downloaded our private jobs.

Browser alternative: sign into Kaggle as `waizimran`, open Corrective training 004 above, and inspect its run/log/output information. Labels may change. The saved version must remain private. Do not start an additional interactive GPU session just to inspect a saved run.

## 3. Download the completed job

Use a new folder per run/version so historical evidence remains intact:

```powershell
tmp\kaggle_client\Scripts\kaggle.exe kernels output waizimran/crypto-qwen3-pdf-sft-006 -p results\pdf_sft_006_v1
```

Expected folder inside it: `pdf_sft_006`. Inspect:

```powershell
Get-Content results\pdf_sft_006_v1\pdf_sft_006\status.json
Get-Content results\pdf_sft_006_v1\pdf_sft_006\result.json
Get-Content results\pdf_sft_006_v1\pdf_sft_006\runtime.json
Get-FileHash results\pdf_sft_006_v1\pdf_sft_006\adapter\adapter_model.safetensors -Algorithm SHA256
```

Successful fitting should record `completed_training_human_evaluation_pending`, real training steps/metrics, and an adapter file. A successful upload or package installation is **not** completed training. If a job failed after saving an intermediate checkpoint, retain it but do not call the final run complete.

## 4. Read the answers, not only the loss

```powershell
Get-Content results\pdf_sft_006_v1\pdf_sft_006\parent_answers.json
Get-Content results\pdf_sft_006_v1\pdf_sft_006\adapted_answers.json
Get-Content results\pdf_sft_006_v1\pdf_sft_006\reloaded_answers.json
```

For every answer, compare the response with the reference and cited PDF pages. Record pass, partial, or fail, and explain the exact mistake. Check arithmetic independently with a calculator, including units. A response at the generation limit may be incomplete and cannot receive a full-answer pass. Compare parent and new adapter on the same questions. Check that saving/reloading preserves the answers.

Run 002's predeclared check was at least three of four new application questions correct, without new severe errors on retention questions relative to the parent. It reached three passes and one partial, while the parent had four passes. Four older questions were truncated and exposed a prompt/protocol defect; details are in `research/PDF_SFT_002_RESULTS.md`. They are diagnostic retention checks, not an untouched test. Concepts also overlap training, so this is not a general accuracy estimate.

Do not repeatedly tune against test answers. Once you have inspected them, keep their exposure recorded. Create a fresh independent assessment before making stronger claims. Falling loss alone does not prove useful reasoning, trading performance, or profitability.

## 5. Understand what PDF training means here

We are making reviewed questions and answers from selected PDF passages, then teaching the model those answers. We are not feeding every page blindly into the model. Some supplied books contain wrong calculations, dated statements, unsupported success claims, advertisements, or charts needing visual interpretation.

Workflow for each PDF:

1. Identify the file and its source ID in `tmp/pdfs/data_pdf_review/inventory.json`.
2. Read the relevant text and view its charts in the original PDF.
3. Record useful concepts, errors, dates and qualifications with PDF page numbers.
4. Write clear question/answer examples. Correct errors explicitly; preserve author attribution. Do not silently teach a historical claim as a current fact.
5. Separate training, validation and test examples before fitting. Keep paraphrases and closely related duplicates together. Do not put previous test examples into later training.
6. Include earlier **training** examples in later batches to reduce forgetting; recheck earlier skills afterwards.
7. Build the private cloud script, submit it to Kaggle, download the adapter, and review its answers.
8. Update the coverage ledger. â€œThis PDF contributed examplesâ€ does not mean â€œevery page or chart has been trained.â€

The user attested permission to use these PDFs for training. This is recorded as user permission, not independent proof of each publisher's license. Continue private use and attribution. Do not publish the PDFs or adapters as an automatic next step.

## 6. Read the extracted pages locally

These commands only display text or render images; they do not train:

```powershell
python scripts\read_pdf_batch.py DP07 1 10
python scripts\read_pdf_batch.py DP07 11 20
python scripts\read_pdf_batch.py DP07 21 31
python scripts\read_pdf_batch.py DP07 9 10 --render
```

Rendered images are saved under `tmp\pdfs\data_pdf_review\DP07`. Open them normally. Extraction may lose equations, columns, Urdu text or chart labels. Use the physical PDF page number, not a printed page number that may have a different offset.

## 7. Prepare the next batch

The existing example format is demonstrated in `research/pdf_training_dp07.json`:

```json
{
  "id": "dp01-unique-concept-name",
  "split": "train",
  "source": "DP01",
  "pages": [44, 45],
  "question": "Does a fixed supply alone ensure stable purchasing power?",
  "answer": "No. Demand can change even when supply is constrained, so a fixed supply does not guarantee stable purchasing power.",
  "adaptation": "Paraphrase of the source's demand and volatility discussion."
}
```

Put multiple records inside a JSON array. Use unique IDs. `split` must be `train`, `validation`, or `test`. Keep a separate file per prepared source/batch and leave earlier files unchanged. The general-purpose continuation builder is `scripts/prepare_pdf_run.py`. It verifies the completed parent, adapter hash, frozen parent data, source PDF hashes, IDs, exact question duplication and split structure; it then embeds the cumulative payload and generates private Kaggle metadata. It cannot determine whether new answers are factually correct, so manually review them first. Do not manually edit the large embedded payload inside a generated cloud script.

Example showing the original run 003 preparation based on completed run 002:

```powershell
python scripts\prepare_pdf_run.py --batch 003 --parent-batch 002 --parent-results results\pdf_sft_002_v1\pdf_sft_002 --examples research\pdf_training_dp01.json
python -m py_compile notebooks\pdf_sft_003\train.py
tmp\kaggle_client\Scripts\kaggle.exe kernels push -p notebooks\pdf_sft_003
```

The original builders have fixed purposes:

```powershell
python scripts\build_pdf_training_batch.py
python scripts\build_pdf_notebook.py
```

These rebuild **001**, not a new batch. `python scripts\build_pdf_continuation.py` rebuilds **002** specifically. Do not use these commands to overwrite a later run or assume they automatically read every PDF.

`prepare_pdf_run.py` now also accepts `--epochs` and `--learning-rate`. Run 004 used `--epochs 1 --learning-rate 0.00005` after run 003 failed its quality gate. A changed setting is a new recorded run and requires fresh held-out questions; do not repeatedly tune against already inspected test answers.

## 8. Submit only a newly prepared, checked run

For the already prepared 002, the submission command was:

```powershell
tmp\kaggle_client\Scripts\kaggle.exe kernels push -p notebooks\pdf_sft_002
```

**Do not repeat that command while 002 is running or after it succeeds unless deliberately creating a new version.** A push executes the cloud job. Future runs need their own folder, kernel ID, correct parent adapter and dataset. Metadata must contain `is_private: true`, GPU enabled, internet enabled, and the correct private parent in `kernel_sources`.

Shared settings are Qwen3-8B, four-bit NF4, rank-8 LoRA on query/value projections, microbatch 1, gradient accumulation 4, and seed 217. Runs 002 and 003 used two epochs at learning rate 0.0001. Corrective run 004 uses one epoch at 0.00005. Each continuation starts a new optimizer while loading accepted adapter weights; that is continuation of model weights, not exact resumption of the prior optimizer session.

## 9. Troubleshooting

| Symptom | What to do |
| --- | --- |
| No GPU / CPU-only runtime | Check Kaggle account verification and available GPU quota; select a GPU for the saved run. Never switch to laptop training. |
| DNS/model download/package failure | Confirm internet is enabled for the notebook, inspect the log, then retry only after addressing the cause. |
| Out of memory | Keep microbatch 1, four-bit loading and checkpointing; inspect the sequence lengths and GPU allocation. Do not silently truncate answers. A changed configuration is a new recorded experiment. |
| Parent adapter not found | Check `kernel_sources`, parent job completion and attached output structure. Do not silently start from the base model instead. |
| Adapter hash mismatch | Confirm the intended parent version and downloaded file. Do not disable the check to make the script run. |
| Token length assertion | Shorten or split the example at a meaningful boundary, preserve provenance, and rebuild a new dataset version. |
| GPU quota exhausted | Save available results, wait for legitimate quota renewal, or explicitly choose another authorized free cloud runtime. Do not buy compute or evade limits. |
| Download gives a Unicode error | Set `$env:PYTHONUTF8 = '1'` and retry the download. Do not retrain for a local console-encoding problem. |
| Kaggle says complete, but results are bad | Keep the artifact and document failures. Completion is an execution result, not an expertise certificate. |
| Assistant usage limit | Follow this document; the existing Kaggle run can continue. No unattended scheduler for new PDF batches has been installed. |

## 10. Files to preserve and update

- `Data PDF`: original files; leave unchanged.
- `research/pdf_training_examples.json`: frozen first batch.
- `research/pdf_training_dp07.json`: new on-chain examples.
- `data/pdf_sft_batch_001` and `data/pdf_sft_batch_002`: exact prepared data and manifests.
- `notebooks/pdf_sft_001` and `notebooks/pdf_sft_002`: submitted private cloud code.
- `results`: immutable downloaded logs, adapters and metrics, separated by run/version.
- `research/PDF_SFT_001_RESULTS.md`: first run's honest quality assessment.
- `research/part1_library/DATA_PDF_REVIEW_PROGRESS.md`: review coverage and source problems; older status statements may be superseded by newer entries.
- This document: update active job, completed step, result path and next action after each milestone.

There are 22 uploaded files but 19 distinct works after exact/near-duplicate grouping: DP02 duplicates DP01, DP22 duplicates DP21, and DP20 is substantially the same paper as DP19. Do not count duplicate copies as independent knowledge or let them cross train/test boundaries.

Remaining work includes broader source review, more representative examples, visual interpretation of charts, independent evaluation and simulated market testing. Qwen3-8B here is text-only: chart images have not been visually learned by feeding these text examples. Neither these runs nor this handover authorize real orders or demonstrate profitable trading.



