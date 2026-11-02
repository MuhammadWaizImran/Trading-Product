'use strict';
const $ = s => document.querySelector(s);
const make = (tag, text, cls) => { const e = document.createElement(tag); if(text !== undefined)e.textContent=text; if(cls)e.className=cls; return e; };
const STORAGE='crypto-research-chats-v1';
let history=[], active=null, busy=false, expanded=false;
try { const saved=JSON.parse(localStorage.getItem(STORAGE)||'[]'); if(Array.isArray(saved))history=saved.filter(x=>typeof x.question==='string' && x.result && Array.isArray(x.result.evidence)).slice(0,30); } catch (_) {}
function toast(text){$('#toast').textContent=text;$('#toast').hidden=false;clearTimeout(toast.timer);toast.timer=setTimeout(()=>$('#toast').hidden=true,4500);}
function dialog(title,text){stopMedia();$('#dialog-title').textContent=title;$('#dialog-body').replaceChildren(make('p',text));$('#details').showModal();}
function store(){try{localStorage.setItem(STORAGE,JSON.stringify(history.slice(0,30)));}catch(_){toast('Browser storage unavailable. This conversation will not be saved.');}}
function renderHistory(){
 const query=$('#history-search').value.toLowerCase(); const filtered=history.filter(x=>x.question.toLowerCase().includes(query)); const box=$('#history-list');box.replaceChildren();
 if(!filtered.length)box.append(make('p',query?'No matching conversations.':'Your next idea starts here. Ask a question to begin.','empty-history'));
 for(const row of filtered.slice(0,expanded?30:3)) {const b=make('button',undefined,'history-row');b.append(make('span',row.question),make('time',new Date(row.time).toLocaleDateString(undefined,{month:'short',day:'numeric'})));b.addEventListener('click',()=>show(row));box.append(b);}
 $('#see-more').hidden=filtered.length<=3; $('#see-more').textContent=expanded?'See Less ↑':'See More ↓';
}
function show(row){
 active=row;$('#back-button').hidden=false;$('#chat-tab').hidden=false;$('#welcome').hidden=true;$('#suggestions').hidden=true;$('#conversation').hidden=false;$('#chat-orb').hidden=false;
 const box=$('#conversation');box.replaceChildren();
 for(const turn of (row.turns||[{question:row.question,result:row.result}])){
  const user=make('div',turn.question,'message user');const edit=make('button','Edit message','copy-answer');edit.type='button';edit.onclick=()=>{$('#message').value=turn.question;$('#message').focus();};user.append(edit);box.append(user);
  const answer=make('div',turn.result.answer,'message assistant');answer.append(make('small',turn.result.method));
  for(const e of turn.result.evidence.slice(0,4)){const block=make('div',undefined,'evidence');block.append(make('strong',e.question),make('p',e.answer));const link=make('a',`${e.source} | Pages ${(e.pages||[]).join(', ')}`);link.href='/source/'+encodeURIComponent(e.source)+'#page='+(e.pages||[1])[0];link.target='_blank';link.rel='noopener';block.append(link);answer.append(block);}
  const copy=make('button','Copy answer','copy-answer');copy.type='button';copy.onclick=async()=>{try{await navigator.clipboard.writeText([turn.result.answer,...turn.result.evidence.map(e=>e.answer)].join('\n\n'));toast('Answer copied.');}catch(_){toast('Clipboard unavailable. Select the answer to copy it.');}};answer.append(copy);box.append(answer);
 }
 box.scrollTop=box.scrollHeight;
}

