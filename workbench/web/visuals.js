import {Orb} from '/orb.js';
import {initializeIntro} from '/intro-controller.js';
initializeIntro({Orb,playIntroSound,document,window});
const orb = new Orb(document.querySelector('#orb-particles'));
startNetwork();
addEventListener('pagehide',()=>orb.destroy());
function startNetwork() {
 const canvas=document.querySelector('#network-background'), ctx=canvas.getContext('2d'); if(!ctx)return;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
 const colors=['139,92,246','99,102,241','167,139,250','124,58,237','196,181,253','245,158,11'];
 let w=innerWidth,h=innerHeight,last=0;
 const nodes=Array.from({length:72},()=>({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*.45,vy:(Math.random()-.5)*.45,r:Math.random()*1.8+.8,c:colors[Math.floor(Math.random()*6)],p:Math.random()*6.28}));
 const resize=()=>{const oldW=w,oldH=h;w=innerWidth;h=innerHeight;for(const n of nodes){n.x=n.x/oldW*w;n.y=n.y/oldH*h;}canvas.width=w;canvas.height=h;last=0;}; resize(); addEventListener('resize',resize);
 function draw(t){requestAnimationFrame(draw);if(document.hidden||t-last<32)return;if(reduced&&last)return;last=t;ctx.clearRect(0,0,w,h);
 for(const n of nodes){if(!reduced){n.x+=n.vx;n.y+=n.vy;n.p+=.02;}if(n.x<0||n.x>w)n.vx*=-1;if(n.y<0||n.y>h)n.vy*=-1;n.x=Math.max(0,Math.min(w,n.x));n.y=Math.max(0,Math.min(h,n.y));}
 for(let i=0;i<nodes.length;i++)for(let j=i+1;j<nodes.length;j++){const a=nodes[i],b=nodes[j],d=Math.hypot(a.x-b.x,a.y-b.y);if(d<160){ctx.strokeStyle='rgba(139,92,246,'+((1-d/160)*.23)+')';ctx.lineWidth=.7;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();}}
 for(const n of nodes){const pulse=(Math.sin(n.p)+1)/2,r=n.r+pulse*2;const glow=ctx.createRadialGradient(n.x,n.y,0,n.x,n.y,r*5);glow.addColorStop(0,'rgba('+n.c+','+(.2+pulse*.25)+')');glow.addColorStop(1,'rgba('+n.c+',0)');ctx.fillStyle=glow;ctx.beginPath();ctx.arc(n.x,n.y,r*5,0,Math.PI*2);ctx.fill();ctx.fillStyle='rgba('+n.c+','+(.5+pulse*.5)+')';ctx.beginPath();ctx.arc(n.x,n.y,r,0,Math.PI*2);ctx.fill();}}
 requestAnimationFrame(draw);
}

