(()=>{"use strict";
const $=id=>document.getElementById(id);
const people=[["ria","강리아","R"],["jihyun","백지현","J"],["yujin","차유진","Y"],["seoyun","한서윤","S"]];
const choices=["조용한 카페에서 조금 더 이야기하자.","천천히 걷자. 목적지는 걸으면서 고르고.","오늘은 내가 고른 곳도 하나 보여 주고 싶어."];
const answers=["좋아. 오늘은 내가 고른 자리도 네가 한번 봐 줘~","좋아! 대신 너무 빨리 걷기 없기. 나 지금 같이 있는 게 좋거든.","...그 말은 좀 기대되는데? 오늘은 내가 따라가 볼게~"];
const replies=[["miss","보고 싶다고 짧게 답한다."],["evening","오늘 할 일을 나누고 저녁 연락을 제안한다."],["small_memory","어제 좋았던 작은 순간을 하나 골라 보낸다."]];
const initial=[{sender:"ria",body:"일어났어? 나는 빵 먹는 중~ 오늘 추천 코스는 식탁!"},{sender:"dohyun",body:"나도 이제 아침 먹으려고. 어제 차 잘 마셨어."},{sender:"ria",body:"오늘의 추천 코스 인증~ 빵은 내가 골랐어!",media:true},{sender:"ria",body:"오늘 뭐 해? 나는 빨래 돌리고 나면 특별한 일 없어."}];
const state={view:"dialogue",selected:"ria",archive:false,waiting:false,replied:false,rows:initial.map(r=>({...r})),dialogue:0};
function el(tag,cls,text){const x=document.createElement(tag);if(cls)x.className=cls;if(text!==undefined)x.textContent=text;return x}
function fit(){const width=$("stage-wrap").clientWidth;const scale=width/1280;$("stage").style.transform="scale("+scale+")";$("stage-wrap").style.height=(720*scale)+"px"}
new ResizeObserver(fit).observe($("stage-wrap"));fit();
function currentName(){return people.find(p=>p[0]===state.selected)[1]}
function showView(view){state.view=view;$("phone").hidden=view!=="phone";$("scene").hidden=view==="phone";$("choices").hidden=view!=="choices";$("advance").hidden=view==="choices";document.querySelectorAll("[data-view]").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.view===view)));$("preview-status").textContent={dialogue:"대화 화면",choices:"중앙 선택지",phone:"메신저"}[view];if(view==="phone")renderPhone();else renderScene()}
function renderScene(){const night=$("night-toggle").checked;$("scene").classList.toggle("night",night);$("scene-time").textContent=night?"초여름 저녁 · 퇴근 후":"초여름 오후 · 온빛브랜딩";
 const sample=state.dialogue===0?(night?"오늘은 코스 안 정해도 괜찮지? 그냥 조금 더 같이 있고 싶어서.":"오늘 퇴근하고 시간 있어? 가 보고 싶은 곳이 하나 생겼어~"):state.dialogue===1?"있어. 이번에는 나도 같이 고르고 싶어.":state.dialogue;
 $("speaker").textContent=state.dialogue===1?"도현":"강리아";$("speaker").style.color=state.dialogue===1?"#fffdf8":"#ffe0a3";
 $("dialogue-line").textContent=$("long-toggle").checked?"오늘 퇴근하고 시간 있어? 가 보고 싶은 곳이 하나 생겼어~\n오늘은 코스 안 정해도 괜찮지? 그냥 조금 더 같이 있고 싶어서.\n좋아! 대신 너무 빨리 걷기 없기. 나 지금 같이 있는 게 좋거든.":sample;
 $("choices").replaceChildren();choices.forEach((c,i)=>{const b=el("button","",c+($("long-toggle").checked?" "+c+" "+c:""));b.type="button";b.dataset.choice=String(i);b.addEventListener("click",()=>{state.dialogue=answers[i];showView("dialogue")});$("choices").append(b)})}
