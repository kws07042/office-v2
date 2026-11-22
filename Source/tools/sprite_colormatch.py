# 사용법(로컬, 읽기 전용 입력): 기준 입상과 같은 인물의 새 입상 색을 영역별로 맞춘다. 원본은 덮어쓰지 않는다.
"""Match skin / hair / iris colours of a sprite to a reference sprite (same heroine).
Parameters are fitted on one image (the pose's neutral) and applied identically to every
expression of that pose, so shared body pixels stay identical."""
import numpy as np
from PIL import Image, ImageFilter

def load(p): return np.asarray(Image.open(p).convert("RGBA")).astype(np.float32)

def hsv(rgb):
    mx=rgb.max(-1); mn=rgb.min(-1); s=(mx-mn)/np.maximum(mx,1); return mx, s

def masks(a, hair_rule):
    rgb=a[...,:3]; al=a[...,3]; r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]
    v,s=hsv(rgb); fig=al>128
    skin=fig&(r>170)&(r-g>28)&(g>=b-6)&(r-b>32)&(r-b<110)&(s>0.12)&(s<0.45)
    hair=fig&hair_rule(r,g,b,v,s)&~skin
    ys,xs=np.where(fig); top=ys.min()
    # face band: first skin rows under the top
    band=np.zeros_like(fig); band[top+110:top+210]=True
    iris=band&fig&~skin&~hair&(v>60)&(v<235)&(s>0.08)
    # keep iris near face centre columns
    sk=np.where(skin[top+60:top+260])
    if len(sk[1]):
        cx0,cx1=np.percentile(sk[1],5),np.percentile(sk[1],95); cols=np.zeros_like(fig); cols[:,int(cx0):int(cx1)]=True; iris&=cols
    return skin, hair, iris

def fit(src, ref, hair_rule):
    out={}
    ms=masks(src,hair_rule); mr=masks(ref,hair_rule)
    for name,m1,m2 in zip(("skin","hair","iris"),ms,mr):
        if m1.sum()<50 or m2.sum()<50: continue
        a=src[...,:3][m1]; b=ref[...,:3][m2]
        out[name]=(a.mean(0),a.std(0)+1e-3,b.mean(0),b.std(0)+1e-3)
    return out

def apply(img, params, hair_rule, strength={"skin":0.85,"hair":0.9,"iris":0.9}):
    rgb=img[...,:3].copy(); ms=dict(zip(("skin","hair","iris"),masks(img,hair_rule)))
    for name,(smu,ssd,rmu,rsd) in params.items():
        m=Image.fromarray((ms[name]*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
        w=np.asarray(m).astype(np.float32)[...,None]/255.0*strength[name]
        t=(img[...,:3]-smu)/ssd*np.minimum(rsd/ssd,1.6)*ssd/ssd*ssd/ssd if False else (img[...,:3]-smu)/ssd*rsd+rmu
        rgb=rgb*(1-w)+np.clip(t,0,255)*w
    o=np.concatenate([rgb,img[...,3:4]],-1)
    return Image.fromarray(np.clip(o,0,255).astype(np.uint8),"RGBA")

HAIR={
 "seoyun": lambda r,g,b,v,s: (v<200)&(b>g+3)&(r>g+3)&(s>0.14)&~((r>200)&(r-b>25)),           # dark plum hair
 "ria":    lambda r,g,b,v,s: (r>150)&(r-b>40)&(v>150)&(s>0.25)&(s<0.7),
 "jihyun": lambda r,g,b,v,s: (r>90)&(r>g*1.6)&(r>b*1.4),
 "yujin":  lambda r,g,b,v,s: (s<0.12)&(v>150),
}

# ---- histogram (CDF) matching per region: captures shading/highlights, not only the mean ----
def fit_hist(src, ref, hair_rule):
    out={}
    for name,m1,m2 in zip(("skin","hair","iris"),masks(src,hair_rule),masks(ref,hair_rule)):
        if m1.sum()<50 or m2.sum()<50: continue
        luts=[]
        for c in range(3):
            a=src[...,c][m1].astype(int); b=ref[...,c][m2].astype(int)
            ha=np.bincount(a,minlength=256).cumsum()/len(a); hb=np.bincount(b,minlength=256).cumsum()/len(b)
            luts.append(np.interp(ha,hb,np.arange(256)))
        out[name]=luts
    return out

def apply_hist(img, luts, hair_rule, strength={"skin":0.8,"hair":0.85,"iris":0.9}):
    rgb=img[...,:3].copy(); ms=dict(zip(("skin","hair","iris"),masks(img,hair_rule)))
    for name,lut in luts.items():
        m=Image.fromarray((ms[name]*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
        w=np.asarray(m).astype(np.float32)[...,None]/255.0*strength[name]
        t=np.stack([lut[c][img[...,c].astype(int)] for c in range(3)],-1)
        rgb=rgb*(1-w)+t*w
    o=np.concatenate([rgb,img[...,3:4]],-1)
    return Image.fromarray(np.clip(o,0,255).astype(np.uint8),"RGBA")

# ---- iris recolour: find eyes from the white sclera, then move iris hue/sat to the reference ----
def eye_boxes(a):
    rgb=a[...,:3]; al=a[...,3]; v=rgb.max(-1); s=(v-rgb.min(-1))/np.maximum(v,1)
    ys,xs=np.where(al>128); top=ys.min()
    scl=(al>200)&(v>225)&(s<0.10); scl[:top+115]=False; scl[top+205:]=False
    from scipy import ndimage
    lab,n=ndimage.label(scl); boxes=[]
    for sl in ndimage.find_objects(lab):
        h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start
        if 3<=h<=40 and 4<=w<=70: boxes.append((sl[0].start-8,sl[0].stop+8,sl[1].start-10,sl[1].stop+10))
    return boxes

def iris_mask(a):
    rgb=a[...,:3]; v=rgb.max(-1); s=(v-rgb.min(-1))/np.maximum(v,1); r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]
    m=np.zeros(v.shape,bool)
    for y0,y1,x0,x1 in eye_boxes(a):
        box=np.zeros_like(m); box[max(y0,0):y1,max(x0,0):x1]=True
        m|=box&(v>70)&(v<225)&(b>=r-6)&(b>=g)&(a[...,3]>200)&~((v<150)&(r>g+3)&(s>0.14))
    return m

def iris_stats(a):
    m=iris_mask(a); hsv=np.asarray(Image.fromarray(a[...,:3].astype(np.uint8)).convert("HSV")).astype(np.float32)
    m2=m&(hsv[...,1]>70)
    if m2.sum()>40: m=m2
    return np.median(hsv[...,0][m]), hsv[...,1][m].mean(), m.sum()

def recolor_iris(img_pil, ref_arr, strength=0.9):
    a=np.asarray(img_pil).astype(np.float32); m=iris_mask(a)
    rh,rs,_=iris_stats(ref_arr)
    hsv=np.asarray(Image.fromarray(a[...,:3].astype(np.uint8)).convert("HSV")).astype(np.float32)
    h2=hsv.copy(); h2[...,0][m]=rh; h2[...,1][m]=np.clip(np.maximum(hsv[...,1][m]*1.25,rs*1.35),0,255)
    rgb2=np.asarray(Image.fromarray(h2.astype(np.uint8),"HSV").convert("RGB")).astype(np.float32)
    w=np.asarray(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32)[...,None]/255*strength
    rgb=a[...,:3]*(1-w)+rgb2*w
    return Image.fromarray(np.clip(np.concatenate([rgb,a[...,3:4]],-1),0,255).astype(np.uint8),"RGBA")
