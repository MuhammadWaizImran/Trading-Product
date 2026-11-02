"""Validate private staged examples and write a coverage ledger; no ML imports."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
STAGED=('pdf_training_dp05_expanded.json','pdf_training_dp10_corrected.json',
        'pdf_training_dp17_expanded.json','pdf_training_dp16_foundations.json')


def load(path):return json.loads(path.read_text(encoding='utf8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--completed-batch',default='008',choices=['006','007','008','009'])
    ap.add_argument('--active-batch',default='none',choices=['007','008','009','none'])
    args=ap.parse_args()
    inventory=load(ROOT/'tmp/pdfs/data_pdf_review/inventory.json')
    sources={r['id']:r for r in inventory}
    included_ids=set()
    def records(batch):
        if batch=='none':return []
        path=ROOT/f'data/pdf_sft_batch_{batch}'
        manifest=load(path/'manifest.json')
        for s in ('train','validation','test'):
            assert sha(path/f'{s}.jsonl')==manifest['splits'][s]
            included_ids.update(json.loads(line)['id'] for line in (path/f'{s}.jsonl').read_text(encoding='utf8').splitlines())
        return [json.loads(line) for line in (path/'train.jsonl').read_text(encoding='utf8').splitlines()]
    completed=records(args.completed_batch)
    active=records(args.active_batch)
    old=[]
    for split in ('train','validation','test'):
        old += [json.loads(line) for line in (ROOT/'data/pdf_sft_batch_007'/f'{split}.jsonl').read_text(encoding='utf8').splitlines()]
    ids={r['id'] for r in old}
    questions={r['messages'][-2]['content'].split('\n\nSupplied evidence')[0].strip().casefold() for r in old}
    staged=[]; checked=set(); manifests=[]
    for filename in STAGED:
        path=ROOT/'research'/filename
        rows=load(path)
        counts=Counter(r['split'] for r in rows)
        assert set(counts)=={'train','validation','test'}
        for row in rows:
            assert row['id'] not in ids,'Duplicate ID: '+row['id']
            ids.add(row['id'])
            q=row['question'].strip().casefold()
            assert q not in questions,'Duplicate question: '+row['id']
            questions.add(q)
            assert all(isinstance(row[k],str) and row[k].strip() for k in ('answer','adaptation','question'))
            src=sources[row['source']]
            assert not src['duplicate_of'] and row['source']!='DP20'
            assert row['pages'] and all(type(p) is int and 1<=p<=src['pages'] for p in row['pages'])
            if row['source'] not in checked:
                assert sha(ROOT/'Data PDF'/src['file'])==src['sha256'],'Source PDF changed'
                checked.add(row['source'])
        staged+=rows
        manifests.append({'file':filename,'sha256':sha(path),'counts':dict(counts)})
    finished=Counter(r['provenance']['source_id'] for r in completed)
    pending=Counter(r['provenance']['source_id'] for r in active)
    remaining=[r for r in staged if r['id'] not in included_ids]
    staged_count=Counter(r['source'] for r in remaining if r['split']=='train')
    lines=['# PDF coverage ledger - 23 September 2026','',
        'Counts are selected teaching records, not complete pages learned, full books reviewed or a percentage of expertise. Repeated missing-evidence/source-identity variants do not add new source coverage.', '',
        f'Latest completed fitting dataset: {args.completed_batch}. Active/submitted dataset: {args.active_batch}. Completion here describes execution, not passing the quality gate.', '',
        '| ID | PDF file | Completed dataset records | Active/submitted records | Staged training records | Scope |',
        '| --- | --- | ---: | ---: | ---: | --- |']
    ledger=[]
    for src in inventory:
        sid=src['id']; duplicate=src['duplicate_of'] or ('DP19' if sid=='DP20' else None)
        scope=('Duplicate/near-duplicate of '+duplicate if duplicate else
               'Selected material only; full coverage not certified' if finished[sid] or pending[sid] else
               'Selected module staged; not fitted' if staged_count[sid] else
               'Not in current datasets; further review/preparation required')
        lines.append(f"| {sid} | {src['file']} | {finished[sid]} | {pending[sid]} | {staged_count[sid]} | {scope} |")
        ledger.append(dict(id=sid,file=src['file'],sha256=src['sha256'],pdf_pages=src['pages'],
            duplicate_of=duplicate,completed_records=finished[sid],active_records=pending[sid],
            staged_training_records=staged_count[sid],scope=scope))
    totals={s:sum(r['split']==s for r in remaining) for s in ('train','validation','test')}
    lines+=['',f'Remaining staged totals outside completed/active datasets: {totals}. Reviewed module records already included in those datasets are not counted again. Validation/test records are development checks with concept overlap, not an untouched expertise examination.', '',
        'The library contains 22 files representing 19 distinct works. User-attested private training permission is recorded; publisher licenses are not universally verified. Preserve individual source attributions and restrictions. No redistribution is authorized.', '',
        'This ledger does not certify full-library fitting, visual chart understanding, all-coin market coverage or profitable forecasting.']
    (ROOT/'research/PDF_COVERAGE_LEDGER.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    report={'structural_validation':'PASS','semantic_validation':'Manual review required; this script does not establish truth or complete semantic split isolation.',
            'completed_batch':args.completed_batch,'active_batch':args.active_batch,'staged_counts':totals,'staged_files':manifests,'sources':ledger}
    (ROOT/'research/PDF_COVERAGE_LEDGER.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('sources','staged_files')},indent=2))


if __name__=='__main__':main()
