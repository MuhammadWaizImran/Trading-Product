"""Cloud-only paired evidence-format diagnostic; no fitting or new factual material."""
import ast
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
def main():
    out=ROOT/'notebooks/pdf_format_eval_012'
    assert not out.exists(), 'Frozen experiment exists'
    prior=ROOT/'notebooks/pdf_broad_eval_011'
    source=(prior/'evaluate.py').read_text(encoding='utf8')
    node=next(n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='cases' for t in n.targets))
    old=json.loads(ast.literal_eval(node.value.args[0]))
    chosen=['b010-04-supported','b010-06-supported','b010-10-supported','b010-24-supported','b010-16-irrelevant','b010-22-irrelevant']
    cases=[]
    for c in old:
        if c['id'] not in chosen:continue
        for mode in ['qa','declarative']:
            row=deepcopy(c);row['id']=c['id']+'-'+mode
            if mode=='declarative':
                for e in row['retrieved']:
                    e.pop('question',None)
                    e['text']=re.sub(r'^(?:Yes|No)\.\s*','',e.pop('answer'))
            cases.append(row)
    assert len(cases)==12
    lines=source.splitlines(keepends=True)
    lines[node.lineno-1:node.end_lineno]=['cases = json.loads('+repr(json.dumps(cases))+')\n']
    source=''.join(lines).replace('pdf_broad_011','pdf_format_012')
    source=source.replace('on 100 grouped evidence cases','on 12 paired evidence-format cases')
    ast.parse(source)
    meta=json.loads((prior/'kernel-metadata.json').read_text())
    meta.update(id='waizimran/crypto-qwen3-pdf-format-check-012',title='Crypto Qwen3 PDF Format Check 012')
    protocol=dict(purpose='Test whether embedded evidence questions and leading yes/no anchors contribute to polarity and source errors.',
        cases=12,generations=24,models=['base','adapter010'],
        manipulation='Combined representation ablation: remove evidence question, rename answer to text, remove initial Yes./No. only. No new facts or answer targets supplied.',
        limits='Six selected failure scenarios, two correlated variants each. Exposed development diagnostic, not independent acceptance. Cannot isolate which of the three formatting changes caused an effect.',
        decision='Read all outputs. Compare correctness, contradiction, unsupported details and evidence relevance. If failures remain, do not repeat identical fine-tuning. No promotion from this diagnostic alone.',
        training_executed=False,production_approved=False,
        code_sha256=hashlib.sha256(source.encode()).hexdigest())
    out.mkdir()
    for name,data in [('evaluate.py',source),('kernel-metadata.json',json.dumps(meta,indent=2)),('review_protocol.json',json.dumps(protocol,indent=2))]:(out/name).write_text(data,encoding='utf8')
    print(json.dumps(protocol,indent=2))
if __name__=='__main__':main()
