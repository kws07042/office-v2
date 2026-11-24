import re,json,os,sys
import pathlib
G=str(pathlib.Path(__file__).resolve().parents[1]/"game")+"/"
OUT=sys.argv[1]
NAME={"d":"도현","r":"리아","j":"지현","y":"유진","s":"서윤","dn":"도현(속마음)","jn":"지현(속마음)","yn":"유진(속마음)","rn":"리아(속마음)","sn":"서윤(속마음)","msgd":"도현(메시지)","msgr":"리아(메시지)"}
PN={"dohyun":"도현","ria":"리아","jihyun":"지현","yujin":"유진","seoyun":"서윤","ria_shared":"리아"}
st=json.load(open(G+"event_story.json",encoding="utf-8"))
mt={s["id"]:s for s in json.load(open(G+"event_main_text.json",encoding="utf-8"))}
RI=re.compile(r"""\[?ri\(\s*(['"])((?:(?!\1)[^\\]|\\.)*)\1\s*,\s*(['"])((?:(?!\3)[^\\]|\\.)*)\3\s*\)\]?""")
def clean(t):
    t=RI.sub(lambda m:m.group(2),t)
    t=re.sub(r"\[memory\.get\('(\w+)',\s*'([^']*)'\)\]",lambda m:"("+m.group(2)+")",t)
    t=re.sub(r"\[(\w+)\]",r"(\1)",t)
    return t.replace('\\"','"').replace("\\n"," / ")
COS={"bunny":"바니걸","nurse":"간호사","cheer":"치어리더","qipao":"차이나드레스","maid":"메이드","police":"여경찰"}
def event_block(eid,var,ind):
    who=eid.split("_")[0]; hn=PN[who]; out=[]
    def line(k,v):
        v=v[0] if isinstance(v,list) else v
        return {"narration":"  *"+v+"*","heroine":"**"+hn+"**: "+v,"dohyun":"**도현**: "+v}[k]
    beats=st.get(eid,{}).get(var,[])
    out.append(ind+"> ━━ 성인 이벤트 `%s` (%s) ━━"%(eid,var))
    for i,b in enumerate(beats[:3]):
        h=b.get("heroine") or b.get("ria",[""])[0]
        out+= [ind+"> [도입 %d] *%s*"%(i+1,b["narration"]), ind+"> **%s**: %s"%(hn,h), ind+"> **도현**: %s"%b["dohyun"][0]]
    keys=["%s:%s"%(eid,var)] if var!="cosplay" else ["%s:cosplay:%s"%(eid,c) for c in ("bunny","nurse","cheer","qipao","maid","police") if "%s:cosplay:%s"%(eid,c) in mt]
    for k in keys:
        s=mt.get(k)
        if not s: continue
        if var=="cosplay": out.append(ind+"> ── 코스프레: %s ──"%COS[k.split(":")[-1]])
        for c,cg in enumerate(s["main"],1):
            out.append(ind+"> [본장면 CG%d]"%c)
            for kk,v in cg["lines"]: out.append(ind+"> "+line(kk,v))
    if len(beats)>3:
        b=beats[3]; h=b.get("heroine") or b.get("ria",[""])[0]
        out+= [ind+"> [이후] *%s*"%b["narration"], ind+"> **%s**: %s"%(hn,h), ind+"> **도현**: %s"%b["dohyun"][0]]
    out.append(ind+"> ━━ 이벤트 끝 ━━")
    return out
