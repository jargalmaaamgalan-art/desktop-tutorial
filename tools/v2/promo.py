"""GMP enrolment poster (photo left, offer right). python3 promo.py -> /home/claude/preview/promo.png"""
import base64, sys
sys.argv = [sys.argv[0]]
import gen41
from gen41 import F
from playwright.sync_api import sync_playwright

T, T2, G, CREAM = '#0b2a38', '#123b4c', '#f3b045', '#fff8ea'
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-photo.jpg', 'rb').read()).decode()

MARK = f'''<svg viewBox="0 0 100 100" width="74" height="74"><g fill="none" stroke="#fff" stroke-width="4"><circle cx="50" cy="40" r="32"/><ellipse cx="50" cy="40" rx="14" ry="32"/><path d="M50 8V72M20 28Q50 38 80 28M20 52Q50 62 80 52"/></g>
<path d="M12 80Q30 68 50 82Q70 68 88 80L84 92Q68 82 50 94Q32 82 16 92Z" fill="{G}"/></svg>'''

def ico(kind):
    s = 'fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'
    d = {'doc': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>',
         'chart': '<path d="M4 20h16M7 16v-5M12 16V7M17 16v-9"/>',
         'group': '<circle cx="9" cy="8" r="3"/><circle cx="16" cy="9" r="2.5"/><path d="M3 19c0-3 3-5 6-5s6 2 6 5M14 19c0-2 2-4 4-4s3 1 3 3"/>',
         'laptop': '<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 19h20"/>',
         'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>'}[kind]
    return f'<svg viewBox="0 0 24 24" width="30" height="30" {s}>{d}</svg>'

def card(title, days, extra):
    chips = ''.join(f'<span>{d}</span>' for d in days)
    return f'''<div class="card"><div class="ct">SAT <b>{title}</b></div>
<div class="row"><div><div class="days">{chips}</div><div class="tz">Монголын цагаар</div><div class="time">20:00 - 21:20</div></div>{extra}</div></div>'''

MATH = f'''<div class="side"><div class="lap"><div class="scr"><svg viewBox="0 0 120 60" width="120" height="60"><path d="M6 50Q30 6 60 30T114 10" fill="none" stroke="{G}" stroke-width="3"/><path d="M6 54H114M10 6V54" stroke="#9fb6c2" stroke-width="2"/></svg></div><div class="base"></div></div><div class="cap">Desmos + алгебр, геометр,<br>дата анализ</div></div>'''
ENG = f'''<div class="side"><div class="score"><div class="sl">Сурагчийн оноо · 2026 оны 5-р сар</div><div class="big">1560<small>/ 1600</small></div><div class="sub"><span>Унших, бичих <b>770</b></span><span>Математик <b>790</b></span></div></div></div>'''

FEATS = [('doc', 'College Board-ийн албан ёсны асуултуудаар бэлтгэнэ'), ('chart', 'Долоо хоног бүр ахиц, сул чадварын тайлан эцэг эхэд'),
         ('group', 'Цөөн сурагчтай бүлэг, хүүхэд бүрд анхаарна'), ('laptop', 'Англи, Монгол хэлээр, онлайнаар Канадаас 🇨🇦')]
