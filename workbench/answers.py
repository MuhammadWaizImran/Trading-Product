"""Tool-backed answers and source-scoped evidence; no model execution or orders."""
from scripts.research_math import limit_price_rule
from workbench.source_scope import route_evidence, has_unidentified_source


def answer_request(library, request):
    kind=request.get('kind','evidence')
    if kind=='limit':
        result=limit_price_rule(request['side'],request['limit'],request['fill'])
        direction='at or below' if result['side']=='buy' else 'at or above'
        verdict='satisfies' if result['price_constraint_satisfied'] else 'does not satisfy'
        return dict(status='calculated',method='Exact decimal rule; no language model',model_invoked=False,
                    answer=f"A {result['side']} limit requires a gross fill price {direction} {result['limit_price']}. "
                           f"The hypothetical price {result['hypothetical_fill_price']} {verdict} this constraint. "
                           'Meeting the price constraint does not guarantee execution.',
                    calculation=result,evidence=[{k:v for k,v in r.items() if k!='_tokens'} for r in library.rows if r['id']=='limit-order'])
    if kind!='evidence':
        raise ValueError('Unsupported answer type')
    question=request.get('question','').strip()
    if not question or len(question)>500:
        raise ValueError('Enter a question of 1 to 500 characters')
    scope=request.get('scope','source_specific')
    selected=request.get('source_id') or None
    if has_unidentified_source(question):
        route=route_evidence([],scope='source_specific',source_id=None)
    elif scope=='source_specific' and selected is None:
        route=route_evidence([],scope=scope,source_id=selected)
    else:
        if selected is not None and selected not in library.sources:
            raise ValueError('Source is not in the verified local library')
        matches=library.search(question,source_id=selected)
        route=route_evidence(matches,scope=scope,source_id=selected)
    return dict(status=route['status'],answer=route['response'] or
                'These reviewed passages are candidates for your question. Inspect their context and pages; a search match does not establish support.',
                evidence=route['evidence'],model_invoked=False,
                method='Source-scoped evidence search; no generated interpretation')
