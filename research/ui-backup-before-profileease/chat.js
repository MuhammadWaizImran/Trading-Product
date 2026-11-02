'use strict';
const $ = s => document.querySelector(s);
const make = (tag, text, cls) => { const e = document.createElement(tag); if(text !== undefined)e.textContent=text; if(cls)e.className=cls; return e; };
const STORAGE='crypto-research-chats-v1';
let history=[], active=null, busy=false, expanded=false;
try { const saved=JSON.parse(localStorage.getItem(STORAGE)||'[]'); if(Array.isArray(saved))history=saved.filter(x=>typeof x.question==='string' && x.result && Array.isArray(x.result.evidence)).slice(0,30); } catch (_) {}
function toast(text){$('#toast').textContent=text;$('#toast').hidden=false;clearTimeout(toast.timer);toast.timer=setTimeout(()=>$('#toast').hidden=true,4500);}
function dialog(title,text){$('#dialog-title').textContent=title;$('#dialog-body').replaceChildren(make('p',text));$('#details').showModal();}
function store(){try{localStorage.setItem(STORAGE,JSON.stringify(history.slice(0,30)));}catch(_){toast('Browser storage unavailable. This conversation will not be saved.');}}
function renderHistory(){
 const query=$('#history-search').value.toLowerCase(); const filtered=history.filter(x=>x.question.toLowerCase().includes(query)); const box=$('#history-list');box.replaceChildren();
 if(!filtered.length)box.append(make('p',query?'No matching conversations.':'Your next idea starts here. Ask a question to begin.','empty-history'));
 for(const row of filtered.slice(0,expanded?30:3)) {const b=make('button',undefined,'history-row');b.append(make('span',row.question),make('time',new Date(row.time).toLocaleDateString(undefined,{month:'short',day:'numeric'})));b.addEventListener('click',()=>show(row));box.append(b);}
 $('#see-more').hidden=filtered.length<=3; $('#see-more').textContent=expanded?'See Less ↑':'See More ↓';
}
function show(row){
 active=row; $('#welcome').hidden=true;$('#suggestions').hidden=true;$('#conversation').hidden=false;
 const box=$('#conversation');box.replaceChildren(make('div',row.question,'message user'));
 const answer=make('div',row.result.answer,'message assistant');answer.append(make('small',row.result.method));
 for(const e of row.result.evidence.slice(0,4)) {const block=make('div',undefined,'evidence');block.append(make('strong',e.question),make('p',e.answer));const link=make('a',`${e.source} · Pages ${(e.pages||[]).join(', ')}`);link.href='/source/'+encodeURIComponent(e.source)+'#page='+(e.pages||[1])[0];link.target='_blank';link.rel='noopener';block.append(link);answer.append(block);}
 box.append(answer);box.scrollTop=0;
}
function reset(){if(busy)return;active=null;$('#conversation').hidden=true;$('#welcome').hidden=false;$('#suggestions').hidden=false;$('#message').value='';$('#message').focus();}
$('#chat-form').addEventListener('submit',async event=>{
 event.preventDefault(); if(busy)return;const question=$('#message').value.trim();if(!question)return;
 const params=new URLSearchParams({kind:'evidence',question,scope:$('#scope').value});if($('#scope').value==='source_specific')params.set('source_id',$('#source').value);
 busy=true;$('#send').disabled=true;$('#send').textContent='…';
 try{const response=await fetch('/api/answer?'+params);const result=await response.json();if(!response.ok)throw new Error(result.error||'Research request failed');const row={question,result,time:new Date().toISOString()};history.unshift(row);history=history.slice(0,30);store();renderHistory();show(row);$('#message').value='';}
 catch(e){toast(e.message||'Unable to connect to the local research service.');}
 finally{busy=false;$('#send').disabled=false;$('#send').textContent='➤';}
});
$('#message').addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing){e.preventDefault();$('#chat-form').requestSubmit();}});
document.querySelectorAll('[data-prompt]').forEach(b=>b.addEventListener('click',()=>{$('#message').value=b.dataset.prompt;$('#message').focus();}));
$('#scope').addEventListener('change',()=>{$('#source-picker').hidden=$('#scope').value!=='source_specific';});
$('#source-button').addEventListener('click',()=>{$('#scope').value='source_specific';$('#source-picker').hidden=false;$('#source').focus();});
$('#new-chat').addEventListener('click',reset);$('#back-button').addEventListener('click',reset);$('#chat-tab').addEventListener('click',reset);
$('#history-button').addEventListener('click',()=>{$('#recent').scrollIntoView({block:'center'});$('#history-search').focus();});
$('#history-search').addEventListener('input',renderHistory);$('#see-more').addEventListener('click',()=>{expanded=!expanded;renderHistory();});
$('#close-dialog').addEventListener('click',()=>$('#details').close());
function status(){dialog('Your research workspace','The assistant currently searches reviewed PDF passages. Qwen3-8B is under evaluation; generated model answers and live trading agents are not enabled. No trades are placed.');const a=make('a','Open the research workbench →');a.href='/workbench';$('#dialog-body').append(a);}
['#overview-tab','#status-button','#agent-status'].forEach(s=>$(s).addEventListener('click',status));
$('#mode-info').addEventListener('click',()=>dialog('Evidence Search','Search checked educational passages, with links to their PDF pages. Select Source to search a particular document. Search matches are supporting material to review, not a generated analysis or a live trade signal.'));
$('#notification-button').addEventListener('click',()=>dialog('Notifications','No market alerts are active. Continuous monitoring and phone/email notifications have not been connected.'));
function profile(){dialog('Private workspace','Welcome, Waiz. Your conversations stay in this browser on this device. The research library is served from your local project.');}
$('#profile-button').addEventListener('click',profile);$('#avatar-button').addEventListener('click',profile);
$('#settings-button').addEventListener('click',()=>{dialog('Conversation settings','Up to 30 conversations are stored in this browser. Clear them below; source PDFs and evaluation results are not affected.');const b=make('button','Clear conversation history');b.addEventListener('click',()=>{history=[];store();renderHistory();reset();$('#details').close();toast('Conversation history cleared.');});$('#dialog-body').append(b);});
const hour=new Date().getHours();$('.greeting').textContent=`Good ${hour<12?'morning':hour<18?'afternoon':'evening'}, Waiz`;
renderHistory();
(async()=>{try{const response=await fetch('/api/status');if(!response.ok)throw new Error();const data=await response.json();for(const source of data.sources){const option=make('option',`${source.id} · ${source.file}`);option.value=source.id;$('#source').append(option);}}catch(_){toast('Local research service unavailable. Start the workbench server.');}})();