function reset(){if(busy)return;active=null;$('#back-button').hidden=true;$('#chat-tab').hidden=true;$('#conversation').hidden=true;$('#chat-orb').hidden=true;$('#welcome').hidden=false;$('#suggestions').hidden=false;$('#message').value='';$('#message').focus();}
$('#chat-form').addEventListener('submit',async event=>{
 event.preventDefault(); if(busy)return;const question=$('#message').value.trim();if(!question)return;
 if(question.startsWith('/image')){dialog('Image generation','The reference image-generation service is not connected here. No prompt or image has been sent to it.');return;}
 const params=new URLSearchParams({kind:'evidence',question,scope:$('#scope').value});if($('#scope').value==='source_specific')params.set('source_id',$('#source').value);
 busy=true;$('#send').disabled=true;$('#send').textContent='…';$('#send').classList.add('busy');
 $('#conversation').hidden=false;$('#chat-orb').hidden=false;$('#welcome').hidden=true;$('#suggestions').hidden=true;
 $('#conversation').replaceChildren(make('div',question,'message user'),make('div','Searching reviewed sources','message pending'));
 try{const response=await fetch('/api/answer?'+params);const result=await response.json();if(!response.ok)throw new Error(result.error||'Research request failed');const row=active||{question,result,time:new Date().toISOString(),turns:[]};if(!row.turns)row.turns=[{question:row.question,result:row.result}];row.turns.push({question,result});row.turns=row.turns.slice(-50);row.result=result;row.time=new Date().toISOString();history=history.filter(item=>item!==row);history.unshift(row);history=history.slice(0,30);store();renderHistory();show(row);$('#message').value='';}
 catch(e){const message=e.message||'Unable to connect to the local research service.';toast(message);$('#conversation').replaceChildren(make('div',question,'message user'),make('div',message+' Your question is still in the composer; try again.','message assistant'));$('#back-button').hidden=false;}
 finally{busy=false;$('#send').disabled=false;$('#send').textContent='\u2191';$('#send').classList.remove('busy');}
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

renderHistory();
(async()=>{try{const response=await fetch('/api/status');if(!response.ok)throw new Error();const data=await response.json();for(const source of data.sources){const option=make('option',`${source.id} · ${source.file}`);option.value=source.id;$('#source').append(option);}}catch(_){toast('Local research service unavailable. Start the workbench server.');}})();

function closeSidebar(){$('#sidebar-backdrop').hidden=true;$('#sidebar').hidden=true;$('#sidebar-toggle').setAttribute('aria-expanded','false');}
$('#sidebar-toggle').addEventListener('click',()=>{$('#sidebar').hidden=!$('#sidebar').hidden;$('#sidebar-backdrop').hidden=$('#sidebar').hidden;$('#sidebar-toggle').setAttribute('aria-expanded',String(!$('#sidebar').hidden));});
$('#sidebar-close').addEventListener('click',closeSidebar);
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeSidebar();});
$('#orb-button').addEventListener('click',()=>openVoice(true));
$('#more-button').addEventListener('click',status);
$('#voice-button').addEventListener('click',()=>openVoice(false));
$('#footer-settings').addEventListener('click',()=>$('#settings-button').click());
$('#message').addEventListener('input',e=>{e.target.style.height='auto';e.target.style.height=Math.min(e.target.scrollHeight,140)+'px';});

