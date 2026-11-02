"""Validate frozen payload against files without executing the trainer or importing ML."""
import argparse
import ast
import base64
import gzip
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch',required=True)
    args=parser.parse_args()
    assert re.fullmatch(r'\d{3}',args.batch)
    data=ROOT/f'data/pdf_sft_batch_{args.batch}'
    notebook=ROOT/f'notebooks/pdf_sft_{args.batch}'
    source=(notebook/'train.py').read_text(encoding='utf8')
    tree=ast.parse(source)
    assignment=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAYLOAD' for t in n.targets))
    assert isinstance(assignment.value,ast.Call)
    arg=assignment.value.args[0]
    if isinstance(arg,ast.Constant):
        payload=json.loads(ast.literal_eval(arg))
    else:
        # Decode only the explicitly recognized literal compression envelope;
        # never evaluate or execute uploaded model code during local checks.
        assert isinstance(arg,ast.Call) and isinstance(arg.func,ast.Attribute)
        assert isinstance(arg.func.value,ast.Name) and arg.func.value.id=='gzip' and arg.func.attr=='decompress'
        inner=arg.args[0]
        assert isinstance(inner,ast.Call) and isinstance(inner.func,ast.Attribute)
        assert isinstance(inner.func.value,ast.Name) and inner.func.value.id=='base64' and inner.func.attr=='b64decode'
        payload=json.loads(gzip.decompress(base64.b64decode(ast.literal_eval(inner.args[0]),validate=True)))
    manifest=json.loads((data/'manifest.json').read_text())
    assert payload['manifest']==manifest
    ids=set(); questions=set(); verified={}; max_chars=0
    for split in ['train','validation','test']:
        p=data/f'{split}.jsonl'
        assert hashlib.sha256(p.read_bytes()).hexdigest()==manifest['splits'][split]
        rows=[json.loads(s) for s in p.read_text(encoding='utf8').splitlines()]
        assert payload[split]==rows and len(rows)==manifest['counts'][split]
        for r in rows:
            assert r['id'] not in ids; ids.add(r['id'])
            assert [m['role'] for m in r['messages']]==['system','user','assistant']
            q=r['messages'][1]['content']; assert q not in questions; questions.add(q)
            max_chars=max(max_chars,sum(len(m['content']) for m in r['messages']))
            prov=r['provenance']; pdf=(ROOT/'Data PDF'/prov['file']).resolve()
            assert pdf.parent==(ROOT/'Data PDF').resolve()
            if pdf not in verified: verified[pdf]=hashlib.sha256(pdf.read_bytes()).hexdigest()
            assert verified[pdf]==prov['sha256']
            assert prov['permission'] and prov['pdf_pages']
            cites=re.findall(r'\[([^\[\]\n]+)\]',r['messages'][2]['content'])
            assert all(c in r['evidence_ids'] for c in cites),r['id']
    metadata=json.loads((notebook/'kernel-metadata.json').read_text())
    assert metadata['is_private'] and metadata['enable_gpu'] and metadata['enable_internet']
    assert manifest['parent_adapter'] is None and not manifest['local_training_executed']
    assert 'Refuse silent truncation' in source and 'if not torch.cuda.is_available():' in source
    assert 'No working CUDA GPU. CPU training is disabled' in source
    report=dict(structural_checks='PASS',batch=args.batch,counts=manifest['counts'],
                source_files=len(verified),max_message_characters=max_chars,
                token_check='Cloud tokenizer must enforce 2048 tokens; character count is not token validation.',
                code_sha256=hashlib.sha256(source.encode()).hexdigest(),local_model_execution=False,
                limitation='No semantic correctness or independent evaluation guarantee.')
    (notebook/'preflight.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