def convert(fname):
    L=open(G+fname,encoding="utf-8").read().split("\n"); out=[]; src=[]
    def emit(x): out.append(x); src.append((fname,li))
    def emitn(xs):
        for x in xs: emit(x)
    for li,l in enumerate(L,1):
        s=l.strip(); ind_n=(len(l)-len(l.lstrip()))//4; ind="  "*max(0,ind_n-1)
        if not s or s.startswith("#"): continue
        m=re.match(r"label (\w+)",s)
        if m: emitn(["","## "+m.group(1),""]); continue
        m=re.match(r'\$ chapter = "(.*)"',s)
        if m: emitn(["### "+clean(m.group(1)),""]); continue
        m=re.match(r'\$ location = (.*)',s)
        if m:
            v=m.group(1); v=v.strip('"') if v.startswith('"') else "(상황에 따라 바뀜)"
            emit(ind+"📍 *"+clean(v)+"*"); continue
        m=re.match(r'^"((?:[^"\\]|\\.)*)"\s*:$',s)
        if m: emit(ind+"▶ **선택지:** "+clean(m.group(1))); continue
        if s=="menu:": emit(ind+"— 선택 —"); continue
        m=re.match(r'^(\w+)\s+"((?:[^"\\]|\\.)*)"$',s)
        if m and m.group(1) in NAME:
            emit(ind+"**%s**: %s"%(NAME[m.group(1)],clean(m.group(2)))); continue
        m=re.match(r'^"((?:[^"\\]|\\.)*)"$',s)
        if m: emit(ind+"*"+clean(m.group(1))+"*"); continue
        m=re.match(r'call phone_deliver\("[^"]+",\s*"(\w+)",\s*(.+?)(?:,\s*(?:contact|important|media)=.*)?\)\s*$',s)
        if m:
            body=m.group(2); mm=RI.search(body)
            txt=mm.group(2) if mm else re.sub(r'^"|"$','',body.strip())
            emit(ind+"📱 **%s**: %s"%(PN.get(m.group(1),m.group(1)),clean(txt))); continue
        m=re.match(r'call pc_chat\("(\w+)",\s*\[(.*)\]\)',s)
        if m:
            for who,txt in re.findall(r'\("(\w+)",\s*"((?:[^"\\]|\\.)*)"\)',m.group(2)):
                emit(ind+"💻 **%s**: %s"%(PN.get(who,who),clean(txt)))
            continue
        m2=re.match(r'call event_sequence\("(\w+)_" \+ slot,\s*outfit\)',s)
        if m2:
            who=m2.group(1)
            emit(ind+"*(이 장면은 R07·R12·R15에서 같은 자리로 불린다. 아래에 셋 다 적는다.)*")
            for eid,vars_ in ((who+"_r07",["casual"]),(who+"_r12",["special"]),(who+"_r15",["home","cosplay"])):
                for var in vars_: emitn(event_block(eid,var,ind))
            continue
        m=re.match(r'call event_sequence\("(\w+)",\s*(.+)\)',s)
        if m:
            eid=m.group(1); v=m.group(2).strip()
            vars_=[v.strip('"')] if v.startswith('"') else (["home","cosplay"] if "r15" in eid else list(st.get(eid,{}).keys()))
            for var in vars_: emitn(event_block(eid,var,ind))
            continue
        m=re.search(r'event_play_text_scene\("([^"]+)"',s)
        if m:
            sc=mt[m.group(1)]; emit(ind+"> ━━ 성인 장면 `%s` ━━"%m.group(1))
            for c,cg in enumerate(sc["main"],1):
                emit(ind+"> [CG%d]"%c)
                for k,v in cg["lines"]:
                    v=v[0] if isinstance(v,list) else v
                    emit(ind+"> "+{"narration":"*"+v+"*","heroine":"**리아**: "+v,"dohyun":"**도현**: "+v}[k])
            emit(ind+"> ━━ 끝 ━━"); continue
    return out,src
GROUPS=[("00_공통",["prologue.rpy","common.rpy","schedule_pick.rpy"]),
("01_강리아",["ria_r01.rpy","ria_r02_r04.rpy","ria_r05_r08.rpy","ria_o04.rpy","ria_r09_r12.rpy","ria_r13_e01.rpy"]),
("02_백지현",["jihyun_r01_r04.rpy","jihyun_r05_r12.rpy","jihyun_optional.rpy","jihyun_r13_e01.rpy"]),
("03_차유진",["yujin_r01_r04.rpy","yujin_r05_r08.rpy","yujin_optional.rpy","yujin_r09_r12.rpy","yujin_r13_e01.rpy"]),
("04_한서윤",["seoyun_r01_r04.rpy","seoyun_r05_r12.rpy","seoyun_optional.rpy","seoyun_r13_e01.rpy"]),
("05_특별·크리스마스·봄·이별",["special_scenes.rpy","xmas_scenes.rpy","xmas_after.rpy","spring_story.rpy","bond_breakup.rpy"])]
os.makedirs(OUT,exist_ok=True); tot=0; MAP={}
for name,files in GROUPS:
    lines=["# 〈퇴근 후, 우리〉 대사 정리 · "+name.split("_",1)[1],"",
           "기준: 0.42.0-test9 · 표기: **이름**: 대사 / *지문* / ▶ 선택지(들여쓰기는 그 선택지를 골랐을 때) / 📱 문자 / 💻 GY톡 / 📍 장소 / > 성인 이벤트 · '도현'은 플레이어가 정한 이름으로 바뀐다. 리아와는 반말로 고정.",""]
    lmap=[None]*len(lines)
    for f in files:
        o,sr=convert(f)
        lines+=["","---","","# 파일: "+f]; lmap+=[None]*4
        lines+=o; lmap+=sr
    open(os.path.join(OUT,name+".md"),"w",encoding="utf-8").write("\n".join(lines)+"\n"); tot+=len(lines)
    MAP[name+".md"]=lmap
print("lines",tot)
json.dump(MAP,open(os.path.join(OUT,"_map.json"),"w",encoding="utf-8"),ensure_ascii=False)
