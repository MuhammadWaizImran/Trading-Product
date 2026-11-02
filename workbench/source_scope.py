"""Explicit source scope for experimental answering; no inference or fitting.

The caller must obtain scope/source_id from the user's selection, never from a
retrieval result or model guess. This does not detect intent in arbitrary prose
and does not establish that a passage supports an answer.
"""
from copy import deepcopy
import re


def has_unidentified_source(question):
    """Conservative English cue guard, not general intent or entailment detection.

    Explicit uncertainty takes priority over a possibly stale source dropdown.
    Quoted/negated cues may request clarification too; never silently guess.
    """
    patterns = (
        r'\b(?:unnamed|unidentified|unspecified|unknown)\s+(?:report|paper|article|survey|study|document)\b',
        r'\b(?:report|paper|article|survey|study|document)\b.{0,60}\bwithout\s+(?:its\s+|a\s+|the\s+)?(?:title|name|identifier)\b',
        r"\b(?:have\s+not|haven't|haven’t)\s+identified\b.{0,40}\b(?:report|paper|article|survey|study|document)\b",
    )
    return any(re.search(p, question, re.IGNORECASE) for p in patterns)


def route_evidence(evidence, *, scope='source_specific', source_id=None):
    if scope not in ('source_specific', 'general'):
        raise ValueError('Choose source_specific or general scope explicitly')
    if scope == 'general' and source_id is not None:
        raise ValueError('A selected source requires source_specific scope')
    if source_id is not None and (not isinstance(source_id, str) or not source_id.strip()):
        raise ValueError('source_id must be a nonempty document identifier')
    if scope == 'source_specific' and source_id is None:
        return dict(status='needs_source', evidence=[], model_allowed=False,
                    response='Please identify or select the document you mean. Retrieved passages alone do not establish the identity of an unnamed source.')
    selected = [deepcopy(e) for e in evidence if scope == 'general' or e.get('source') == source_id]
    if not selected:
        return dict(status='needs_evidence', evidence=[], model_allowed=False,
                    response='No reviewed evidence is available for this request and source selection. Please provide the relevant passage.')
    return dict(status='ready', evidence=selected, model_allowed=True, response=None)
