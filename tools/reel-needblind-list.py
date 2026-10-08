#!/usr/bin/env python3
"""Need-blind 8 schools Reel (Oct 7, 2026), editorial split layout: real campus video, hard cuts, a big white title box
and numbered pills that pop in one by one (the format of the viral list Reels the owner shared).
No university logos: names in text only. Each clip is labelled with the real place it shows.
Usage: python3 campus.py bg | stills | frames | all"""
import base64, pathlib, sys, os, json, subprocess
sys.path.insert(0, '../v2'); import gen15 as g
b = lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
FD = pathlib.Path('../fbcover/node_modules/@fontsource')
def face(name, pkg, ws):
    s = ''
    for w in ws:
        for sub, r in g.RNG.items():
            f = FD/pkg/'files'/f'{pkg}-{sub}-{w}-normal.woff2'
            if f.exists(): s += "@font-face{font-family:%s;font-weight:%d;unicode-range:%s;src:url(data:font/woff2;base64,%s)}\n" % (name, w, r, b(f))
    return s
CSS = face('M', 'montserrat', (600, 700, 800, 900)) + face('S', 'literata', (700,))
# each school's name on a card in its own colour (text only, no logos or seals)
SCHOOL = {'Harvard': '#A51C30', 'MIT': '#5A5D61', 'Yale': '#00356B', 'Princeton': '#E77500', 'Stanford': '#8C1515', 'Cornell': '#B31B1B', 'Columbia': '#1D4F91'}
s0 = open('sat.py').read()
bcss = s0[s0.index('.brand{{'):s0.index('\n', s0.index('.brand .bt small svg'))].replace('{{', '{').replace('}}', '}')
bhtml = s0[s0.index('<div class="brand">'):s0.index('</div></div>', s0.index('<div class="brand">'))+12].replace('{LG}', 'data:image/png;base64,'+b('../fbcover/logo_t.png')).replace('{{', '{').replace('}}', '}')
W, H, FPS = 1080, 1920, 30

U = '/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/'
FH = 1010   # height of the video window at the top
# (clip, start, length, crop-x fraction, place label: only when the place is true)
SHOTS = [
 (U+'4d9a3bd6-8060932-hd_1920_1080_25fps.mp4', 2.0, 4.0, 0.5, ''),
 (U+'9aa53a46-15029439_2160_3840_30fps.mp4', 0.5, 3.0, 0.5, 'Charles River, Boston'),
 (U+'e675abc3-14902158_2160_3840_30fps.mp4', 0.5, 3.0, 0.5, 'Charles River, Boston'),
 (U+'b75e1901-6145396-uhd_2160_3840_24fps.mp4', 2.0, 3.0, 0.5, ''),
 (U+'1a71d79f-6145404-uhd_2160_3840_24fps.mp4', 1.0, 3.0, 0.5, ''),
 (U+'1357ef54-7683445-hd_1080_1920_30fps.mp4', 2.5, 3.0, 0.5, ''),
 (U+'616ada45-5957445-uhd_2160_3840_24fps.mp4', 2.0, 3.0, 0.5, ''),
 (U+'d69466c6-7683402-hd_1920_1080_30fps.mp4', 1.0, 3.0, 0.5, ''),
 (U+'120c8a62-8060866-hd_1080_1920_25fps.mp4', 2.0, 3.0, 0.5, ''),
 (U+'b27941e3-7970447-uhd_3840_2160_30fps.mp4', 2.0, 4.4, 0.45, ''),
]
ST = []; t = 0
for sh in SHOTS: ST.append(round(t, 2)); t += sh[2]
DUR = round(t, 2)
# colours: each school's own colour (a colour bar, no logos)
C = {'Harvard':'#A51C30','MIT':'#5A5D61','Yale':'#00356B','Princeton':'#E77500','Dartmouth':'#00693E','Brown':'#4E3629','Amherst':'#3F1F69','Bowdoin':'#1d1d1f'}
SCHOOLS = [
 ('Harvard','REA','11/1','Олон улсын сурагч АНУ-ын сурагчтай <b>ижил</b> тэтгэлэг авна'),
 ('MIT','EA','11/1','Оюутнуудын <b>88%</b> нь өргүй төгсдөг'),
 ('Yale','SCEA','11/1','Тэтгэлгийн маягтын хугацаа: <b>12/1</b>'),
 ('Princeton','SCEA','11/1','Зээл биш, <b>буцалтгүй</b> тэтгэлэг олгодог'),
 ('Dartmouth','ED','11/1','Зээл авах <b>шаардлагагүй</b>'),
 ('Brown','ED','11/1','Тэтгэлгээ өргөдөлтэйгөө <b>хамт</b> хүсвэл 100% хангана'),
 ('Amherst','ED','11/9','SAT оноо <b>заавал биш</b>'),
 ('Bowdoin','ED I','11/15','Тэтгэлгийн баримтаа <b>тэнцсэнээс хойш 7 хоногт</b> өгнө'),
]
def school_html(k, n, plan, d, f):
    return f"""<div class="sc" id="s{k+1}" style="--c:{C[n]}">
 <div class="cnt"><b>{k+1:02d}</b><span>/ 08</span><div class="chips"><i>NEED-BLIND</i><i>100% ХЭРЭГЦЭЭ{"*" if n=="Brown" else ""}</i></div></div>
 <div class="nm"><span>{n}</span></div><div class="rl"></div>
 <div class="row r1"><small>{plan}</small><b>{d}</b>{"<em>ТЭНЦВЭЛ ЗААВАЛ ОЧНО</em>" if plan.startswith("ED") else ""}</div>
 <div class="row r2">{f}</div></div>"""
