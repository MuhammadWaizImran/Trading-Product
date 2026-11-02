import unittest
from workbench.source_scope import route_evidence


class SourceScopeTests(unittest.TestCase):
    def setUp(self):
        self.evidence = [{'id':'a','source':'DP01','answer':'one'}, {'id':'b','source':'DP19','answer':'two'}]

    def test_missing_identity_never_inferred_from_single_hit(self):
        result=route_evidence(self.evidence[:1])
        self.assertFalse(result['model_allowed'])
        self.assertEqual(result['evidence'],[])
        self.assertEqual(result['status'],'needs_source')

    def test_explicit_source_filters_cross_document_distractor(self):
        result=route_evidence(self.evidence,source_id='DP19')
        self.assertTrue(result['model_allowed'])
        self.assertEqual([e['id'] for e in result['evidence']],['b'])
        result['evidence'][0]['answer']='changed'
        self.assertEqual(self.evidence[1]['answer'],'two')

    def test_unknown_selection_does_not_fallback(self):
        self.assertEqual(route_evidence(self.evidence,source_id='DP99')['status'],'needs_evidence')

    def test_general_scope_requires_explicit_choice(self):
        self.assertFalse(route_evidence(self.evidence)['model_allowed'])
        self.assertEqual(route_evidence(self.evidence,scope='general')['evidence'],self.evidence)

    def test_empty_general_context_is_not_model_knowledge_fallback(self):
        self.assertFalse(route_evidence([],scope='general')['model_allowed'])

    def test_ambiguous_or_invalid_metadata_rejected(self):
        for kwargs in ({'scope':'automatic'},{'scope':'general','source_id':'DP01'},{'source_id':''}):
            with self.assertRaises(ValueError): route_evidence(self.evidence,**kwargs)


if __name__=='__main__': unittest.main()
