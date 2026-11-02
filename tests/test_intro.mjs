import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const code=readFileSync(new URL('../workbench/web/intro-controller.js',import.meta.url),'utf8');
const {initializeIntro}=await import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'));
function fixture(reduced=false){
 const nodes=new Map(),timers=new Map();let counter=0, sounds=0,destroyed=0;
 const document={activeElement:null,handlers:{},addEventListener(k,f){this.handlers[k]=f;},querySelector(s){
  if(!nodes.has(s))nodes.set(s,{hidden:false,inert:false,attributes:{},handlers:{},classList:{add(){}},
   addEventListener(k,f){this.handlers[k]=f;},setAttribute(k,v){this.attributes[k]=v;},focus(){document.activeElement=this;}});
  return nodes.get(s);
 }};
 const window={localStorage:{getItem(){return null;},setItem(){}},matchMedia(){return {matches:reduced};},
  setTimeout(fn,ms){const id=++counter;timers.set(id,{fn,ms});return id;},clearTimeout(id){timers.delete(id);},addEventListener(){}};
 class Orb{destroy(){destroyed++;}}
 const controller=initializeIntro({Orb,document,window,playIntroSound(){sounds++;return{state:'running',close(){return Promise.resolve();}};}});
 const click=s=>document.querySelector(s).handlers.click();
 return {controller,document,nodes,timers,click,get sounds(){return sounds;},get destroyed(){return destroyed;}};
}
let f=fixture();
assert.equal(f.nodes.get('#app-shell').inert,true);
f.click('#begin-intro');assert.equal(f.sounds,1);assert.equal(f.timers.size,2);
f.click('#skip-intro');assert.equal(f.nodes.get('#startup').hidden,true);assert.equal(f.nodes.get('#app-shell').inert,false);assert.equal(f.timers.size,0);assert.equal(f.destroyed,1);
f.click('#replay-intro');assert.equal(f.nodes.get('#startup').hidden,false);assert.equal(f.nodes.get('#app-shell').inert,true);
f.click('#intro-sound');f.click('#begin-intro');assert.equal(f.sounds,1);
f.document.handlers.keydown({key:'Escape',preventDefault(){}});assert.equal(f.nodes.get('#app-shell').inert,false);
f=fixture(true);f.click('#begin-intro');assert.equal(f.sounds,0);assert.equal(f.timers.size,0);assert.equal(f.nodes.get('#startup').hidden,true);
f=fixture();f.click('#begin-intro');const finish=[...f.timers.values()].find(t=>t.ms===7200).fn;finish();assert.equal(f.nodes.get('#startup').hidden,true);assert.equal(f.timers.size,0);
console.log('PASS intro: tap, timer completion, skip, replay, mute, Escape, reduced motion, cleanup.');