let recognition=null, cameraStream=null, previewURL=null;
function stopMedia(){try{recognition?.abort();}catch(_){} recognition=null;cameraStream?.getTracks().forEach(t=>t.stop());cameraStream=null;if(previewURL){URL.revokeObjectURL(previewURL);previewURL=null;}window.speechSynthesis?.cancel();}
$('#details').addEventListener('close',stopMedia);
window.addEventListener('pagehide',stopMedia);
$('#sidebar-backdrop').addEventListener('click',closeSidebar);
$('#voice-mode-button').addEventListener('click',()=>openVoice(true));
$('#theme-button').addEventListener('click',()=>{
 dialog('Appearance','Choose the appearance for this browser.');const grid=make('div',undefined,'theme-grid');
 for(const theme of ['quantum','cyber','matrix','sunset','premium']){const button=make('button',theme[0].toUpperCase()+theme.slice(1));button.onclick=()=>{document.body.dataset.theme=theme;try{localStorage.setItem('crypto-chat-theme',theme);}catch(_){}};grid.append(button);}$('#dialog-body').append(grid);
});
try{const theme=localStorage.getItem('crypto-chat-theme');if(['quantum','cyber','matrix','sunset','premium'].includes(theme))document.body.dataset.theme=theme;}catch(_){}
function openVoice(full){
 dialog(full?'Voice assistant':'Speak to type','Press Start to enable your microphone. Browser speech recognition may process audio through your browser provider. Recognized words go into the composer for your review; nothing is sent automatically.');
 const canvas=make('canvas',undefined,'voice-orb');$('#dialog-body').prepend(canvas);document.dispatchEvent(new CustomEvent('voice-orb-open',{detail:canvas}));
 const controls=make('div',undefined,'voice-controls');const start=make('button','Start microphone');const stop=make('button','Stop');const read=make('button','Read latest answer');const label=make('p','Ready when you are.');const language=make('select');language.setAttribute('aria-label','Speech language');for(const [id,name] of [['en-US','English'],['ur-PK','Urdu']]){const o=make('option',name);o.value=id;language.append(o);}
 start.onclick=()=>{const Recognition=window.SpeechRecognition||window.webkitSpeechRecognition;if(!Recognition){label.textContent='Speech recognition is unavailable in this browser. You can still type in the chat.';return;}stopMedia();recognition=new Recognition();recognition.lang=language.value;recognition.interimResults=true;recognition.onresult=e=>{let transcript='';for(let i=0;i<e.results.length;i++)transcript+=e.results[i][0].transcript+' ';$('#message').value=transcript.trim().slice(0,500);label.textContent=transcript;};recognition.onerror=e=>{label.textContent='Microphone stopped: '+e.error;start.disabled=false;};recognition.onend=()=>{start.disabled=false;};try{recognition.start();start.disabled=true;label.textContent='Listening...';}catch(_){label.textContent='Could not start speech recognition.';start.disabled=false;}};
 stop.onclick=()=>{stopMedia();start.disabled=false;label.textContent='Stopped. Review your words in the composer.';};
 read.onclick=()=>{if(!active){label.textContent='Ask a question first.';return;}if(!window.speechSynthesis){label.textContent='Speech playback is unavailable.';return;}window.speechSynthesis.cancel();window.speechSynthesis.speak(new SpeechSynthesisUtterance(active.result.answer));};
 controls.append(start,stop,read);$('#dialog-body').append(language,label,controls);
}
$('#lens-button').addEventListener('click',()=>{
 dialog('QuantuMania Lens','Preview an image from your device or camera. Images stay in this browser. AI image analysis, OCR and translation are not connected in this workspace.');
 const preview=make('img');preview.alt='Selected image preview';preview.className='lens-preview';preview.hidden=true;
 const video=make('video');video.className='lens-preview';video.autoplay=true;video.muted=true;video.playsInline=true;video.hidden=true;
 const upload=make('input');upload.type='file';upload.accept='image/png,image/jpeg,image/webp';upload.setAttribute('aria-label','Choose an image');
 upload.onchange=()=>{const file=upload.files[0];if(!file)return;if(!['image/png','image/jpeg','image/webp'].includes(file.type)||file.size>10*1024*1024){toast('Choose a PNG, JPEG or WebP image under 10 MB.');return;}stopMedia();video.hidden=true;previewURL=URL.createObjectURL(file);preview.src=previewURL;preview.hidden=false;};
 const camera=make('button','Open camera');camera.onclick=async()=>{stopMedia();try{const stream=await navigator.mediaDevices.getUserMedia({video:true,audio:false});if(!$('#details').open){stream.getTracks().forEach(t=>t.stop());return;}cameraStream=stream;video.srcObject=stream;video.hidden=false;preview.hidden=true;}catch(_){toast('Camera unavailable or permission denied. You can upload an image instead.');}};
 const capture=make('button','Capture frame');capture.onclick=()=>{if(!cameraStream||!video.videoWidth){toast('Open the camera first.');return;}const c=document.createElement('canvas');c.width=video.videoWidth;c.height=video.videoHeight;c.getContext('2d').drawImage(video,0,0);preview.src=c.toDataURL('image/png');preview.hidden=false;video.hidden=true;stopMedia();};$('#dialog-body').append(preview,video,upload,camera,capture);
});
