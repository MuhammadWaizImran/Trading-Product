"""Offline rejection gate for generated answers; no model calls or approval.

Passing structural checks never proves that a citation entails a claim.
Keep generated text quarantined until an independent semantic review exists.
"""
import json


def review_response(text, evidence, *, source_id=None, truncated=False):
    errors=[]
    if truncated:
        errors.append('truncated')
    def unique_object(pairs):
        obj={}
        for key,value in pairs:
            if key in obj:
                raise ValueError('duplicate JSON key')
            obj[key]=value
        return obj
    try:
        obj=json.loads(text,object_pairs_hook=unique_object)
    except (ValueError,TypeError):
        return dict(status='rejected',errors=errors+['invalid_json'],publishable=False)
    if not isinstance(obj,dict) or set(obj)!={'status','answer','evidence_id'}:
        return dict(status='rejected',errors=errors+['invalid_schema'],publishable=False)
    if obj['status'] not in ('supported','insufficient'):
        errors.append('invalid_status')
    if not isinstance(obj['answer'],str) or not obj['answer'].strip():
        errors.append('empty_answer')
    citation=obj['evidence_id']
    if obj['status']=='insufficient':
        if citation is not None:
            errors.append('insufficient_with_citation')
    elif obj['status']=='supported':
        matches=[e for e in evidence if e.get('id')==citation] if isinstance(citation,str) else []
        if len(matches)!=1:
            errors.append('citation_not_one_unique_passage')
        elif source_id is not None and matches[0].get('source')!=source_id:
            errors.append('wrong_document')
    return dict(status='rejected' if errors else 'needs_semantic_review',
                errors=errors,publishable=False)
