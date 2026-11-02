"""Offline structural review of cloud outputs; semantic approval is always manual."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from workbench.response_review import review_response


def review(records, cases):
    expected = {r['id']: r for r in cases}
    seen = set()
    reviewed = []
    for record in records:
        identifier = record['id']
        if identifier not in expected or identifier in seen:
            raise ValueError('Unknown or duplicate result ID')
        seen.add(identifier)
        case = expected[identifier]
        gate = review_response(record.get('final_response', ''), case['evidence'],
                               truncated=record.get('hit_token_limit', True))
        matched = False
        if not gate['errors']:
            answer = json.loads(record['final_response'])
            matched = (answer['status'] == case['expected_status'] and
                       answer['evidence_id'] == case['expected_evidence_id'])
        reviewed.append(dict(id=identifier, structural_review=gate,
                             expected_status_and_citation_match=matched,
                             semantic_review='pending', reference=case['messages'][-1]['content'],
                             response=record.get('final_response', '')))
    missing = sorted(set(expected)-seen)
    return dict(expected_cases=len(cases), received_cases=len(records), missing_ids=missing,
                structurally_valid=sum(not r['structural_review']['errors'] for r in reviewed),
                status_and_citation_matches=sum(r['expected_status_and_citation_match'] for r in reviewed),
                semantic_accuracy=None, promotion_allowed=False, cases=reviewed)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--results', type=Path, required=True)
    args = p.parse_args()
    cases = json.loads((ROOT/'notebooks/pdf_transfer_eval_021/cases.json').read_text())
    reports = {}
    for name in ['baseline_thinking', 'adapted_thinking']:
        reports[name] = review(json.loads((args.results/(name+'.json')).read_text()), cases)
    target = args.results/'structural_review.json'
    target.write_text(json.dumps(reports, indent=2), encoding='utf-8')
    print(target)


if __name__ == '__main__':
    main()
