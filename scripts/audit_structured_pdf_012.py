"""Artifact-only JSON contract checks; never claims semantic correctness."""
import argparse
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--results',type=Path,required=True)
    parser.add_argument('--batch',default='012');args=parser.parse_args()
    assert re.fullmatch(r'\d{3}',args.batch)
    folder=args.results.resolve();assert ROOT in folder.parents
    expected={json.loads(s)['id'] for s in (ROOT/f'data/pdf_sft_batch_{args.batch}/test.jsonl').read_text(encoding='utf8').splitlines()}
    report={}
    for name in ['baseline','adapted','reloaded']:
        rows=json.loads((folder/(name+'_answers.json')).read_text(encoding='utf8'))
        assert len(rows)==len(expected) and {r['id'] for r in rows}==expected
        errors=[]
        for r in rows:
            try:
                obj=json.loads(r['response'])
                assert isinstance(obj,dict) and set(obj)=={'status','answer','evidence_id'},'wrong keys'
                assert obj['status'] in ['supported','insufficient'],'invalid status'
                assert isinstance(obj['answer'],str) and obj['answer'].strip(),'empty answer'
                if obj['status']=='insufficient':assert obj['evidence_id'] is None,'insufficient with citation'
                else:assert isinstance(obj['evidence_id'],str) and obj['evidence_id'] in r['evidence_ids'],'unknown evidence ID'
                assert not r['hit_token_limit'],'truncated'
            except (ValueError,AssertionError,TypeError) as exc:errors.append(dict(id=r['id'],error=str(exc)))
        report[name]=dict(records=len(rows),contract_passes=len(rows)-len(errors),errors=errors)
    report['semantic_review']='Still required: valid JSON and existing IDs do not prove support, correct status or correct calculations.'
    (folder/'structured_contract_audit.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