scenes = """<div class="sc" id="s0" style="--c:#c2410c">
 <div class="kick">NEED-BLIND · 2027 ЭЛСЭЛТ</div>
 <div class="hl">Гэр бүлийн орлогоос үл хамааран элсүүлдэг <em>8</em> сургууль</div>
 <div class="hs">Тэнцвэл тэтгэлгийн хэрэгцээг <b>100%</b> хангадаг. Олон улсын сурагчдад ч адилхан.</div></div>
""" + ''.join(school_html(k, *x) for k, x in enumerate(SCHOOLS)) + """
<div class="sc" id="s9" style="--c:#c2410c">
 <div class="kick">GLOBAL MATH PREP</div>
 <div class="hl">Аль сургууль нь <em>сонирхолтой</em> байна вэ?</div>
 <div class="hs">Коммент хэсэгт бичээрэй. Хадгалж аваад, найздаа илгээгээрэй.</div>
 <div class="disc">Огноо, баримтыг 2026.10.06-нд сургууль бүрийн албан ёсны сайтаас шалгасан, өөрчлөгдөж болно. Not affiliated with or endorsed by any university named.</div></div>"""
places = ''.join(f'<div class="place" id="p{k}"><b></b>{sh[4]}</div>' for k, sh in enumerate(SHOTS) if sh[4])
page = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;overflow:hidden;font-family:M;background:transparent}}
{bcss}
.topfade{{position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,0))}}
.panel{{position:absolute;left:0;right:0;top:{FH-50}px;bottom:0;background:#F6F1E7;border-radius:48px 48px 0 0;box-shadow:0 -20px 50px rgba(0,0,0,.35)}}
.panel:before{{content:'';position:absolute;left:0;right:0;top:0;height:14px;border-radius:48px 48px 0 0;background:var(--pc,#c2410c);transition:none}}
.ill{{position:absolute;right:30px;top:{FH-110}px;font:700 22px M;color:rgba(255,255,255,.85);background:rgba(0,0,0,.45);padding:6px 14px;border-radius:999px}}
.place{{position:absolute;left:36px;top:{FH-115}px;display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.55);color:#fff;font:800 28px M;padding:8px 20px 8px 14px;border-radius:999px;opacity:0}}
.place b{{width:12px;height:12px;border-radius:50%;background:#ff4b4b}}
.bars{{position:absolute;left:36px;right:36px;top:118px;display:flex;gap:6px}}
.bar{{flex:1;height:5px;border-radius:5px;background:rgba(255,255,255,.35);overflow:hidden}} .bar b{{display:block;height:100%;width:0;background:#fff}}
.sc{{position:absolute;left:70px;right:70px;top:{FH+20}px;bottom:0;opacity:0}}
.kick{{display:table;font:900 28px M;letter-spacing:4px;color:#fff;background:var(--c);padding:10px 20px;border-radius:10px}}
.hl{{margin-top:26px;font:700 82px/1.1 S;color:#15171c;letter-spacing:-1px}}
.hl em{{font-style:normal;color:var(--c)}}
.hs{{margin-top:26px;font:700 40px/1.35 M;color:#3b3f48}} .hs b{{color:var(--c);font-weight:900}}
.cnt{{display:flex;align-items:baseline;gap:12px}} .cnt b{{font:700 70px S;color:var(--c)}} .cnt span{{font:700 34px M;color:#8a8f99}}
.chips{{margin-left:auto;display:flex;gap:10px}} .chips i{{font:900 22px M;font-style:normal;letter-spacing:2px;color:var(--c);border:3px solid var(--c);padding:6px 12px;border-radius:999px}}
.nm{{overflow:hidden;margin-top:0}} .nm span{{display:block;font:700 150px/1.12 S;color:#15171c;letter-spacing:-2px}}
.rl{{height:12px;width:220px;background:var(--c);border-radius:6px;margin:10px 0 30px;transform-origin:left}}
.row{{opacity:0}}
.r1{{display:flex;align-items:baseline;gap:24px}} .r1 small{{font:900 34px M;letter-spacing:3px;color:#8a8f99}} .r1 em{{font-style:normal;align-self:center;font:900 22px M;letter-spacing:1px;color:#fff;background:#c92a2a;padding:8px 12px;border-radius:8px}} .r1 b{{font:900 104px/1 M;color:var(--c);letter-spacing:-3px}}
.r2{{margin-top:24px;font:700 52px/1.25 M;color:#15171c;padding-right:90px}} .r2 b{{color:var(--c);font-weight:900}}
.disc{{margin-top:34px;font:600 25px/1.4 M;color:#6b6f78;padding-right:60px}}
</style></head><body><div class="topfade"></div><div class="bars">{''.join(f'<div class="bar"><b id="b{i}"></b></div>' for i in range(len(SHOTS)))}</div>{bhtml}
<div class="ill">жишээ бичлэг</div>{places}
<div class="panel" id="pn"></div>{scenes}
<script>
const ST={json.dumps(ST)},DUR={DUR};
const cl=x=>Math.max(0,Math.min(1,x)); const eo=x=>1-Math.pow(1-cl(x),3);
const PLACE={json.dumps({k: True for k, sh in enumerate(SHOTS) if sh[4]})};
function render(t){{
 const pn=document.getElementById('pn'); const pp=eo(t/0.45); pn.style.transform=`translateY(${{(1-pp)*900}}px)`;
 for(let i=0;i<ST.length;i++){{
  const s=ST[i], e=(i+1<ST.length?ST[i+1]:DUR), a=t-s, el=document.getElementById('s'+i);
  document.getElementById('b'+i).style.width=(cl((t-s)/(e-s))*100)+'%';
  const pl=document.getElementById('p'+i); if(pl) pl.style.opacity=(a>=0&&t<e)?eo(a/0.3):0;
  if(a<0||t>=e+(i+1<ST.length?0:1)){{el.style.opacity=0;continue;}}
  el.style.opacity=1; pn.style.setProperty('--pc',getComputedStyle(el).getPropertyValue('--c'));
  const out=(i+1<ST.length)?cl((e-t)/0.18):1; el.style.opacity=out;
  const q=(sel,d,dur)=>eo((a-d)/(dur||0.35));
  el.querySelectorAll('.kick,.cnt').forEach(x=>{{const p=q(x,i==0?0.35:0.0); x.style.opacity=p; x.style.transform=`translateY(${{(1-p)*20}}px)`;}});
  el.querySelectorAll('.hl').forEach(x=>{{const p=q(x,i==0?0.5:0.15,0.45); x.style.opacity=p; x.style.transform=`translateY(${{(1-p)*40}}px)`;}});
  el.querySelectorAll('.hs').forEach(x=>{{const p=q(x,i==0?1.1:0.6); x.style.opacity=p; x.style.transform=`translateY(${{(1-p)*24}}px)`;}});
  el.querySelectorAll('.nm span').forEach(x=>{{const p=q(x,0.05,0.4); x.style.transform=`translateY(${{(1-p)*110}}%)`;}});
  el.querySelectorAll('.rl').forEach(x=>{{x.style.transform=`scaleX(${{q(x,0.3,0.4)}})`;}});
  el.querySelectorAll('.r1').forEach(x=>{{const p=q(x,0.45); x.style.opacity=p; x.style.transform=`translateX(${{(1-p)*-40}}px)`;}});
  el.querySelectorAll('.r2').forEach(x=>{{const p=q(x,0.75); x.style.opacity=p; x.style.transform=`translateY(${{(1-p)*20}}px)`;}});
  el.querySelectorAll('.disc').forEach(x=>{{const p=q(x,1.4); x.style.opacity=p;}});
 }}
}}
</script></body></html>"""

def bg():
    os.makedirs('list_bg', exist_ok=True); parts = []
    for k, (f, s, d, cx, _) in enumerate(SHOTS):
        sw, sh = int(W*1.15), int(FH*1.15)
        vf = f"scale={sw}:{sh}:force_original_aspect_ratio=increase,crop={sw}:{sh}:(iw-{sw})*{cx}:(ih-{sh})*{0.72 if k==3 else 0.45}"
        n = int(d*FPS)
        vf += f",fps={FPS},zoompan=z='1+0.08*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{FH}:fps={FPS},pad={W}:{H}:0:0:black"
        out = f'list_bg/p{k}.mp4'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',str(s),'-t',str(d),'-i',f,'-an','-vf',vf+',setsar=1','-c:v','libx264','-crf','18','-pix_fmt','yuv420p',out], check=True)
        parts.append(out)
    open('list_bg/list.txt','w').write(''.join(f"file '{os.path.basename(p)}'\n" for p in parts))
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','list_bg/list.txt','-c','copy','list_bg/bg.mp4'], check=True)

from playwright.sync_api import sync_playwright
def overlay(mode):
    os.makedirs('framesL', exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': W, 'height': H}); pg.set_content(page); pg.wait_for_timeout(800)
        if mode == 'stills':
            for k in range(len(ST)):
                e = ST[k+1] if k+1 < len(ST) else DUR
                pg.evaluate(f'render({e-0.3})'); pg.screenshot(path=f'lo_{k}.png', omit_background=True)
        else:
            for i in range(int(DUR*FPS)):
                pg.evaluate(f'render({i/FPS})'); pg.screenshot(path=f'framesL/f{i:04d}.png', omit_background=True)
        br.close()

mode = sys.argv[1] if len(sys.argv) > 1 else 'stills'
if mode in ('bg','all'): bg()
if mode == 'stills': overlay('stills')
if mode in ('frames','all'): overlay('frames')
if mode == 'all':
    subprocess.run(['ffmpeg','-v','error','-y','-i','list_bg/bg.mp4','-framerate',str(FPS),'-i','framesL/f%04d.png','-filter_complex','[0:v][1:v]overlay=0:0:format=auto','-t',str(DUR),'-c:v','libx264','-crf','19','-pix_fmt','yuv420p','-movflags','+faststart','GMP-Reel-NeedBlind8.mp4'], check=True)
print('ST', ST, 'DUR', DUR)
