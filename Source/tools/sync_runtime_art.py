#!/usr/bin/env python3
# 사용: 저장소 루트에서 python Source/tools/sync_runtime_art.py (Pillow, numpy 필요). 외부 접속 없음.
# 후보 폴더의 최신 승인본과 게임용 사본을 맞춘다(바뀐 것만 다시 만든다).
import glob,os,re,json,hashlib
from PIL import Image
import numpy as np
C="CharacterArt/candidates/"
REJECT={"ria_office_pose01_teary","jihyun_office_pose01_teary","seoyun_office_pose01_teary","jihyun_casual_pose01_teary"}
def sha(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
def latest(dirs):
    best={}
    for d in dirs:
        for f in glob.glob(C+d+"/*.png"):
            m=re.match(r"(.+)_v(\d{3})\.png$",os.path.basename(f))
            if m:
                k,v=m.group(1),int(m.group(2))
                if k not in best or v>best[k][0]: best[k]=(v,f)
    return {k:f for k,(v,f) in best.items()}
def resize_premul(im,size):
    a=np.array(im.convert("RGBA")).astype(np.float32)/255
    a[...,:3]*=a[...,3:4]
    r=np.stack([np.array(Image.fromarray((a[...,i]*255).astype(np.uint8)).resize(size,Image.LANCZOS)).astype(np.float32)/255 for i in range(4)],-1)
    al=r[...,3:4]; rgb=np.where(al>1e-4,r[...,:3]/np.maximum(al,1e-4),0)
    return Image.fromarray((np.clip(np.concatenate([rgb,al],-1),0,1)*255).astype(np.uint8))
man=json.load(open("Source/game/images/characters/SPRITES.json")); files=man["files"]; done=[]
for k,f in sorted(latest(["chatgpt-v001","chatgpt-v002"]).items()):
    if k in REJECT or not re.match(r"^(ria|jihyun|yujin|seoyun)_(office|casual|home|winter|special)_pose0\d_[a-z]+$",k): continue
    rel=f"images/characters/{k.split('_')[0]}/{k}.png"; out="Source/game/"+rel; s=sha(f)
    if os.path.exists(out) and files.get(rel,{}).get("source_sha256")==s: continue
    resize_premul(Image.open(f),(676,1014)).save(out,optimize=True)
    files[rel]={"from":os.path.relpath(f,C),"sha256":sha(out),"source_sha256":s}; done.append(k)
man["files"]=dict(sorted(files.items())); json.dump(man,open("Source/game/images/characters/SPRITES.json","w"),ensure_ascii=False,indent=1)
art=json.load(open("Source/game/images/ART_RUNTIME.json"))
for d,outdir in [("bg-chatgpt-v001","bg"),("cg-chatgpt-v001","cg")]:
    for k,f in sorted(latest([d]).items()):
        name=k.replace("_day","") if outdir=="bg" else k.replace("_scene","")
        rel=f"images/{outdir}/{name}.jpg"; s=sha(f)
        if art["files"].get(rel,{}).get("source_sha256")==s: continue
        Image.open(f).convert("RGB").resize((1280,720),Image.LANCZOS).save("Source/game/"+rel,quality=90,optimize=True)
        art["files"][rel]={"from":os.path.relpath(f,C),"source_sha256":s,"sha256":sha("Source/game/"+rel)}; done.append(rel)
json.dump(art,open("Source/game/images/ART_RUNTIME.json","w"),ensure_ascii=False,indent=1)
print(done)
