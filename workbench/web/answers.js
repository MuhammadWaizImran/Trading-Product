'use strict';
function showCheckedAnswer(target, result) {
  target.replaceChildren(el('p',result.answer),el('small',result.method));
  for (const r of result.evidence) {
    const card=el('article',undefined,'card');
    card.append(el('h3',r.question),el('p',r.answer));
    const link=el('a',`${r.source} | PDF pages ${r.pages.join(', ')} | ${r.id}`);
    link.href='/source/'+encodeURIComponent(r.source)+'#page='+r.pages[0];
    link.target='_blank'; link.rel='noopener';
    card.append(link); target.append(card);
  }
}
$('#answer-scope').addEventListener('change',()=>{
  const general=$('#answer-scope').value==='general';
  $('#answer-source-label').hidden=general;
  $('#answer-source').disabled=general;
  $('#evidence-answer-result').replaceChildren();
});
$('#evidence-answer-form').addEventListener('submit',async event=>{
  event.preventDefault(); clearError();
  const box=$('#evidence-answer-result'); box.replaceChildren();
  const params={kind:'evidence',question:$('#answer-question').value,scope:$('#answer-scope').value};
  if(params.scope==='source_specific')params.source_id=$('#answer-source').value;
  try { showCheckedAnswer(box,await api('/api/answer',params)); }
  catch(e) { error(e); }
});
$('#limit-answer-form').addEventListener('submit',async event=>{
  event.preventDefault(); clearError();
  const box=$('#limit-answer-result'); box.replaceChildren();
  try { showCheckedAnswer(box,await api('/api/answer',{kind:'limit',...Object.fromEntries(new FormData(event.target))})); }
  catch(e) { error(e); }
});
(async()=>{
  try {
    const status=await api('/api/status');
    for(const source of status.sources){
      const option=el('option',`${source.id} - ${source.file}`);
      option.value=source.id; $('#answer-source').append(option);
    }
  } catch(e) { error(e); }
})();
