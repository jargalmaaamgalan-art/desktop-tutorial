"""Mockup: new portal entry page (welcome, 3 steps, sign-in). Phone width, EN and MN side by side."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from playwright.sync_api import sync_playwright

LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/logo-left-light.png', 'rb').read()).decode()

T = {
 'en': dict(lang='EN', kick='Student portal', h='Welcome to Global Math Prep', sub='Digital SAT Math and Reading & Writing, live on Zoom from Canada.',
   tabNew='I am new', tabHave='I have an account',
   stepsT='Join in 3 steps', s=[('Take the free level test', 'Math or Reading & Writing · about 35 min · no account needed', 'Start the free test'),
        ('Create your account', 'Name, email, the course you want. Your teacher sees it at once.', 'Create account'),
        ('Pay and get your schedule', 'After payment your portal and class times open.', 'See schedule & fees')],
   help='Questions?', wa='WhatsApp +1 428 880 1826',
   signT='Sign in', addr='Inner address', addrH='The address your teacher gave you', pw='Password', keep='Keep me signed in', btn='Sign in',
   links=['Have an invite code?', 'Forgot password?', 'Parent with an invite']),
 'mn': dict(lang='МН', kick='Сурагчийн портал', h='Global Math Prep-д тавтай морил', sub='Digital SAT Математик, Reading & Writing. Канадаас Zoom-ээр шууд.',
   tabNew='Шинээр элсэх', tabHave='Бүртгэлтэй',
   stepsT='3 алхмаар элсэнэ', s=[('Үнэгүй түвшний тест өгөх', 'Математик эсвэл Reading & Writing · 35 мин орчим · бүртгэл шаардахгүй', 'Тест эхлүүлэх'),
        ('Бүртгэл үүсгэх', 'Нэр, имэйл, сонгох хичээл. Багш шууд харна.', 'Бүртгүүлэх'),
        ('Төлбөр төлж хуваарь авах', 'Төлбөр төлсний дараа портал, хичээлийн цаг нээгдэнэ.', 'Хуваарь, төлбөр'),],
   help='Асуух зүйл байна уу?', wa='WhatsApp +1 428 880 1826',
   signT='Нэвтрэх', addr='Дотоод хаяг', addrH='Багшийн өгсөн хаяг', pw='Нууц үг', keep='Энэ төхөөрөмж дээр нэвтэрсэн хэвээр', btn='Нэвтрэх',
   links=['Урилгын код байгаа юу?', 'Нууц үгээ мартсан', 'Эцэг эх (урилгаар)']),
}

ICON = ['<path d="M5 4h11l3 3v13H5z M8 10h8 M8 14h8 M8 18h5"/>', '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>', '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18 M8 3v4 M16 3v4"/>']
def ic(i): return f'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICON[i]}</svg>'

def phone(L):
    d = T[L]
    steps = ''.join(f'''<div class="st s{i}"><div class="num">{i+1}</div><div class="sb"><div class="stt"><i>{ic(i)}</i>{t}</div><div class="std">{x}</div>
<div class="{'pri' if i==0 else 'sec'}">{b} →</div></div></div>''' for i, (t, x, b) in enumerate(d['s']))
    return f'''<div class="ph">
<div class="hdr"><img src="{LOGO}"><div class="lg"><span class="{'on' if L=='en' else ''}">EN</span><span class="{'on' if L=='mn' else ''}">МН</span></div></div>
<div class="body">
<div class="kick">{d['kick']}</div><h1>{d['h']}</h1><p class="sub">{d['sub']}</p>
<div class="tabs"><div class="tb on"><b>1</b>{d['tabNew']}</div><div class="tb"><b>2</b>{d['tabHave']}</div></div>
<div class="card"><div class="ct">{d['stepsT']}</div>{steps}
<div class="help">{d['help']} <b>{d['wa']}</b></div></div>
<div class="card sign"><div class="ct">{d['signT']}</div>
<label>{d['addr']}</label><div class="in"></div><div class="hint">{d['addrH']}</div>
<label>{d['pw']}</label><div class="in"></div>
<div class="keep"><span>✓</span>{d['keep']}</div>
<div class="pri full">{d['btn']}</div>
<div class="lk">{' · '.join(d['links'])}</div></div>
</div></div>'''

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('NR', 'newsreader', [500, 600, 700])}{F('SS', 'source-serif-4', [600, 700])}
*{{box-sizing:border-box;margin:0}}
body{{background:#dfe6ea;padding:30px;display:flex;gap:36px;font-family:NR,SS,serif;color:#0B3C49;width:910px}}
.ph{{width:400px;background:#F3F7F8;border-radius:34px;overflow:hidden;box-shadow:0 20px 50px rgba(11,60,73,.25);border:8px solid #0d1b20}}
.hdr{{background:#0B3C49;border-bottom:4px solid #FFAD1F;padding:14px 16px;display:flex;align-items:center;justify-content:space-between}}
.hdr img{{height:34px}}
.lg{{display:flex;background:rgba(255,255,255,.12);border-radius:20px;padding:3px}}.lg span{{color:#cfe0e5;font:600 12px/1 NR,SS,serif;padding:6px 10px;border-radius:16px}}.lg .on{{background:#FFAD1F;color:#0B3C49}}
.body{{padding:20px 16px 22px}}
.kick{{font-size:11px;letter-spacing:2.5px;text-transform:uppercase;color:#12707F;font-weight:700}}
h1{{font-size:27px;line-height:1.12;margin:6px 0 8px;font-weight:700}}
.sub{{font-size:14.5px;color:#46636d;line-height:1.4}}
.tabs{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:18px 0 14px}}
.tb{{display:flex;align-items:center;gap:8px;justify-content:center;padding:11px 8px;border-radius:30px;background:#fff;border:1.5px solid #cfdde2;font-size:14px;font-weight:600;color:#46636d}}
.tb b{{width:22px;height:22px;border-radius:50%;background:#e3ecef;display:flex;align-items:center;justify-content:center;font-size:12px}}
.tb.on{{background:#0B3C49;color:#fff;border-color:#0B3C49}}.tb.on b{{background:#FFAD1F;color:#0B3C49}}
.card{{background:#fff;border-radius:20px;padding:16px;box-shadow:0 2px 0 rgba(11,60,73,.06),0 6px 18px rgba(11,60,73,.06);margin-bottom:14px}}
.ct{{font-size:18px;font-weight:700;margin-bottom:12px}}
.st{{display:flex;gap:12px;position:relative;padding-bottom:16px}}
.s0:before,.s1:before{{content:'';position:absolute;left:15px;top:34px;bottom:4px;width:2px;background:#e3ecef}}
.num{{flex:none;width:32px;height:32px;border-radius:50%;background:#FFAD1F;color:#0B3C49;font-weight:700;font-size:15px;display:flex;align-items:center;justify-content:center}}
.s1 .num,.s2 .num{{background:#0B3C49;color:#fff}}
.stt{{display:flex;align-items:center;gap:7px;font-size:16px;font-weight:700;line-height:1.2}}.stt i{{color:#12707F;display:flex}}
.std{{font-size:13px;color:#5d7882;margin:4px 0 9px;line-height:1.35}}
.pri{{display:inline-block;background:#FFAD1F;color:#0B3C49;font-weight:700;font-size:14.5px;padding:10px 16px;border-radius:30px}}
.sec{{display:inline-block;border:1.5px solid #0B3C49;color:#0B3C49;font-weight:600;font-size:13.5px;padding:8px 14px;border-radius:30px}}
.help{{font-size:13px;color:#5d7882;border-top:1px solid #e3ecef;padding-top:12px}}.help b{{color:#0B3C49}}
.sign{{opacity:.55}}
label{{display:block;font-size:11px;letter-spacing:1.8px;text-transform:uppercase;color:#46636d;font-weight:700;margin:8px 0 5px}}
.in{{height:40px;border:1.5px solid #cfdde2;border-radius:10px;background:#fbfdfd}}
.hint{{font-size:12px;color:#7a929a;margin-top:4px}}
.keep{{display:flex;align-items:center;gap:8px;font-size:13px;margin:12px 0}}.keep span{{width:18px;height:18px;border-radius:5px;background:#0B3C49;color:#fff;font-size:11px;display:flex;align-items:center;justify-content:center}}
.full{{display:block;text-align:center}}
.lk{{font-size:12px;color:#12707F;text-align:center;margin-top:12px;line-height:1.6}}
</style></head><body>{phone('en')}{phone('mn')}</body></html>'''
open('/home/claude/preview/portal-mock.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 970, 'height': 900}, device_scale_factor=2)
    pg.goto('file:///home/claude/preview/portal-mock.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/portal-mock.png', full_page=True); b.close()
print('ok')
