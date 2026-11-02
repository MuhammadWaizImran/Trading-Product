"""Verify downloaded cloud artifacts without loading or fitting any model."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_text(encoding='utf8'))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch',required=True)
    parser.add_argument('--results',type=Path,required=True)
    args=parser.parse_args()
    assert re.fullmatch(r'\d{3}',args.batch)
    data=ROOT/f'data/pdf_sft_batch_{args.batch}'
    folder=args.results.resolve()
    assert ROOT in folder.parents, 'Keep audit output in project workspace'
    status=read(folder/'status.json')
    assert status['stage']=='completed_training_human_evaluation_pending',status
    manifest=read(data/'manifest.json')
    assert read(folder/'dataset_manifest.json')==manifest,'Cloud/local manifest mismatch'
    runtime=read(folder/'runtime.json')
    assert runtime['model']==manifest['model'] and runtime['revision']==manifest['revision']
    for split,expected in manifest['splits'].items():
        assert hashlib.sha256((data/f'{split}.jsonl').read_bytes()).hexdigest()==expected
    tests=[json.loads(line) for line in (data/'test.jsonl').read_text(encoding='utf8').splitlines()]
    expected_ids={r['id'] for r in tests}
    outputs={name:read(folder/(name+'_answers.json')) for name in ('baseline','adapted','reloaded')}
    for name,rows in outputs.items():
        assert len(rows)==len(expected_ids) and {r['id'] for r in rows}==expected_ids,name
    base={r['id']:r for r in outputs['baseline']}
    adapted={r['id']:r for r in outputs['adapted']}
    reloaded={r['id']:r for r in outputs['reloaded']}
    cases=[]
    for row in tests:
        rid=row['id']; allowed=set(row.get('evidence_ids',[]))
        assert adapted[rid]['response']==reloaded[rid]['response'], 'Reload response mismatch: '+rid
        item={'id':rid,'question':row['messages'][-2]['content'].split('\n\nSupplied evidence')[0],
              'evidence_ids':sorted(allowed)}
        for name,answer in [('baseline',base[rid]),('adapted',adapted[rid])]:
            cites=re.findall(r'\[([^\[\]\n]+)\]',answer['response'])
            item[name]={'response':answer['response'],'citation_ids':cites,
                        'unrecognized_citations':[c for c in cites if c not in allowed],
                        'hit_token_limit':answer.get('hit_token_limit')}
        cases.append(item)
    result=read(folder/'result.json')
    assert math.isfinite(result['train_metrics']['train_loss'])
    adapter=folder/'adapter/adapter_model.safetensors'
    audit={'artifact_checks':'PASS','semantic_review':'pending; citation existence is not support',
           'production_approved':False,'batch':args.batch,'gpu':runtime.get('gpu'),
           'counts':manifest['counts'],'adapter_sha256':hashlib.sha256(adapter.read_bytes()).hexdigest(),
           'adapter_bytes':adapter.stat().st_size,'adapted_reload_equal':True,'cases':cases}
    (folder/'local_artifact_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in audit.items() if k!='cases'},indent=2))
    for item in cases:
        print('\nCASE',item['id'],item['question'])
        for name in ('baseline','adapted'):
            value=item[name]
            print(name,'unrecognized_citations=',value['unrecognized_citations'],'limit=',value['hit_token_limit'])
            print(value['response'])


if __name__=='__main__':main()
