# TradingAgents + Groq research setup

Prepared 2026-10-28. Upstream: https://github.com/TauricResearch/TradingAgents
Pinned checkout: `c4544913a14ed3df5f1ed7b9e8483270ce20682a` (Apache-2.0).

## What this gives us

A separate agent framework with market, news, social and fundamentals analysts, researcher debate and a risk review. Upstream has native Groq configuration and accepts `asset_type="crypto"`. This is a useful experimental foundation, not a pretrained crypto expert or an accepted trading strategy. Crypto support does not establish complete tokenomics/on-chain coverage: several upstream fundamentals tools and prompts remain company/financial-statement oriented.

Our Qwen3-8B PDF adapter is NOT loaded here. The starter model is Groq-hosted `openai/gpt-oss-20b`, listed in Groq's current production catalog: https://console.groq.com/docs/models . It is a low-cost workflow-test candidate, not a performance winner. Account access, tool calling and output quality still require verification. Use `-Model` to select another available model after evaluation.

This launcher researches one explicit data-provider crypto symbol. It does not scan every coin, identify guaranteed pumps, validate Binance futures contracts, calculate a verified executable futures setup, place orders or provide continuous alerts. No exchange API credentials are needed. No local fitting or inference is performed; local code orchestrates remote Groq calls and public data retrieval.

The launcher excludes the company-fundamentals analyst until crypto-specific fundamental tools are implemented. Reports therefore cover market/social/news research and debate only; they are incomplete for the product's full-analysis requirement.

## Secure first use

1. Revoke the Groq key shared in chat and generate a replacement at https://console.groq.com/keys . Do not paste the replacement into chat or source files.
2. Open PowerShell in the project directory.
3. Run the offline import/config check:

   `powershell -NoProfile -File .\integrations\Start-CryptoResearch.ps1 -Mode offline`

4. Verify credentials and model listing (no completion request):

   `powershell -NoProfile -File .\integrations\Start-CryptoResearch.ps1 -Mode check`

   Enter the replacement key at the hidden prompt. It is passed through the child process environment, never a command argument or saved file, then removed/restored on exit.

5. Confirm free quota/account spending controls in Groq before inference. Once satisfied, launch one research job:

   `powershell -NoProfile -File .\integrations\Start-CryptoResearch.ps1 -Mode research -Symbol BTC-USD`

   Substitute a supported provider symbol such as ETH-USD. BTC is a smoke-test example, not a restricted product universe or a recommendation. USD price data is not Binance USDT perpetual data.

6. Inspect `integrations/runtime/reports`. Every rating remains UNVALIDATED research. Verify timestamps, source coverage, numerical calculations and unsupported claims before any product integration. Missing data must not be treated as completed analysis. Ctrl+C stops a foreground run; this is not a background service.

API/model access checks do not prove successful inference. Two tool rounds per analyst, one research/risk debate round, 2048 output tokens per call, zero automatic LLM retries and graph recursion 60 limit work; these are NOT a dollar spending cap or guaranteed run duration. Rate limits and truncation can interrupt a run. Reports and cache remain private/ignored; PDFs are not sent by this launcher.

## Recreate the environment

Python 3.11 is isolated under `integrations/.venv-tradingagents`; the project's existing environment is unchanged.

```powershell
git clone https://github.com/TauricResearch/TradingAgents integrations/TradingAgents
git -C integrations/TradingAgents checkout c4544913a14ed3df5f1ed7b9e8483270ce20682a
uv venv --python 3.11 integrations/.venv-tradingagents
uv pip install --python integrations/.venv-tradingagents/Scripts/python.exe -e integrations/TradingAgents
```

## Main product status and next work

Run020 is complete; no new training job was started for this integration. Its 47/50 adapter format compliance is not trading accuracy; source-identification failures prevent promotion. Keep source guards and independent evaluation in the main product. After this isolated workflow passes an authenticated smoke test, assess data coverage, grounded answers and cost before proposing integration. Broad discovery, futures-specific data, continuous monitoring and alerts remain separate unfinished requirements.

The exposed key was not stored or used. Authenticated Groq and complete research execution remain unverified until the secure credential step is completed.

Verification: installation completed; 88-package compatibility check, Python/PowerShell syntax and offline graph import/config checks passed. Dependency versions captured in tradingagents-dependencies.txt. No authenticated inference test has been performed.
