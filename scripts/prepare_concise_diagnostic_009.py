"""Prepare a cloud-only prompt diagnostic; no local model execution."""
import ast
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
prior=ROOT/'notebooks/pdf_tool_eval_008'
out=ROOT/'notebooks/pdf_concise_eval_009'
assert not out.exists(), 'Refuse to overwrite frozen experiment'
source=(prior/'evaluate.py').read_text(encoding='utf8').replace('pdf_tool_008','pdf_concise_009')
source=source.replace("for mode in ['scoped','scoped_tools']:","for mode in ['original_tools','concise_tools']:")
source=source.replace("if mode=='scoped_tools' and case.get('tool_args'):","if case.get('tool_args'):")
needle="                messages=[dict(role='system',content=system),dict(role='user',content=question)]"
replacement="""                effective_system=system
                if mode=='concise_tools':
                    effective_system='Explain only what the supplied evidence and verified calculator establish. Answer in at most three short sentences. State the direct answer first. Include the exact supporting evidence ID in square brackets. Preserve calculator comparisons exactly. A price constraint never guarantees execution, whether satisfied or not. Do not add legal procedures, registration requirements, market facts or other details absent from the evidence. If evidence is insufficient, say precisely what is missing. Do not repeat the question or offer general background.'
                messages=[dict(role='system',content=effective_system),dict(role='user',content=question)]"""
assert needle in source
source=source.replace(needle,replacement)
source=source.replace("model_invoked=decision['model_allowed'],route_status=decision['status']", "model_invoked=decision['model_allowed'],prompt_condition=mode,route_status=decision['status']")
ast.parse(source)
protocol=json.loads((prior/'review_protocol.json').read_text())
protocol.update(modes=['original_tools','concise_tools'],code_sha256=hashlib.sha256(source.encode()).hexdigest(),
    decision='Read all 52 responses. Concise mode must retain all six correct price comparisons and deny guaranteed execution, cite each supported affirmative answer, omit unsupported legal/procedural assertions and preserve source routing. Compare base and adapter; no promotion or new fitting on loss alone. Cases are exposed development evidence.',
    prompt_change=replacement)
meta=json.loads((prior/'kernel-metadata.json').read_text())
meta.update(id='waizimran/crypto-qwen3-pdf-concise-check-009',title='Crypto Qwen3 PDF Concise Check 009')
assert meta['is_private'] and meta['enable_gpu']
out.mkdir()
for name,value in [('evaluate.py',source),('review_protocol.json',json.dumps(protocol,indent=2)),('kernel-metadata.json',json.dumps(meta,indent=2))]:
    (out/name).write_text(value,encoding='utf8')
print('Frozen 52-response concise/evidence-only cloud comparison; no local inference or fitting.')
