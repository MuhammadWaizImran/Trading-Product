"""Freeze replay of diagnostic 004 for base vs adapter 007; no local ML."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'notebooks/pdf_retrieval_eval_004'
out = ROOT / 'notebooks/pdf_adapter_eval_005'
assert not out.exists(), 'Do not overwrite a frozen diagnostic.'
code = (source / 'evaluate.py').read_text(encoding='utf8')
code = code.replace('pdf_retrieval_004', 'pdf_adapter_005').replace('pdf_sft_006', 'pdf_sft_007')
code = code.replace("for condition in ['closed','retrieved']:", "from peft import PeftModel\nassert hashlib.sha256((root/'adapter/adapter_model.safetensors').read_bytes()).hexdigest() == '98fd7f25a9f2dc9b3518e7a742bd805ccbc79d67a14d8abe872d07559a304f99'\nfor condition in ['base','adapter007']:\n    if condition == 'adapter007':\n        base = PeftModel.from_pretrained(base, root/'adapter', is_trainable=False)")
code = code.replace("if condition=='retrieved':", 'if True:')
code = code.replace('exposed development diagnostic; automatic keyword retrieval from checked training adaptations; no fitting', 'Exposed diagnostic 004 replay with identical frozen evidence for base and adapter007; no fitting; not independent acceptance')
code = code.replace('Repairs ambiguous source context and inadequate output length in the first check.', 'Replays all 16 diagnostic 004 packets against base and adapter007 with identical prompts.')
compile(code, str(out / 'evaluate.py'), 'exec')
metadata = json.loads((source/'kernel-metadata.json').read_text())
metadata.update(id='waizimran/crypto-qwen3-pdf-adapter-005', title='Crypto Qwen3 PDF Adapter Diagnostic 005', kernel_sources=['waizimran/crypto-qwen3-pdf-sft-007'])
out.mkdir()
(out/'evaluate.py').write_text(code, encoding='utf8')
(out/'kernel-metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf8')
(out/'packets.json').write_bytes((source/'packets.json').read_bytes())
protocol = {'purpose':'Check unresolved source identity and sell-limit errors; compare all 16 existing diagnostic cases', 'conditions':['base','adapter007'], 'answers':32, 'training':False, 'independent_test':False, 'packet_sha256':hashlib.sha256((out/'packets.json').read_bytes()).hexdigest(), 'code_sha256':hashlib.sha256(code.encode()).hexdigest(), 'decision':'Do not promote if unidentified-source attribution, sell-limit direction, missing-data fabrication, unsupported citations or truncation remain. Require clear supported-answer improvement over identically prompted base before continuing this adapter. Even a pass requires independent assessment.'}
(out/'review_protocol.json').write_text(json.dumps(protocol, indent=2), encoding='utf8')
print(json.dumps(protocol, indent=2))