feats = ''.join(f'<div class="f"><i>{ico(k)}</i><span>{t}</span></div>' for k, t in FEATS)

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('SS', 'source-serif-4', [700, 800])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;background:{T};font-family:IN,sans-serif;color:#fff;overflow:hidden;position:relative}}
.ph{{position:absolute;left:0;top:0;width:430px;height:1350px;background:{T} url({PHOTO}) center top/100% auto no-repeat;}}
.ph:after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,42,56,0) 42%,rgba(11,42,56,1) 68%)}}
.who{{position:absolute;left:0;bottom:0;width:430px;padding:0 30px 60px;z-index:2}}
.who h2{{font-family:SS,serif;font-size:40px;font-weight:800;line-height:1.1}}
.who .role{{color:{G};font-weight:800;font-size:17px;letter-spacing:1.5px;margin:10px 0 12px;text-transform:uppercase}}
.who p{{font-size:18px;line-height:1.4;color:#dbe6ec}}
.rt{{position:absolute;left:430px;top:0;width:650px;height:1350px;padding:36px 36px 30px 34px;display:flex;flex-direction:column;gap:22px}}
.logo{{display:flex;align-items:center;gap:14px;margin-bottom:4px}}
.logo .n{{font-family:SS,serif;font-weight:800;font-size:34px;letter-spacing:1px;line-height:1}}
.logo .s{{color:{G};font-weight:600;font-size:17px;letter-spacing:2.5px;margin-top:6px}}
.card{{background:{T2};border:2px solid #24546a;border-radius:22px;padding:18px 22px 20px}}
.ct{{font-family:SS,serif;font-size:42px;font-weight:800;line-height:1;margin-bottom:12px}}.ct b{{color:{G}}}
.row{{display:flex;align-items:center;justify-content:space-between;gap:14px}}
.days{{display:flex;gap:8px;margin-bottom:10px}}.days span{{background:{CREAM};color:{T};font-weight:800;font-size:19px;padding:6px 14px;border-radius:9px}}
.tz{{font-size:17px;color:#b8cbd5}}.time{{white-space:nowrap;font-family:SS,serif;font-size:36px;font-weight:800;color:{G};line-height:1.1}}
.side{{text-align:center;color:#dbe6ec;font-size:15px;line-height:1.3}}
.lap{{width:210px;margin:0 auto 8px}}.scr{{background:#1a2a33;border:4px solid #c9d6de;border-bottom:0;border-radius:10px 10px 0 0;padding:10px 0 4px;display:flex;justify-content:center}}.base{{height:14px;background:#c9d6de;border-radius:0 0 10px 10px}}
.score{{background:{CREAM};color:{T};border-radius:18px;padding:14px 18px;min-width:270px;text-align:left}}
.sl{{font-size:14px;font-weight:600;color:#4a6675;letter-spacing:.5px}}
.big{{font-family:SS,serif;font-size:60px;font-weight:800;line-height:1.05}}.big small{{font-size:22px;color:#4a6675;margin-left:6px;font-family:IN}}
.sub{{display:flex;gap:18px;font-size:15px;color:#4a6675;margin-top:4px}}.sub b{{color:{T};font-size:20px;margin-left:4px}}
.fl{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.f{{background:{T2};border:2px solid #24546a;border-radius:16px;padding:12px 14px;display:flex;align-items:center;gap:12px;font-size:17px;line-height:1.3;font-weight:600}}
.f i{{flex:none;width:46px;height:46px;border-radius:50%;background:{G};color:{T};display:flex;align-items:center;justify-content:center}}
.cta{{background:{G};color:{T};font-weight:800;font-size:34px;text-align:center;padding:22px;border-radius:60px;letter-spacing:1.5px;box-shadow:0 8px 0 #b47d1f}}
.foot{{display:flex;justify-content:space-between;align-items:center;font-size:20px;font-weight:600;margin-top:auto}}
.foot span{{display:flex;align-items:center;gap:8px}}
.disc{{font-size:11px;color:#7d97a5;line-height:1.3}}
</style></head><body>
<div class="ph"></div>
<div class="who"><h2>Жаргалмаа Амгалан</h2><div class="role">Математикийн багш · 2010 оноос</div><p>Цогц сургалтын төвийн багш. 2025 оноос хойш Канад улсаас онлайнаар хичээл зааж байна.</p></div>
<div class="rt">
<div class="logo">{MARK}<div><div class="n">GLOBAL MATH PREP</div><div class="s">JARGALMAA AMGALAN</div></div></div>
{card('Математик', ['Да', 'Лх', 'Ба'], MATH)}
{card('Англи хэл', ['Мя', 'Пү', 'Ня'], ENG)}
<div class="fl">{feats}</div>
<div class="cta">ЭЛСЭЛТ НЭЭЛТТЭЙ →</div>
<div class="foot"><span>🌐 globalmathprep.academy</span><span>💬 WhatsApp +1 428 880 1826</span></div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
</div></body></html>'''

open('/home/claude/preview/promo.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
    pg.goto('file:///home/claude/preview/promo.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo.png'); b.close()
print('ok')
