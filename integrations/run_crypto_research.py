"""Isolated Groq research launcher. No training or order execution."""
import argparse
from copy import deepcopy
from datetime import date
import json
import os
from pathlib import Path
import re
import sys

# Do not send traces to an inherited external LangSmith project.
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGSMITH_TRACING"] = "false"

BASE = Path(__file__).resolve().parent
ENDPOINT = "https://api.groq.com/openai/v1"


def build_config(model):
    from tradingagents.default_config import DEFAULT_CONFIG
    config = deepcopy(DEFAULT_CONFIG)
    config.update(
        llm_provider="groq", quick_think_provider="groq", deep_think_provider="groq",
        backend_url=ENDPOINT, quick_think_backend_url=ENDPOINT,
        deep_think_backend_url=ENDPOINT,
        quick_think_llm=model, deep_think_llm=model,
        max_debate_rounds=1, max_risk_discuss_rounds=1,
        max_tool_rounds=2, max_recur_limit=60, llm_max_retries=0,
        max_tokens=2048, checkpoint_enabled=False,
        results_dir=str(BASE / "runtime/reports"),
        data_cache_dir=str(BASE / "runtime/cache"),
        memory_log_path=str(BASE / "runtime/memory.md"),
        output_language="English",
    )
    return config


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["offline", "check", "research"], default="offline")
    parser.add_argument("--model", default="openai/gpt-oss-20b")
    parser.add_argument("--symbol", default="BTC-USD")
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Z0-9]{2,20}-USD", args.symbol):
        parser.error("Use a data-provider crypto symbol such as BTC-USD; this is not a futures contract.")
    if date.fromisoformat(args.date) > date.today():
        parser.error("Future dates are not supported.")
    config = build_config(args.model)
    from tradingagents.graph.trading_graph import TradingAgentsGraph
    if args.mode == "offline":
        print(json.dumps({"status": "imports_and_config_ok", "provider": "groq",
                          "model": args.model, "asset_type": "crypto",
                          "network_calls": 0, "order_execution": False}, indent=2))
        return 0
    if not os.getenv("GROQ_API_KEY"):
        print("Missing GROQ_API_KEY. Use the secure PowerShell launcher.")
        return 2
    from openai import OpenAI
    client = OpenAI(api_key=os.environ["GROQ_API_KEY"], base_url=ENDPOINT,
                    max_retries=0, timeout=30)
    try:
        models = {m.id for m in client.models.list().data}
        if args.model not in models:
            print("Requested model is not listed for this account. Check Groq model permissions.")
            return 2
        print("Groq authentication accepted; requested model is listed. Inference not yet verified.")
        if args.mode == "check":
            return 0
        print("Partial crypto research: market, social and news only; token fundamentals are not implemented.")
        graph = TradingAgentsGraph(selected_analysts=("market", "social", "news"),
                                   config=config, debug=False)
        _, signal = graph.propagate(args.symbol, args.date, asset_type="crypto")
        print(f"Research completed. Unvalidated rating: {signal}. Reports: {config['results_dir']}")
        return 0
    except Exception as exc:
        # Never dump SDK exceptions, request headers or credentials.
        print(f"Operation failed ({type(exc).__name__}); check connectivity, quota and model access.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
