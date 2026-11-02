import json
import unittest
from workbench.response_review import review_response


class ResponseReviewTests(unittest.TestCase):
    evidence=[{'id':'cold','source':'DP01','text':'Cold storage reduces online exposure.'}]

    def test_existing_but_unrelated_citation_never_approved(self):
        text=json.dumps(dict(status='supported',answer='The transfer proves ownership.',evidence_id='cold'))
        result=review_response(text,self.evidence)
        self.assertEqual(result['status'],'needs_semantic_review')
        self.assertFalse(result['publishable'])

    def test_wrong_source_and_truncation(self):
        text=json.dumps(dict(status='supported',answer='Claim',evidence_id='cold'))
        r=review_response(text,self.evidence,source_id='DP07',truncated=True)
        self.assertEqual(set(r['errors']),{'wrong_document','truncated'})

    def test_invalid_citations(self):
        for citation in ['missing',['cold'],'cold,other',None]:
            text=json.dumps(dict(status='supported',answer='Claim',evidence_id=citation))
            self.assertEqual(review_response(text,self.evidence)['status'],'rejected')

    def test_duplicate_keys_and_ambiguous_passages(self):
        self.assertEqual(review_response('{"status":"supported","status":"insufficient"}',[])['status'],'rejected')
        text=json.dumps(dict(status='supported',answer='Claim',evidence_id='cold'))
        self.assertEqual(review_response(text,self.evidence*2)['status'],'rejected')

    def test_abstention_is_not_automatic_semantic_approval(self):
        for citation in [None,'cold']:
            r=review_response(json.dumps(dict(status='insufficient',answer='Missing evidence',evidence_id=citation)),self.evidence)
            self.assertFalse(r['publishable'])
            self.assertEqual(r['status'],'needs_semantic_review' if citation is None else 'rejected')