function renderContacts(){$("contacts").replaceChildren();people.forEach(([id,name,letter])=>{const b=el("button",id===state.selected?"active":"");b.type="button";b.setAttribute("aria-pressed",String(id===state.selected));b.dataset.contact=id;b.append(el("span","initial",letter));const copy=el("span","contact-copy");copy.append(el("strong","",name),el("small","",id==="ria"?"메시지 "+state.rows.length+"개":"아직 대화가 없어요"));b.append(copy);b.addEventListener("click",()=>{state.selected=id;renderPhone()});$("contacts").append(b)})}
function openPhoto(){$("photo-overlay").hidden=false;$("photo-close").focus()}
function closePhoto(){$("photo-overlay").hidden=true;const p=document.querySelector(".photo-preview");if(p)p.focus()}
function renderPhone(){renderContacts();$("contact-name").textContent=currentName();$("contact-status").textContent=state.selected==="ria"?"교제 중 · 개인 대화":"개인 대화";$("phone-mode").textContent=state.archive?"개인 메시지 · 대화 기록":"개인 메시지 · 일요일 아침";$("archive-toggle").textContent=state.archive?"진행 중인 대화":"대화 기록";
 const choosing=state.selected==="ria"&&!state.archive&&!state.replied&&!state.waiting;
 $("messages").className="messages"+(state.archive?" archive":choosing?" replying":"");$("messages").replaceChildren();
 if(state.selected!=="ria")$("messages").append(el("p","empty-messages","아직 주고받은 메시지가 없어요."));
 else{$("messages").append(el("div","date-pill","일요일 아침"));state.rows.forEach(row=>{const bubble=el("article","bubble"+(row.sender==="dohyun"?" mine":""));bubble.append(el("small","",row.sender==="dohyun"?"나":"강리아"),el("p","",row.body));if(row.media){const p=el("button","photo-preview");p.type="button";p.append(el("span","","사진 준비 중"),el("small","","아침 식탁 · 눌러서 확대"));p.addEventListener("click",openPhoto);bubble.append(p)}$("messages").append(bubble)})}
 const compose=$("phone-compose");compose.className="phone-compose";compose.replaceChildren();$("phone-foot").hidden=choosing||state.archive;
 function btn(text,action){const b=el("button","",text);b.type="button";b.addEventListener("click",action);return b}
 if(state.archive){compose.classList.add("archiving");compose.append(el("p","","이 회차에서 받은 메시지만 표시합니다."));if(state.selected==="ria")compose.append(btn("최근 사진 다시 보기",openPhoto))}
 else if(state.selected!=="ria"){compose.append(el("p","","강리아 대화가 기다리고 있어요."),btn("진행 중인 대화로 돌아가기",()=>{state.selected="ria";renderPhone()}))}
 else if(state.waiting){compose.append(el("p","","강리아 님이 입력 중…"),btn("바로 보기",finishReply))}
 else if(choosing){compose.classList.add("replying");compose.append(el("p","reply-heading","어떤 마음을 전할까요?"));const list=el("div","reply-options");list.setAttribute("aria-label","답장 선택");replies.forEach(([id,caption])=>{const b=btn(caption+($("long-toggle").checked?" "+caption+" "+caption:""),()=>sendReply(id));b.dataset.reply=id;list.append(b)});compose.append(list)}
 else compose.append(el("p","","대화를 읽고 편할 때 이어가세요."),btn("다음 메시지",()=>showView("dialogue")));
 requestAnimationFrame(()=>{$("messages").scrollTop=$("messages").scrollHeight})}
function sendReply(id){const texts={miss:"기록 정리 중인데, 벌써 보고 싶네.",evening:"기록 좀 정리하려고. 저녁에 끝나면 얘기할래?",small_memory:"어제 나란히 앉아 있던 거 생각났어. 별말 안 해도 좋더라."};state.rows.push({sender:"dohyun",body:texts[id]});state.replied=true;state.waiting=true;state.lastReply=id;renderPhone()}
function finishReply(){const a={miss:"방금 세 번 읽었어. 네가 보낸 거 한 줄 맞지? 휴대폰 탓인가~",evening:"좋아. 나는 빨래 산부터 넘을게. 이쪽도 꽤 큰 작업이야~",small_memory:"나도! 사실 조용해질 때 무슨 얘기할지 찾고 있었는데~"};state.rows.push({sender:"ria",body:a[state.lastReply||"miss"]});state.waiting=false;renderPhone()}
function openSheet(title){$("sheet-title").textContent=title;$("sheet-body").replaceChildren();if(title==="대화 기록")$("sheet-body").append(el("p","","강리아"),el("p","",$("dialogue-line").textContent));else $("sheet-body").append(el("p","","미리보기에서는 화면 구성을 확인합니다. 실제 "+title+" 기능은 Ren’Py에서 연결됩니다."));$("sheet-overlay").hidden=false;$("sheet-close").focus()}
document.querySelectorAll("[data-view]").forEach(b=>b.addEventListener("click",()=>showView(b.dataset.view)));
$("night-toggle").addEventListener("change",renderScene);$("long-toggle").addEventListener("change",()=>{renderScene();if(state.view==="phone")renderPhone()});
$("archive-toggle").addEventListener("click",()=>{state.archive=!state.archive;renderPhone()});$("phone-close").addEventListener("click",()=>showView("dialogue"));$("phone-back").addEventListener("click",()=>{state.rows=initial.map(r=>({...r}));state.replied=false;state.waiting=false;state.archive=false;state.selected="ria";renderPhone()});
$("photo-close").addEventListener("click",closePhoto);$("sheet-close").addEventListener("click",()=>{$("sheet-overlay").hidden=true});
document.querySelectorAll("[data-sheet]").forEach(b=>b.addEventListener("click",()=>openSheet(b.dataset.sheet)));
document.querySelectorAll("[data-action]").forEach(b=>b.addEventListener("click",()=>{const a=b.dataset.action;if(a==="phone")showView("phone");else if(a==="history")openSheet("대화 기록");else if(a==="back"){state.dialogue=0;showView("dialogue")}else if(a==="auto"||a==="skip")b.setAttribute("aria-pressed",String(b.getAttribute("aria-pressed")!=="true"));else openSheet({save:"저장",load:"불러오기",settings:"설정",menu:"메뉴"}[a])}));
document.addEventListener("keydown",e=>{if(e.key==="Escape"){if(!$("photo-overlay").hidden)closePhoto();else if(!$("sheet-overlay").hidden)$("sheet-overlay").hidden=true;else if(state.view==="phone")showView("dialogue")}if(e.key==="Enter"&&e.target===document.body&&state.view==="dialogue"){state.dialogue=state.dialogue===0?1:0;renderScene()}});
showView("dialogue");
})();
