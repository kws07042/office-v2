'use strict';
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const stage = $('#stage');
const people = {
  ria:{name:'강리아',caption:'비가 그친 뒤에도, 조금 더 함께.'},
  jihyun:{name:'백지현',caption:'작은 취미를 나누는, 느긋한 저녁.'},
  yujin:{name:'차유진',caption:'같은 창가에서 발견한 다른 풍경.'},
  seoyun:{name:'한서윤',caption:'책장을 넘기듯, 천천히 가까워지는 시간.'}
};
let introTimer, introEndTimer, previousFocus, readingTimer;
let settings={speed:100,typing:true,motion:!matchMedia('(prefers-reduced-motion: reduce)').matches};
try { const saved=JSON.parse(localStorage.getItem('afterwork-title-preview-v2')||'null'); if(saved) settings={...settings,...saved}; } catch {}
settings.speed=Math.max(0,Math.min(100,Number(settings.speed)||0));
function persist(){try{localStorage.setItem('afterwork-title-preview-v2',JSON.stringify(settings));}catch{}}
function resize(){const box=$('#viewport').getBoundingClientRect();stage.style.transform=`scale(${box.width/1280})`;}
new ResizeObserver(resize).observe($('#viewport'));resize();
function choosePerson(key){
  if(!people[key]) return;
  stage.dataset.person=key;
  $$('.portrait').forEach(im=>im.classList.toggle('active',im.dataset.person===key));
  $$('.person-tabs button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.person===key)));
  $('#person-name').textContent=people[key].name;
  $('#person-caption').textContent=people[key].caption;
  $('#scene-index').textContent=`0${Object.keys(people).indexOf(key)+1} / 04`;
}
$$('.person-tabs button').forEach(b=>b.addEventListener('click',()=>choosePerson(b.dataset.person)));
function showView(view,focus=true){
  clearInterval(readingTimer);stage.dataset.view=view;
  $('#main-screen').hidden=view!=='main';
  $('#menu-screen').hidden=!['settings','load'].includes(view);
  $('#story-screen').hidden=view!=='story';
  $('#settings-panel').hidden=view!=='settings';$('#load-panel').hidden=view!=='load';
  $$('.side-tab').forEach(b=>b.classList.toggle('active',b.dataset.menu===view));
  if(view==='settings'){$('#menu-title').textContent='설정';$('#menu-subtitle').textContent='나에게 편안한 속도로';}
  if(view==='load'){$('#menu-title').textContent='불러오기';$('#menu-subtitle').textContent='우리의 이야기가 머문 곳';}
  if(focus){const target=view==='main'?'#start':view==='story'?'#story-return':'#back';$(target).focus({preventScroll:true});}
}
$('#settings').onclick=()=>showView('settings');$('#load').onclick=()=>showView('load');$('#back').onclick=()=>showView('main');
$$('.side-tab').forEach(b=>b.onclick=()=>showView(b.dataset.menu));
$('#start').onclick=()=>{choosePerson('ria');showView('story');};
$('#story-return').onclick=()=>showView('main');
function updateSettings(){
  $('#speed').value=settings.speed;
  $('#speed-value').textContent=settings.speed===100?'즉시':`${settings.speed}자 / 초`;
  $('#typing').setAttribute('aria-checked',String(settings.typing));
  $('#motion').setAttribute('aria-checked',String(settings.motion));
  stage.classList.toggle('no-motion',!settings.motion);
}
$('#speed').oninput=e=>{settings.speed=Number(e.target.value);updateSettings();persist();};
$('#speed').onchange=()=>{
  clearInterval(readingTimer);const text='오늘은 조금 더, 같이 있고 싶어서.';let count=0;
  if(settings.speed===100){$('#reading-sample').textContent=text;return;}
  $('#reading-sample').textContent='';
  readingTimer=setInterval(()=>{$('#reading-sample').textContent=text.slice(0,++count);if(count>=text.length)clearInterval(readingTimer);},1000/Math.max(1,settings.speed));
};
$('#typing').onclick=()=>{settings.typing=!settings.typing;updateSettings();persist();};
$('#motion').onclick=()=>{settings.motion=!settings.motion;updateSettings();persist();};
function finishIntro(animate=true){
  clearTimeout(introTimer);clearTimeout(introEndTimer);
  try{sessionStorage.setItem('afterwork-title-intro-v2','seen');}catch{}
  if(animate&&settings.motion){$('#intro').classList.add('ending');introEndTimer=setTimeout(()=>{$('#intro').hidden=true;$('#main-screen').inert=false;$('#start').focus({preventScroll:true});},700);}
  else{$('#intro').hidden=true;$('#main-screen').inert=false;$('#start').focus({preventScroll:true});}
}
function playIntro(){
  clearTimeout(introTimer);clearTimeout(introEndTimer);showView('main',false);$('#closed').hidden=true;
  const intro=$('#intro');intro.hidden=true;intro.classList.remove('ending');void intro.offsetWidth;intro.hidden=false;
  $('#main-screen').inert=true;$('#skip').focus({preventScroll:true});
  introTimer=setTimeout(()=>finishIntro(),settings.motion?4300:1200);
}
$('#skip').onclick=e=>{e.stopPropagation();finishIntro(false);};$('#intro').onclick=()=>finishIntro(false);$('#replay').onclick=playIntro;
function modal(open){
  $('#modal-cover').hidden=!open;
  for(const id of ['main-screen','menu-screen','story-screen']) $('#'+id).inert=open;
  if(open){previousFocus=document.activeElement;$('#dialog-cancel').focus();}else previousFocus?.focus();
}
$('#quit').onclick=()=>modal(true);$('#dialog-cancel').onclick=()=>modal(false);
$('#dialog-ok').onclick=()=>{modal(false);$('#closed').hidden=false;$('#main-screen').inert=true;$('#reopen').focus();};
$('#reopen').onclick=()=>{$('#closed').hidden=true;$('#main-screen').inert=false;showView('main');};
document.addEventListener('keydown',e=>{
  if(!$('#intro').hidden&&['Enter','Escape',' '].includes(e.key)){e.preventDefault();finishIntro(false);return;}
  if(!$('#modal-cover').hidden){
    if(e.key==='Escape')modal(false);
    if(e.key==='Tab'){e.preventDefault();(document.activeElement===$('#dialog-cancel')?$('#dialog-ok'):$('#dialog-cancel')).focus();}
    return;
  }
  if(e.key==='Escape'&&stage.dataset.view!=='main')showView('main');
});
$('#expand').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await $('#viewport').requestFullscreen();}catch{$('#expand').textContent='브라우저에서 전체 화면을 지원하지 않습니다';}};
for(let i=0;i<9;i++){const dot=document.createElement('i');dot.className='mote';dot.style.left=`${510+(i*83)%730}px`;dot.style.top=`${85+(i*109)%540}px`;dot.style.animationDelay=`-${i*1.7}s`;$('#motes').append(dot);}
updateSettings();
let seen=false;try{seen=!!sessionStorage.getItem('afterwork-title-intro-v2');}catch{}
if(!seen)playIntro();
document.addEventListener('visibilitychange',()=>{for(const a of stage.getAnimations({subtree:true})){if(document.hidden)a.pause();else a.play();}});
