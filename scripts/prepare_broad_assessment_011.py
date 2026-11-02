"""Freeze adapter010 versus same-prompt base regression assessment, cloud only."""
import ast
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'notebooks/pdf_broad_eval_011'

def main():
    assert not OUT.exists(), 'Do not overwrite frozen experiment'
    prior=ROOT/'notebooks/pdf_broad_eval_010'
    source=(prior/'evaluate.py').read_text(encoding='utf8')
    prompt=json.loads((ROOT/'data/pdf_sft_batch_010/train.jsonl').read_text(encoding='utf8').splitlines()[0])['messages'][0]['content']
    tree=ast.parse(source)
    lines=source.splitlines(keepends=True)
    assignments=[n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('system','effective_system') for t in n.targets) and isinstance(n.value,ast.Constant)]
    for n in sorted(assignments,key=lambda n:n.lineno,reverse=True):
        name=n.targets[0].id
        lines[n.lineno-1:n.end_lineno]=[' '*n.col_offset+name+' = '+repr(prompt)+'\n']
    source=''.join(lines).replace('pdf_broad_010','pdf_broad_011').replace('pdf_sft_009','pdf_sft_010').replace('adapter009','adapter010')
    source=source.replace('6fdb8686e878e8d027646bfeb34df7bd859eb702a420bfe2218a6ef29ff4d503','48d2664db5b46246ee98bfd688318b2d28a6f14be0a10892117c6303ca5fc8bf')
    source=source.replace('concise_tools','conditional_evidence')
    ast.parse(source)
    meta=json.loads((prior/'kernel-metadata.json').read_text())
    meta.update(id='waizimran/crypto-qwen3-pdf-broad-check-011',title='Crypto Qwen3 PDF Broad Check 011',kernel_sources=['waizimran/crypto-qwen3-pdf-sft-010'])
    protocol=dict(purpose='Evaluate trained010 under explicit scope gate and its training-time conditional prompt against identically prompted base.',
        cases=100,model_invocations_per_model=50,deterministic_routes_per_model=50,
        independence='Exposed development regression: reuses broad010 cases which informed SFT010. Not final acceptance.',
        decision_rule='No promotion on these cases alone. Review all generated responses for supported conclusions, citation entailment, polarity and abstention. Report routes separately. Require zero severe fabrication or contradiction; compare with base before more fitting.',
        training_executed=False,production_approved=False,
        prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest(),code_sha256=hashlib.sha256(source.encode()).hexdigest(),
        rubric='research/PDF_BROAD_010_RUBRICS.json; remains outside cloud inference')
    OUT.mkdir()
    for name,value in [('evaluate.py',source),('kernel-metadata.json',json.dumps(meta,indent=2)),('review_protocol.json',json.dumps(protocol,indent=2))]:
        (OUT/name).write_text(value,encoding='utf8')
    print(json.dumps(protocol,indent=2))

if __name__=='__main__':main()
