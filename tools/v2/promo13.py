"""GMP enrolment poster, no photo. Same family as the 182K-view announcement post."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from playwright.sync_api import sync_playwright

T, T2, G, CREAM = '#14323f', '#0c2430', '#f3b045', '#f6f1e7'
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo.png', 'rb').read()).decode()

def ic(k):
    s = 'fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"'
    d = {'doc': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>',
         'chart': '<path d="M4 20h16M7 16v-5M12 16V7M17 16v-9"/>',
         'group': '<circle cx="9" cy="8" r="3"/><circle cx="16" cy="9" r="2.5"/><path d="M3 19c0-3 3-5 6-5s6 2 6 5M14 19c0-2 2-4 4-4s3 1 3 3"/>',
         'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'}[k]
    return f'<svg viewBox="0 0 24 24" width="26" height="26" {s}>{d}</svg>'

FE = [('doc', 'College Board-ийн', 'албан ёсны асуултууд'), ('chart', 'Долоо хоног бүр', 'ахицын тайлан эцэг эхэд'),
      ('group', 'Цөөн сурагчтай', 'бүлэг, 2 - 6 хүүхэд'), ('globe', 'Канадаас онлайнаар', 'Англи, Монгол хэлээр')]
feats = ''.join(f'<div class="f"><i>{ic(k)}</i><div><b>{a}</b><span>{b}</span></div></div>' for k, a, b in FE)

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('SS', 'source-serif-4', [600, 800])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:#fff;overflow:hidden;position:relative;background:radial-gradient(1100px 800px at 20% 0%,#1d4656 0,{T} 50%,{T2} 100%)}}
.wm{{position:absolute;right:-30px;top:120px;font-family:SS,serif;font-weight:800;font-size:520px;line-height:1;color:rgba(255,255,255,.035);letter-spacing:-20px}}
.top{{position:absolute;left:64px;right:64px;top:56px;display:flex;align-items:center;justify-content:space-between}}
.top img{{height:84px}}
.tag{{background:{G};color:{T2};font-weight:800;font-size:17px;letter-spacing:3px;padding:12px 20px;border-radius:50px;text-transform:uppercase}}
.hd{{position:absolute;left:64px;right:64px;top:214px}}
.kick{{color:{G};font-weight:800;font-size:18px;letter-spacing:4px;text-transform:uppercase}}
h1{{font-family:SS,serif;font-weight:800;font-size:78px;line-height:1.02;margin-top:14px;letter-spacing:-1.5px}}
h1 em{{font-style:normal;color:{G}}}
.lead{{font-size:23px;color:#cfdde4;margin-top:18px;line-height:1.45;max-width:900px}}
.cards{{position:absolute;left:64px;right:64px;top:586px;display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.card{{background:{CREAM};color:{T2};border-radius:22px;padding:26px 28px 24px;position:relative;overflow:hidden}}
.card:before{{content:'';position:absolute;left:0;top:0;bottom:0;width:8px;background:{G}}}
.card .n{{font-family:SS,serif;font-weight:800;font-size:44px;line-height:1}}
.card .d{{display:flex;gap:8px;margin-top:16px}}.card .d span{{background:{T2};color:#fff;font-weight:800;font-size:19px;padding:7px 14px;border-radius:9px}}
.card .t{{font-size:17px;color:#55707c;margin-top:12px;font-weight:600}}
.time{{position:absolute;left:64px;right:64px;top:808px;display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 26px}}
.time b{{font-family:SS,serif;font-size:44px;font-weight:800;color:{G};line-height:1}}
.time span{{font-size:20px;color:#dbe6ec;line-height:1.35}}
.fl{{position:absolute;left:64px;right:64px;top:950px;display:grid;grid-template-columns:1fr 1fr;gap:22px 28px}}
.f{{display:flex;align-items:center;gap:14px}}
.f i{{flex:none;width:50px;height:50px;border-radius:50%;background:rgba(243,176,69,.14);color:{G};display:flex;align-items:center;justify-content:center;border:1px solid rgba(243,176,69,.4)}}
.f b{{display:block;font-size:19px;line-height:1.15}}.f span{{font-size:16px;color:#9fb6c2}}
.cta{{position:absolute;left:64px;right:64px;bottom:72px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid rgba(255,255,255,.14);padding-top:26px}}
.cta .k{{font-size:19px;color:#cfdde4;line-height:1.6}}.cta .k b{{color:#fff;font-weight:800}}
.btn{{background:{G};color:{T2};font-weight:800;font-size:25px;padding:20px 38px;border-radius:50px}}
.disc{{position:absolute;left:64px;right:64px;bottom:24px;font-size:10.5px;color:#6f8793;text-align:center}}
</style></head><body>
<div class="wm">SAT</div>
<div class="top"><img src="{LOGO}"><div class="tag">Элсэлт нээлттэй</div></div>
<div class="hd"><div class="kick">Digital SAT · 2026 оны намар</div>
<h1>Math + English,<br><em>нэг багштай, нэг дор.</em></h1>
<div class="lead">Канадаас шууд онлайнаар. 15 жилийн туршлагатай багш, хүүхэд бүрд анхаарсан цөөн сурагчтай бүлэг.</div></div>
<div class="cards">
<div class="card"><div class="n">SAT Математик</div><div class="d"><span>Да</span><span>Лх</span><span>Ба</span></div><div class="t">Алгебр · Геометр · Дата анализ · Desmos</div></div>
<div class="card"><div class="n">SAT Англи хэл</div><div class="d"><span>Мя</span><span>Пү</span><span>Ня</span></div><div class="t">Reading · Writing · Үгийн сан · Дүрэм</div></div>
</div>
<div class="time"><b>20:00 - 21:20</b><span>Монголын цагаар, хичээл бүр<br>Долоо хоногт 6 өдөр</span></div>
<div class="fl">{feats}</div>
<div class="cta"><div class="k"><b>Үнэгүй SAT тест</b> авах бол "SAT" гэж коммент бичээрэй<br>WhatsApp +1 428 880 1826 · globalmathprep.academy</div><div class="btn">Бүртгүүлэх →</div></div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
</body></html>'''
open('/home/claude/preview/promo13.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo13.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo13.png'); b.close()
print('ok')