function playIntroSound() {
  try {
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return;
    const ctx = new AC();
    const now = ctx.currentTime;
    const master = ctx.createGain();
    master.gain.setValueAtTime(0.25, now);
    master.connect(ctx.destination);
    const bass = ctx.createOscillator();
    const bassGain = ctx.createGain();
    bass.type = "sine";
    bass.frequency.setValueAtTime(30, now);
    bass.frequency.exponentialRampToValueAtTime(110, now + 2);
    bassGain.gain.setValueAtTime(0, now);
    bassGain.gain.linearRampToValueAtTime(0.35, now + 0.4);
    bassGain.gain.exponentialRampToValueAtTime(1e-3, now + 2.8);
    bass.connect(bassGain);
    bassGain.connect(master);
    bass.start(now);
    bass.stop(now + 2.9);
    const bufSize = ctx.sampleRate * 1.5;
    const noiseBuffer = ctx.createBuffer(1, bufSize, ctx.sampleRate);
    const noiseData = noiseBuffer.getChannelData(0);
    for (let i = 0; i < bufSize; i++) noiseData[i] = Math.random() * 2 - 1;
    const noise = ctx.createBufferSource();
    noise.buffer = noiseBuffer;
    const noiseFilter = ctx.createBiquadFilter();
    noiseFilter.type = "bandpass";
    noiseFilter.frequency.setValueAtTime(200, now + 0.2);
    noiseFilter.frequency.exponentialRampToValueAtTime(4e3, now + 1.4);
    noiseFilter.Q.setValueAtTime(1.5, now + 0.2);
    const noiseGain = ctx.createGain();
    noiseGain.gain.setValueAtTime(0, now + 0.2);
    noiseGain.gain.linearRampToValueAtTime(0.12, now + 0.35);
    noiseGain.gain.exponentialRampToValueAtTime(1e-3, now + 1.6);
    noise.connect(noiseFilter);
    noiseFilter.connect(noiseGain);
    noiseGain.connect(master);
    noise.start(now + 0.2);
    noise.stop(now + 1.8);
    const ringPings = [
      { t: 0.55, freq: 660, dur: 0.6 },
      { t: 0.95, freq: 880, dur: 0.6 },
      { t: 1.35, freq: 1100, dur: 0.6 }
    ];
    ringPings.forEach(({ t, freq, dur }) => {
      const osc = ctx.createOscillator();
      const g = ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, now + t);
      osc.frequency.exponentialRampToValueAtTime(freq * 0.7, now + t + dur);
      g.gain.setValueAtTime(0, now + t);
      g.gain.linearRampToValueAtTime(0.08, now + t + 0.03);
      g.gain.exponentialRampToValueAtTime(1e-3, now + t + dur);
      osc.connect(g);
      g.connect(master);
      osc.start(now + t);
      osc.stop(now + t + dur + 0.1);
    });
    const chordNotes = [
      { freq: 523.25, gain: 0.15 },
      { freq: 659.25, gain: 0.1 },
      { freq: 783.99, gain: 0.08 }
    ];
    chordNotes.forEach(({ freq, gain }) => {
      const osc = ctx.createOscillator();
      const g = ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, now + 2.5);
      g.gain.setValueAtTime(0, now + 2.5);
      g.gain.linearRampToValueAtTime(gain, now + 2.55);
      g.gain.exponentialRampToValueAtTime(1e-3, now + 4);
      osc.connect(g);
      g.connect(master);
      osc.start(now + 2.5);
      osc.stop(now + 4.1);
    });
    const shimmer = ctx.createOscillator();
    const shimmerGain = ctx.createGain();
    shimmer.type = "sawtooth";
    shimmer.frequency.setValueAtTime(3e3, now + 2.6);
    shimmer.frequency.exponentialRampToValueAtTime(800, now + 3.4);
    shimmerGain.gain.setValueAtTime(0, now + 2.6);
    shimmerGain.gain.linearRampToValueAtTime(0.03, now + 2.7);
    shimmerGain.gain.exponentialRampToValueAtTime(1e-3, now + 3.4);
    shimmer.connect(shimmerGain);
    shimmerGain.connect(master);
    shimmer.start(now + 2.6);
    shimmer.stop(now + 3.5);
    const blipTimes = [3.8, 4.2, 4.6, 5];
    blipTimes.forEach((t) => {
      const osc = ctx.createOscillator();
      const g = ctx.createGain();
      osc.type = "square";
      osc.frequency.setValueAtTime(1200, now + t);
      osc.frequency.exponentialRampToValueAtTime(600, now + t + 0.08);
      g.gain.setValueAtTime(0.04, now + t);
      g.gain.exponentialRampToValueAtTime(1e-3, now + t + 0.12);
      osc.connect(g);
      g.connect(master);
      osc.start(now + t);
      osc.stop(now + t + 0.15);
    });
    const hum = ctx.createOscillator();
    const humGain = ctx.createGain();
    hum.type = "sine";
    hum.frequency.setValueAtTime(55, now);
    humGain.gain.setValueAtTime(0, now);
    humGain.gain.linearRampToValueAtTime(0.06, now + 1.5);
    humGain.gain.setValueAtTime(0.06, now + 5.5);
    humGain.gain.linearRampToValueAtTime(0, now + 7);
    hum.connect(humGain);
    humGain.connect(master);
    hum.start(now);
    hum.stop(now + 7.1);
    const outro = ctx.createOscillator();
    const outroGain = ctx.createGain();
    outro.type = "sine";
    outro.frequency.setValueAtTime(440, now + 6);
    outro.frequency.exponentialRampToValueAtTime(80, now + 7);
    outroGain.gain.setValueAtTime(0, now + 6);
    outroGain.gain.linearRampToValueAtTime(0.12, now + 6.1);
    outroGain.gain.exponentialRampToValueAtTime(1e-3, now + 7);
    outro.connect(outroGain);
    outroGain.connect(master);
    outro.start(now + 6);
    outro.stop(now + 7.1);
    setTimeout(() => ctx.close().catch(() => {}), 7400);
    return ctx;
  } catch (_) {
  }
}



const chatOrb=new Orb(document.querySelector('#chat-orb-canvas'));
let voiceOrb;document.addEventListener('voice-orb-open',event=>{voiceOrb?.destroy();voiceOrb=new Orb(event.detail);});document.querySelector('#details').addEventListener('close',()=>{voiceOrb?.destroy();voiceOrb=null;});addEventListener('pagehide',()=>{chatOrb.destroy();voiceOrb?.destroy();});
