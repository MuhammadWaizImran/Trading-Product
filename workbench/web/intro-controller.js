// Presentation only. The loading sequence is not a model/service readiness check.
export function initializeIntro({Orb, playIntroSound, document, window}) {
  const startup=document.querySelector('#startup');
  const shell=document.querySelector('#app-shell');
  const begin=document.querySelector('#begin-intro');
  const soundButton=document.querySelector('#intro-sound');
  const replay=document.querySelector('#replay-intro');
  let introOrb, timer, fadeTimer, audio, playing=false, muted=false;
  try {muted=window.localStorage.getItem('crypto-intro-muted')==='true';}catch(_){}
  function paintSound(){soundButton.textContent=muted?'Sound off':'Sound on';soundButton.setAttribute('aria-pressed',String(muted));}
  function stopSound(){if(audio && audio.state!=='closed')audio.close().catch(()=>{});audio=null;}
  function cancelTimers(){window.clearTimeout(timer);window.clearTimeout(fadeTimer);}
  function finish(){
    cancelTimers();stopSound();introOrb?.destroy();introOrb=null;playing=false;
    startup.hidden=true;shell.inert=false;
    document.querySelector('#orb-button').focus({preventScroll:true});
  }
  function open(){
    cancelTimers();stopSound();introOrb?.destroy();playing=false;
    startup.className='';startup.hidden=false;shell.inert=true;
    introOrb=new Orb(document.querySelector('#intro-orb'));
    paintSound();begin.focus({preventScroll:true});
  }
  function start(){
    if(playing){finish();return;}
    playing=true;startup.classList.add('playing');
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){finish();return;}
    if(!muted)audio=playIntroSound();
    fadeTimer=window.setTimeout(()=>startup.classList.add('leaving'),6400);
    timer=window.setTimeout(finish,7200);
  }
  begin.addEventListener('click',start);
  document.querySelector('#skip-intro').addEventListener('click',finish);
  replay.addEventListener('click',()=>{
    document.querySelector('#sidebar').hidden=true;
    const backdrop=document.querySelector('#sidebar-backdrop');if(backdrop)backdrop.hidden=true;
    document.querySelector('#sidebar-toggle').setAttribute('aria-expanded','false');
    open();
  });
  soundButton.addEventListener('click',()=>{
    muted=!muted;paintSound();if(muted)stopSound();
    try {window.localStorage.setItem('crypto-intro-muted',String(muted));}catch(_){}
  });
  document.addEventListener('keydown',event=>{
    if(startup.hidden)return;
    if(event.key==='Escape'){event.preventDefault();finish();return;}
    if(event.key==='Tab'){
      const controls=[begin,soundButton,document.querySelector('#skip-intro')];
      const index=controls.indexOf(document.activeElement);
      const next=event.shiftKey?(index<=0?controls.length-1:index-1):(index+1)%controls.length;
      event.preventDefault();controls[next].focus();
    }
  });
  window.addEventListener('pagehide',()=>{cancelTimers();stopSound();introOrb?.destroy();});
  open();
  return {finish,open};
}
