import re
"""SAT multi-meaning word posts, one design technique per post.
Run: python3 gen41.py [--video] WORD [WORD ...]   (WORD in words.WORDS; default all)"""
import sys, os, base64
import gen30, gen29, gen38
from gen18 import HERE
from words import WORDS

FD = '/home/claude/fontlab/node_modules/@fontsource'
RNG = {'latin': 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD',
       'cyrillic': 'U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116'}

def F(fam, pkg, weights):
    out = ''
    for w in weights:
        for sub in ('latin', 'cyrillic'):
            p = f'{FD}/{pkg}/files/{pkg}-{sub}-{w}-normal.woff2'
            if os.path.exists(p):
                wd = '100 900' if len(weights) == 1 else str(w)
                out += "@font-face{font-family:%s;font-weight:%s;src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s}\n" % (fam, wd, base64.b64encode(open(p, 'rb').read()).decode(), RNG[sub])
    return out

POLY = 'polygon(50% 0%,61% 18%,80% 8%,78% 30%,100% 35%,84% 52%,98% 70%,76% 72%,75% 94%,58% 82%,50% 100%,42% 82%,25% 94%,24% 72%,2% 70%,16% 52%,0% 35%,22% 30%,20% 8%,39% 18%)'

BASE = """
.pg:before{background:var(--ink)}
.top{top:34px} .top img{height:70px;background:#fff;border-radius:40px;padding:6px 22px}
.top span{font-family:var(--fb);font-weight:900;font-size:26px;color:var(--ink)}
.ft{font-family:var(--fb);color:var(--ink);border-top:2px dashed currentColor;opacity:.85}
.mn{gap:20px;font-family:var(--fb)}
.hd{display:flex;justify-content:space-between;align-items:center;gap:14px}
.hd .l{display:flex;align-items:center;gap:16px}
.no{flex:none;width:90px;height:90px;border-radius:50%;background:var(--a);color:var(--on);font-family:var(--ft);font-size:56px;display:flex;align-items:center;justify-content:center}
.of,.dom{background:var(--card);color:var(--on);border:3px solid var(--on);border-radius:30px;padding:8px 22px;font-weight:900;font-size:23px;letter-spacing:1.5px}
.em{font-size:84px;line-height:1;filter:drop-shadow(0 0 3px #fff) drop-shadow(0 0 3px #fff);animation:fl 3s ease-in-out infinite}
.T{font-family:var(--ft);color:var(--ink);line-height:1.02}
.en{font-size:30px;font-weight:700;color:var(--ink);line-height:1.3}
.mg{align-self:flex-start;background:var(--a);color:var(--on);border-radius:44px;padding:10px 32px;font-size:46px;font-weight:900}
.ex{background:var(--card);color:var(--on);border:3px solid var(--on);border-radius:26px;padding:16px 26px;font-size:38px;font-weight:700;line-height:1.3}
.k{background:var(--a);padding:0 8px;border-radius:10px;font-weight:900;font-size:1.1em}
.vis{display:flex;align-items:flex-end;justify-content:center;gap:16px;position:relative;height:380px}
.mas{flex:none;width:340px;height:340px;position:relative}
.mas svg{filter:drop-shadow(4px 0 0 #fff) drop-shadow(-4px 0 0 #fff) drop-shadow(0 4px 0 #fff) drop-shadow(0 -4px 0 #fff) drop-shadow(0 8px 10px rgba(0,0,0,.25));width:100%;height:100%;animation:bob 1.6s ease-in-out infinite;transform-origin:50% 100%}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-1.5deg)}50%{transform:translateY(-12px) rotate(1.5deg)}}
.vis .q{max-width:400px;margin-bottom:150px;background:var(--card);color:var(--on);border:3px solid var(--on);border-radius:28px;padding:14px 22px;font-size:32px;font-weight:800;line-height:1.25;animation:pop .6s 1s both}
.vis.rev{flex-direction:row-reverse}.prop{font-size:130px;line-height:1;position:absolute;right:10px;bottom:6px}
.rxn{align-self:center;background:var(--b);color:var(--on);border-radius:44px;padding:12px 28px;font-weight:900;font-size:32px;display:flex;gap:14px;align-items:center;text-align:center}
.rxn .lb{font-size:19px;letter-spacing:2px;opacity:.65;font-weight:900;white-space:nowrap;flex:none}.rxn span{text-wrap:balance}.rxn span b{color:inherit;text-decoration:underline;text-decoration-thickness:5px;text-underline-offset:5px}
.sat{font-weight:900;font-size:54px;letter-spacing:-1px;color:var(--ink)} .sat span{color:var(--a2)}
.pov{font-size:38px;font-weight:900;color:var(--a2);font-style:italic;line-height:1.25}
.W{font-family:var(--ft);color:var(--ink);line-height:.95}
.cv{display:flex;align-items:center;gap:20px}.cv .mas{width:340px;height:340px}
.stks{flex:1;display:flex;flex-direction:column;gap:18px;align-items:flex-start}
.s1,.s2,.s3{border-radius:16px;padding:8px 20px;font-weight:900;color:var(--on)}
.s1{background:var(--a);font-size:46px;transform:rotate(4deg)}.s2{background:var(--b);font-size:28px;transform:rotate(-3deg)}.s3{background:var(--card);font-size:28px;transform:rotate(2deg);border:3px solid var(--on)}
.sw{align-self:flex-start;background:var(--a);color:var(--on);border-radius:44px;padding:12px 28px;font-weight:900;font-size:30px}
.T2{font-family:var(--ft);color:var(--ink);line-height:1.1}.T2 .k2,.T3 .k2{color:var(--a2)}
.T3{font-family:var(--ft);color:var(--ink);line-height:1.05}
.sent{background:var(--card);color:var(--on);border:3px solid var(--on);border-radius:26px;padding:18px 26px;font-size:38px;font-weight:700;line-height:1.3}
.opts{display:flex;flex-direction:column;gap:12px}
.opt{display:flex;align-items:center;gap:20px;background:var(--card);color:var(--on);border:3px solid var(--on);border-radius:60px;padding:10px 26px 10px 12px;font-size:36px;font-weight:900}
.opt i{flex:none;width:64px;height:64px;border-radius:50%;background:var(--a);color:var(--on);font-style:normal;font-family:var(--ft);font-size:38px;display:flex;align-items:center;justify-content:center}
.vis.sm{height:215px}.vis.sm .mas{width:215px;height:215px}.vis.sm .q{margin-bottom:50px;font-size:26px;max-width:480px;padding:12px 18px}.vis .mas{width:310px;height:310px}
.note{font-size:21px;font-weight:700;text-align:center;color:var(--ink);opacity:.8}
.ban{background:var(--a);color:var(--on);border-radius:26px;padding:16px 26px;font-size:32px;font-weight:900;line-height:1.3}
.g4{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.g4 .c{border-radius:22px;padding:12px 18px;color:var(--on);border:3px solid var(--on)}
.g4 .c b{display:block;font-family:var(--ft);font-size:40px}
.g4 .c u{text-decoration:none;display:block;font-size:26px;font-weight:900}
.g4 .c i{display:block;font-size:24px;font-style:normal;font-weight:700;margin-top:2px}
.g4 .c em{display:block;font-style:normal;font-size:26px;font-weight:900;margin-top:2px}
.c1{background:var(--c1)}.c2{background:var(--c2)}.c3{background:var(--c3)}.c4{background:var(--c4)}
.su{display:flex;gap:18px;align-items:stretch}
.su .qr{background:var(--card);color:var(--on);border:3px solid var(--on);border-radius:26px;text-align:center;padding:12px}
.su .qr img{width:180px;height:180px;display:block}.su .qr div{font-weight:800;font-size:21px;margin-top:4px}
.su .info{flex:1;background:var(--card);color:var(--on);border:3px solid var(--on);border-radius:26px;padding:12px 22px;display:flex;flex-direction:column;justify-content:center;gap:7px;font-size:25px;font-weight:700}
.su .info h4{font-family:var(--ft);font-size:34px;font-weight:400}
"""

# ---------------------------------------------------------------- skins
SKINS = {}

SKINS['comic'] = dict(
  vars='--ink:#111;--on:#111;--card:#fff;--a:#ffd92e;--a2:#e63946;--b:#4fd1ff;--c1:#ffd92e;--c2:#4fd1ff;--c3:#ff8fa3;--c4:#b8f27c;--ft:Bangers,RB;--fb:RB,sans-serif',
  fonts=lambda: F('Bangers', 'bangers', [400]) + F('RB', 'rubik', [700, 800, 900]),
  ts=(118, 0.46), wsz=(300, 0.46), t2=64, t3=66,
  css="""
.pg{background:radial-gradient(circle,#ff9aa8 3.5px,transparent 4px) 0 0/28px 28px,#fff3a6}
.T{background:#ffd92e;border:6px solid #111;padding:4px 22px;transform:rotate(-2deg);box-shadow:8px 8px 0 #111;align-self:flex-start;letter-spacing:1px}
.no{background:#e63946;color:#fff;border:5px solid #111;box-shadow:4px 4px 0 #111}
.of,.dom{border-radius:6px;box-shadow:4px 4px 0 #111;border-width:4px}
.en{background:#fff;border:3px solid #111;padding:8px 16px;align-self:flex-start;font-weight:800}
.mg{border-radius:6px;border:5px solid #111;box-shadow:6px 6px 0 #111;transform:rotate(1deg);font-family:Bangers,RB;font-weight:400;letter-spacing:1px;font-size:54px}
.ex{border-radius:4px;border-width:5px;box-shadow:7px 7px 0 #111}
.k{background:#ffd92e;box-shadow:inset 0 -4px 0 #e63946}
.vis{height:350px;border:7px solid #111;background:repeating-conic-gradient(#8fdcff 0 10deg,#cfeeff 10deg 20deg);box-shadow:8px 8px 0 #111;overflow:hidden;align-items:flex-end;padding-bottom:8px}
.vis .q{border-radius:50%/60%;border-width:4px;padding:22px 30px;margin-bottom:120px;position:relative;margin-left:10px}
.vis .q:after{content:'';position:absolute;right:-18px;bottom:6px;width:36px;height:36px;background:#fff;border-right:4px solid #111;border-bottom:4px solid #111;transform:skewX(-30deg) rotate(25deg)}
.prop{background:#ffd92e;clip-path:""" + POLY + """;width:200px;height:200px;display:flex;align-items:center;justify-content:center;font-size:88px;right:-6px;top:6px;bottom:auto}
.rxn{border:5px solid #111;border-radius:6px;box-shadow:6px 6px 0 #111;font-family:Bangers,RB;font-weight:400;font-size:38px;letter-spacing:1px}
.W{-webkit-text-stroke:9px #111;paint-order:stroke fill;color:#e63946;text-shadow:10px 10px 0 #111;transform:rotate(-3deg)}
.opt{border-radius:6px;border-width:5px;box-shadow:6px 6px 0 #111}.opt i{border:4px solid #111;background:#ffd92e}
.sent,.ban,.g4 .c,.su .qr,.su .info{border-width:5px;border-radius:6px;box-shadow:6px 6px 0 #111}
.ban{border:5px solid #111}.T2,.T3{text-shadow:4px 4px 0 #ffd92e}
""")

SKINS['notebook'] = dict(
  vars='--ink:#1e2a52;--on:#1e2a52;--card:#fffdf0;--a:#fff176;--a2:#e0475b;--b:#ffb3c7;--c1:#fff176;--c2:#a7e3ff;--c3:#ffb3c7;--c4:#c5f0a4;--ft:Caveat,cursive;--fb:Caveat,cursive',
  fonts=lambda: F('Caveat', 'caveat', [400, 700]),
  ts=(150, 0.5), wsz=(190, 0.56), t2=66, t3=68,
  css="""
.pg{background:linear-gradient(90deg,transparent 88px,#ef5b5b 88px,#ef5b5b 91px,transparent 91px),repeating-linear-gradient(#fdfcf3 0 47px,#a9c9ee 47px 49px)}
.pg:after{content:'';position:absolute;left:20px;top:150px;width:40px;height:1100px;background:radial-gradient(circle,#d9d2bd 0 17px,transparent 18px) 0 0/40px 380px}
.mn{left:118px;right:50px}.top{left:118px}
.T{font-weight:700;background:linear-gradient(transparent 58%,#fff176 58%);align-self:flex-start;padding:0 14px;transform:rotate(-1deg)}
.no{background:none;border:5px solid #e0475b;color:#e0475b;font-size:70px;transform:rotate(-8deg)}
.of,.dom{border:3px dashed #1e2a52;background:transparent;font-size:30px;font-weight:700}
.en{font-size:40px;font-weight:700}
.mg{border-radius:4px;font-size:58px;font-weight:700;transform:rotate(-2deg);box-shadow:4px 6px 12px rgba(0,0,0,.22);padding:2px 28px}
.ex{border:none;border-radius:3px;font-size:50px;font-weight:700;box-shadow:3px 5px 12px rgba(0,0,0,.2);position:relative;line-height:1.2}
.ex:before{content:'';position:absolute;top:-18px;left:42%;width:130px;height:36px;background:rgba(255,160,180,.75);transform:rotate(-3deg)}
.k{background:linear-gradient(transparent 25%,#fff176 25%);border-radius:0}
.vis .q{border-radius:46%/55%;border-style:dashed;font-size:46px;font-weight:700;padding:22px 34px;margin-bottom:110px}
.mas svg{filter:drop-shadow(4px 0 0 #fff) drop-shadow(-4px 0 0 #fff) drop-shadow(0 4px 0 #fff) drop-shadow(0 -4px 0 #fff) drop-shadow(3px 6px 6px rgba(0,0,0,.3))}
.rxn{border:3px dashed #1e2a52;font-size:44px;font-weight:700;background:#ffb3c7}.rxn .lb{font-size:26px}
.W{font-weight:700;background:linear-gradient(transparent 62%,#fff176 62%);align-self:flex-start;padding:0 20px;transform:rotate(-2deg)}
.sat{font-size:62px}.pov{font-size:50px}
.s1{font-size:62px}.s2,.s3{font-size:40px}
.sw{font-size:44px;border-radius:10px;transform:rotate(-2deg)}
.opt{border-radius:6px;font-size:44px;border-style:dashed;padding:4px 20px 4px 8px}.opt i{border-radius:6px;font-size:44px;background:#ffb3c7;width:54px;height:54px}
.sent{font-size:46px;border:none;box-shadow:3px 5px 12px rgba(0,0,0,.2);border-radius:3px}
.ban{font-size:40px;transform:rotate(-1deg);border-radius:4px;font-weight:700}
.g4 .c{border-radius:4px;border:none;box-shadow:3px 5px 12px rgba(0,0,0,.2)}
.g4 .c b{font-size:46px;font-weight:700}.g4 .c u{font-size:32px}.g4 .c i{font-size:28px}.g4 .c em{font-size:30px}
.su .info h4{font-size:42px;font-weight:700}.su .info{font-size:28px}.su .qr div{font-size:24px}.su .qr img{width:150px;height:150px}
.note{font-size:30px}.ft{font-size:28px}.top span{font-size:30px}
""")

SKINS['cards'] = dict(
  vars='--ink:#fff;--on:#1b1f3b;--card:#fff9e6;--a:#ffe27a;--a2:#ff6b6b;--b:#7cf0d3;--c1:#ffd1ff;--c2:#a5f3fc;--c3:#fef08a;--c4:#bbf7d0;--ft:Russo,RB;--fb:RB,sans-serif',
  fonts=lambda: F('Russo', 'russo-one', [400]) + F('RB', 'rubik', [700, 800, 900]),
  ts=(78, 0.66), wsz=(330, 0.66), t2=56, t3=56,
  css="""
.pg{background:radial-gradient(circle at 25% 15%,#3b82f6 0,transparent 55%),radial-gradient(circle at 85% 90%,#a855f7 0,transparent 55%),repeating-linear-gradient(45deg,rgba(255,255,255,.05) 0 14px,transparent 14px 28px),#0f1336}
.mn{left:66px;right:66px;top:134px;bottom:98px;border-radius:44px;padding:20px 26px;background:linear-gradient(#fff6d6,#ffe9a8);border:12px solid #f5c542;box-shadow:0 0 0 5px #7a5a00,0 24px 50px rgba(0,0,0,.55);gap:12px;justify-content:center}
.T,.T2,.T3{color:#1b1f3b}.en,.note{color:#1b1f3b}.sat,.pov{color:#1b1f3b}.W{color:#1b1f3b}
.T{background:#fff;border:4px solid #1b1f3b;border-radius:14px;padding:6px 18px;box-shadow:0 5px 0 #c9a227}
.no{background:#ff6b6b;color:#fff;border:4px solid #1b1f3b;width:80px;height:80px;font-size:44px}
.no:after{content:' HP';font-size:18px;margin-left:4px;margin-top:20px}
.en:before{content:'★ MEANING · ';color:#c9a227;font-weight:900}.en{background:#fff2c2;border-radius:10px;padding:10px 16px;font-size:30px;color:#1b1f3b}
.mg{background:#7cf0d3;border:4px solid #1b1f3b;font-family:Russo,RB;font-weight:400;font-size:46px;border-radius:16px}
.ex{font-style:italic;background:#fff;font-size:38px;border-width:3px;border-radius:14px}
.vis{height:430px;background:linear-gradient(135deg,#ffd1ff,#a5f3fc,#fef08a,#fbcfe8);border:6px solid #b8860b;border-radius:18px;overflow:hidden;box-shadow:inset 0 0 40px rgba(255,255,255,.7)}
.vis:before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(115deg,transparent 0 24px,rgba(255,255,255,.35) 24px 40px);animation:none}
.mas{width:380px;height:380px;z-index:1}.vis .q{z-index:1;font-size:32px;margin-bottom:150px;max-width:340px}
.prop{font-size:110px;z-index:1}
.rxn{border:4px solid #1b1f3b;border-radius:14px;font-size:32px;background:#7cf0d3}
.sw,.s1,.s2,.s3{font-family:Russo,RB;font-weight:400}.s1{font-size:38px}
.ban,.sent,.g4 .c,.su .qr,.su .info,.opt{border-width:4px}
.W{text-shadow:6px 6px 0 #ffd24a;transform:none}.sat{font-size:44px}.pov{font-size:30px}
.dom,.of{background:#fff;font-size:20px}.em{font-size:70px}
.opt{font-size:30px}.sent{font-size:32px}.ban{font-size:27px}.g4 .c b{font-size:34px}.g4 .c u{font-size:23px}.g4 .c i{font-size:21px}.g4 .c em{font-size:23px}.su .info{font-size:21px}.su .info h4{font-size:28px}.su .qr img{width:150px;height:150px}
.vis.sm{height:190px}.vis.sm .mas{width:180px;height:180px}
""")

SKINS['blueprint'] = dict(
  vars="--ink:#fff;--on:#0b3a6e;--card:#fff;--a:#ffe14d;--a2:#ffe14d;--b:#ffe14d;--c1:#cfe8ff;--c2:#ffe14d;--c3:#b9f6ca;--c4:#ffd1dc;--ft:Plex,monospace;--fb:Plex,monospace",
  fonts=lambda: F('Plex', 'ibm-plex-mono', [400, 500, 700]),
  ts=(88, 0.62), wsz=(250, 0.78), t2=50, t3=52,
  css="""
.pg{background:linear-gradient(rgba(255,255,255,.2) 2px,transparent 2px) 0 0/40px 40px,linear-gradient(90deg,rgba(255,255,255,.2) 2px,transparent 2px) 0 0/40px 40px,linear-gradient(rgba(255,255,255,.07) 1px,transparent 1px) 0 0/10px 10px,linear-gradient(90deg,rgba(255,255,255,.07) 1px,transparent 1px) 0 0/10px 10px,#0d4f94}
.T{font-weight:700;border:4px solid #fff;padding:8px 18px;text-transform:uppercase;position:relative}
.T:before{content:'';position:absolute;left:-12px;top:-12px;width:22px;height:22px;border-left:4px solid #ffe14d;border-top:4px solid #ffe14d}
.no{background:#ffe14d;border-radius:0;font-weight:700}.of,.dom{border-radius:0;background:transparent;color:#fff;border-color:#fff;font-size:20px;font-weight:700}
.en{color:#cfe8ff;font-size:27px}.mg{border-radius:0;font-weight:700;font-size:40px;color:#0b3a6e}
.ex{background:transparent;color:#fff;border:3px dashed #fff;border-radius:0;font-size:34px}.k{background:#ffe14d;color:#0b3a6e;border-radius:0}
.vis{border:3px solid #fff;background:rgba(255,255,255,.07);height:370px}
.vis:before{content:'FIG. 1';position:absolute;left:12px;top:8px;color:#ffe14d;font-weight:700;font-size:20px;letter-spacing:2px}
.vis .q{background:transparent;color:#fff;border:3px solid #fff;border-radius:0;font-size:26px;position:relative;max-width:380px;margin-bottom:130px}
.vis .q:after{content:'';position:absolute;right:-60px;bottom:-30px;width:60px;border-top:3px solid #fff;transform:rotate(30deg);transform-origin:left}
.mas svg{filter:drop-shadow(3px 0 0 #fff) drop-shadow(-3px 0 0 #fff) drop-shadow(0 3px 0 #fff) drop-shadow(0 -3px 0 #fff)}
.prop{font-size:90px;right:14px;top:30px;bottom:auto}
.rxn{border-radius:0;box-shadow:6px 6px 0 #ffe14d;background:#fff;font-size:26px}.rxn span b{color:#c2410c}
.W{font-weight:700;border:5px solid #fff;padding:6px 20px;align-self:flex-start;text-transform:uppercase}.sat{font-size:42px}.pov{font-size:28px;color:#ffe14d}
.s1,.s2,.s3,.sw,.opt,.sent,.ban,.g4 .c,.su .qr,.su .info{border-radius:0}
.opt{font-size:30px}.opt i{border-radius:0}.sent{font-size:32px;background:transparent;color:#fff;border:3px dashed #fff}
.ban{font-size:27px}.g4 .c b{font-size:30px}.g4 .c u{font-size:22px}.g4 .c i{font-size:20px}.g4 .c em{font-size:22px}.su .info{font-size:21px}.su .info h4{font-size:26px;font-weight:700}
.T2,.T3{font-weight:700}.note{font-size:19px}
""")

SKINS['postcard'] = dict(
  vars='--ink:#3b2a1a;--on:#3b2a1a;--card:#fffaf0;--a:#ffd7a0;--a2:#b91c1c;--b:#9be0d0;--c1:#ffd7a0;--c2:#b8e0f6;--c3:#ffc9d4;--c4:#cdeac0;--ft:Playfair,serif;--fb:Pangolin,RB,sans-serif',
  fonts=lambda: F('Playfair', 'playfair-display', [900]) + F('Pangolin', 'pangolin', [400]) + F('RB', 'rubik', [700, 800]),
  ts=(104, 0.74), wsz=(240, 0.78), t2=58, t3=58,
  css="""
.pg{background:repeating-linear-gradient(45deg,rgba(0,0,0,.03) 0 6px,transparent 6px 12px),#d6b27f}
.mn{left:58px;right:58px;top:132px;bottom:96px;padding:24px 30px;background:#fffaf0;border:16px solid transparent;border-image:repeating-linear-gradient(45deg,#d62839 0 20px,#fffaf0 20px 32px,#2563eb 32px 52px,#fffaf0 52px 64px) 16;box-shadow:0 20px 40px rgba(0,0,0,.35);gap:14px;justify-content:center}
.T{color:#9b1c1c;font-weight:900;text-transform:uppercase}.W{color:#9b1c1c;font-weight:900}.sat,.pov{color:#3b2a1a}.pov{color:#9b1c1c}
.no{border-radius:4px;background:#fff;border:3px dotted #9b1c1c;color:#9b1c1c;transform:rotate(3deg);font-family:Playfair,serif;font-weight:900}
.of,.dom{border:none;background:transparent;border-bottom:3px solid #9b1c1c;border-radius:0;font-size:20px;color:#9b1c1c}
.en{font-size:34px}.mg{background:transparent;border-bottom:4px solid #9b1c1c;border-radius:0;padding:0 6px;font-size:56px;font-weight:400;color:#1e3a8a}
.ex{border:none;background:repeating-linear-gradient(transparent 0 52px,#c9b79c 52px 54px);border-radius:0;padding:0 6px;font-size:50px;font-weight:400;line-height:54px}
.k{background:#ffd7a0;font-weight:400;font-size:1.05em}
.vis{height:440px}.vis .mas{width:390px;height:390px}.vis .q{border:none;background:#fff;border:3px solid #3b2a1a;border-radius:10px;font-size:38px;font-weight:400;transform:rotate(-2deg);margin-bottom:120px}
.prop{background:#fff;border:4px dotted #9b1c1c;padding:8px;font-size:84px;right:6px;top:0;bottom:auto;transform:rotate(4deg);width:130px;height:150px;display:flex;align-items:center;justify-content:center}
.rxn{border:3px solid #3b2a1a;border-radius:10px;font-size:38px;font-weight:400;background:#9be0d0}
.opt,.sent,.ban,.g4 .c,.su .qr,.su .info,.s1,.s2,.s3,.sw{border-radius:10px}.opt{font-size:36px;font-weight:400}.opt i{font-family:Playfair,serif;font-weight:900}
.sent{font-size:40px;font-weight:400}.ban{font-size:34px;font-weight:400}.g4 .c b{font-size:30px}.g4 .c u{font-size:28px;font-weight:400}.g4 .c i{font-size:26px;font-weight:400}.g4 .c em{font-size:28px;font-weight:400}
.su .info{font-size:25px;font-weight:400}.su .info h4{font-size:34px}.su .qr img{width:160px;height:160px}.note{font-size:22px}
.sat{font-size:44px}.pov{font-size:40px;font-weight:400}.s1,.s2,.s3{font-weight:400}.s1{font-size:44px}.em{font-size:76px}
.vis.sm{height:200px}.vis.sm .mas{width:200px;height:200px}.hd{margin-top:-4px}
""")

SKINS['infographic'] = dict(
  vars='--ink:#12263f;--on:#12263f;--card:#fff;--a:#ffb703;--a2:#e4572e;--b:#8ecae6;--c1:#ffb703;--c2:#8ecae6;--c3:#f4a6a6;--c4:#b5e48c;--ft:Oswald,sans-serif;--fb:NU,sans-serif',
  fonts=lambda: F('Oswald', 'oswald', [700]) + F('NU', 'nunito', [700, 800, 900]),
  ts=(138, 0.46), wsz=(300, 0.46), t2=72, t3=72,
  css="""
.pg{background:#f6f2e9}
.pg:after{content:'';position:absolute;right:-140px;top:420px;width:460px;height:460px;border-radius:50%;background:#8ecae6;opacity:.45;z-index:0}
.T{font-weight:700;text-transform:uppercase;border-left:20px solid #ffb703;padding-left:18px;letter-spacing:1px}
.no{background:#12263f;color:#ffb703;border-radius:16px;font-weight:700}
.of,.dom{border:none;background:#12263f;color:#fff;border-radius:8px;font-size:20px}
.en{font-size:30px}.mg{background:transparent;border:5px solid #12263f;color:#12263f;border-radius:14px;font-size:42px}
.ex{border:none;border-left:16px solid #219ebc;border-radius:8px;box-shadow:0 8px 20px rgba(18,38,63,.12);font-size:36px}
.k{background:#ffb703}
.vis{height:345px;background:#fff;border-radius:22px;box-shadow:0 8px 20px rgba(18,38,63,.12);background:linear-gradient(#219ebc,#219ebc) 6% 100%/9% 34% no-repeat,linear-gradient(#8ecae6,#8ecae6) 20% 100%/9% 52% no-repeat,linear-gradient(#ffb703,#ffb703) 34% 100%/9% 70% no-repeat,linear-gradient(#e4572e,#e4572e) 48% 100%/9% 46% no-repeat,#fff}
.vis .q{border-radius:22px 22px 22px 4px;border:none;background:#12263f;color:#fff;font-size:30px}
.prop{font-size:100px;right:22px;top:14px;bottom:auto}
.rxn{border-radius:14px;background:#ffb703;font-family:NU,sans-serif;font-size:30px}
.W{font-weight:700;text-transform:uppercase;color:#12263f;text-shadow:10px 10px 0 #ffb703}.sat{font-size:50px}.pov{font-size:34px}
.opt,.sent,.ban,.g4 .c,.su .qr,.su .info{border:none;border-radius:14px;box-shadow:0 8px 20px rgba(18,38,63,.12)}
.opt i{border-radius:12px;background:#12263f;color:#ffb703}.ban{background:#12263f;color:#fff}.g4 .c{border-top:10px solid #12263f}
.g4 .c b{font-weight:700;font-size:44px}.T2,.T3{font-weight:700;text-transform:uppercase}.su .info h4{font-weight:700}
""")

SKINS['retro'] = dict(
  vars='--ink:#fff;--on:#0b0630;--card:#fff;--a:#39ff88;--a2:#ffe14d;--b:#ffe14d;--c1:#39ff88;--c2:#35d0ff;--c3:#ff4fd8;--c4:#ffe14d;--ft:PS,monospace;--fb:PS,monospace',
  fonts=lambda: F('PS', 'press-start-2p', [400]),
  ts=(70, 1.02), wsz=(190, 1.02), t2=34, t3=34,
  css="""
.pg{background:repeating-linear-gradient(rgba(0,0,0,.28) 0 2px,transparent 2px 4px),radial-gradient(#2d1b7a,#0b0630)}
.pg:before{background:linear-gradient(90deg,#ff4fd8,#ffe14d,#39ff88,#35d0ff)}
.mn{gap:18px}.T{color:#39ff88;text-shadow:5px 5px 0 #ff4fd8;line-height:1.2}
.no{background:#ffe14d;border-radius:0;box-shadow:0 0 0 4px #fff,7px 7px 0 4px #000;font-size:38px;width:86px;height:86px}
.of,.dom{border:4px solid #fff;border-radius:0;background:#0b0630;color:#fff;font-size:14px;letter-spacing:0;line-height:1.5}
.em{font-size:76px}.en{font-size:22px;line-height:1.6;color:#fff}
.mg{background:#ffe14d;border-radius:0;font-size:30px;box-shadow:0 0 0 4px #fff,8px 8px 0 4px #000;font-weight:400;line-height:1.5}
.ex{background:#0b0630;color:#fff;border:4px solid #fff;border-radius:0;font-size:26px;line-height:1.7;box-shadow:8px 8px 0 #000}
.k{background:#39ff88;color:#0b0630;border-radius:0;font-weight:400;font-size:1em;padding:2px 6px}
.vis{height:380px;border:4px solid #fff;background:linear-gradient(#10104a,#0b0630);border-radius:0;box-shadow:8px 8px 0 #000;overflow:hidden}
.vis:before{content:'';position:absolute;left:0;right:0;bottom:0;height:60px;background:repeating-linear-gradient(90deg,#39ff88 0 38px,#1f9c52 38px 40px)}
.vis .q{background:#0b0630;color:#39ff88;border:4px solid #fff;border-radius:0;font-size:20px;line-height:1.6;font-weight:400;max-width:400px;margin-bottom:150px;z-index:1}
.mas{z-index:1;margin-bottom:34px}.prop{font-size:84px;z-index:1;right:16px;top:14px;bottom:auto}
.rxn{border-radius:0;font-size:20px;line-height:1.6;box-shadow:0 0 0 4px #fff,8px 8px 0 4px #000;background:#ffe14d;font-weight:400;flex-wrap:wrap;justify-content:center}.rxn .lb{font-size:12px;white-space:nowrap}.rxn span b{color:#d6249f;font-weight:400}
.W{color:#39ff88;text-shadow:8px 8px 0 #ff4fd8}.sat{font-size:30px}.pov{font-size:20px;line-height:1.7}
.s1{font-size:26px}.s2,.s3{font-size:15px;line-height:1.5}.sw{font-size:18px;border-radius:0}.s1,.s2,.s3{border-radius:0}
.opt,.sent,.ban,.g4 .c,.su .qr,.su .info{border-radius:0;border:4px solid #fff;box-shadow:6px 6px 0 #000}
.opt{font-size:22px;background:#0b0630;color:#fff}.opt i{border-radius:0;font-size:26px}.sent{font-size:24px;line-height:1.7;background:#0b0630;color:#fff}
.ban{font-size:20px;line-height:1.6}.g4 .c b{font-size:22px}.g4 .c u{font-size:15px;line-height:1.5}.g4 .c i{font-size:19px;line-height:1.3;font-family:RB,sans-serif}.g4 .c em{font-size:21px;font-family:RB,sans-serif;font-weight:900}
.su .info{font-size:21px;line-height:1.4;font-family:RB,sans-serif;font-weight:700;background:#0b0630;color:#fff}.su .info h4{font-size:19px;color:#39ff88}.su .qr img{width:150px;height:150px}.note{font-size:15px;line-height:1.6;font-family:RB,sans-serif}.ft,.top span{font-size:14px}
.vis.sm{height:210px}.vis.sm .mas{width:190px;height:190px;margin-bottom:20px}.vis.sm .q{font-size:15px;margin-bottom:60px}
""")

SKINS['newspaper'] = dict(
  vars='--ink:#161616;--on:#161616;--card:#f8f2e2;--a:#ffe08a;--a2:#b3201a;--b:#ffe08a;--c1:#ffe08a;--c2:#d7e6f2;--c3:#f3c8c3;--c4:#d3e8c3;--ft:Playfair,serif;--fb:Playfair,serif',
  fonts=lambda: F('Playfair', 'playfair-display', [700, 900]),
  ts=(104, 0.72), wsz=(250, 0.72), t2=58, t3=60,
  css="""
.pg{background:repeating-linear-gradient(0deg,rgba(0,0,0,.025) 0 2px,transparent 2px 4px),#efe7d4}
.pg:before{background:#161616}.mn{gap:16px}
.hd:before{content:'THE WORD TIMES';position:absolute;left:0;right:0;top:-34px;text-align:center;font-family:Playfair,serif;font-weight:900;font-size:26px;letter-spacing:6px;border-bottom:3px double #161616;padding-bottom:4px;color:#161616}
.hd{margin-top:36px;position:relative}
.T{font-weight:900;text-transform:uppercase;border-top:7px solid #161616;border-bottom:3px solid #161616;padding:8px 0;letter-spacing:-1px}
.no{background:#b3201a;color:#fff;border-radius:0;font-weight:900}.of,.dom{border:none;border-radius:0;background:transparent;font-size:19px;border-bottom:3px solid #161616;font-weight:900}
.en{font-style:italic;font-size:30px;font-weight:700}.mg{background:transparent;border-left:10px solid #b3201a;border-radius:0;font-size:44px;font-style:italic;font-weight:900;padding:0 0 0 20px}
.ex{background:transparent;border:none;border-top:2px solid #161616;border-bottom:2px solid #161616;border-radius:0;font-size:36px;font-weight:700}
.k{background:#ffe08a;font-weight:900}
.vis{height:380px;border:3px solid #161616;background:radial-gradient(rgba(0,0,0,.16) 1.6px,transparent 2px) 0 0/8px 8px,#ddd2b8}
.vis:after{content:'PHOTO: BEAVER, SPECIAL CORRESPONDENT';position:absolute;left:0;right:0;bottom:-34px;font-size:17px;font-weight:700;letter-spacing:2px}
.vis .q{border-radius:0;border:3px solid #161616;background:#f8f2e2;font-size:30px;font-style:italic;font-weight:700}
.prop{font-size:92px;right:14px;top:12px;bottom:auto}
.rxn{border-radius:0;border:3px solid #161616;font-size:30px;font-weight:700;margin-top:18px}
.W{font-weight:900;text-transform:uppercase;letter-spacing:-6px;text-shadow:8px 8px 0 #ffe08a}.sat{font-size:46px}.pov{font-size:34px;font-weight:700}
.opt,.sent,.ban,.g4 .c,.su .qr,.su .info,.s1,.s2,.s3,.sw{border-radius:0}
.opt{font-size:34px}.opt i{border-radius:0;background:#b3201a;color:#fff}.sent{font-size:38px}.ban{font-size:30px;background:#b3201a;color:#fff}
.g4 .c b{font-size:34px;font-weight:900}.g4 .c u{font-size:25px}.g4 .c i{font-size:23px}.g4 .c em{font-size:25px}.su .info{font-size:24px}.su .info h4{font-weight:900;font-size:32px}.su .qr img{width:160px;height:160px}.note{font-size:20px}
.vis.sm{height:210px}.vis.sm .mas{width:190px;height:190px}.vis.sm:after{display:none}
""")

SKINS['caseboard'] = dict(
  vars='--ink:#fff;--on:#1a1a1a;--card:#fffdf4;--a:#fff3a0;--a2:#ffe14d;--b:#fff3a0;--c1:#fff3a0;--c2:#ffd1dc;--c3:#c8ecff;--c4:#d4f4b0;--ft:Plex,monospace;--fb:Caveat,cursive',
  fonts=lambda: F('Plex', 'ibm-plex-mono', [500, 700]) + F('Caveat', 'caveat', [400, 700]),
  ts=(84, 0.62), wsz=(240, 0.62), t2=48, t3=50,
  css="""
.pg{background:radial-gradient(rgba(0,0,0,.18) 2px,transparent 3px) 0 0/10px 10px,radial-gradient(rgba(255,255,255,.12) 2px,transparent 3px) 5px 5px/14px 14px,#b98a58}
.pg:before{background:#1a1a1a}
.ft,.top span{color:#1a1a1a;opacity:1}
.T{background:#111;color:#fff;font-weight:700;padding:8px 20px;letter-spacing:2px;transform:rotate(-1deg);align-self:flex-start;text-transform:uppercase;box-shadow:4px 6px 10px rgba(0,0,0,.4)}
.no{background:#d62828;color:#fff;border-radius:6px;font-weight:700;transform:rotate(-6deg);border:4px solid #fff}
.of,.dom{background:#111;color:#fff;border:none;border-radius:4px;font-size:19px;font-family:Plex,monospace}
.en{font-family:Plex,monospace;font-weight:500;font-size:24px;background:rgba(0,0,0,.55);padding:8px 14px;color:#fff}
.mg{border-radius:3px;background:#fff3a0;font-family:Caveat,cursive;font-size:62px;font-weight:700;transform:rotate(2deg);box-shadow:4px 6px 12px rgba(0,0,0,.4);padding:2px 30px}
.ex{border:none;border-radius:2px;font-family:Caveat,cursive;font-size:52px;font-weight:700;background:repeating-linear-gradient(#fffdf4 0 58px,#b7d4f0 58px 60px);border-top:12px solid #d62828;box-shadow:4px 6px 12px rgba(0,0,0,.4);line-height:60px;padding:4px 24px 8px}
.k{background:#fff3a0;border-radius:0}
.vis{height:400px;align-items:center;justify-content:flex-start;gap:30px}
.mas{width:330px;height:330px;background:#fff;padding:12px 12px 56px;box-shadow:5px 8px 16px rgba(0,0,0,.45);transform:rotate(-3deg);flex:none}
.mas:before{content:'';position:absolute;left:50%;top:-12px;width:26px;height:26px;border-radius:50%;background:#d62828;box-shadow:inset -4px -4px 0 rgba(0,0,0,.3),0 4px 6px rgba(0,0,0,.4);z-index:2;margin-left:-13px}
.mas svg{background:#e8dcc4}
.vis .q{margin:0;max-width:520px;background:#fffdf4;border:none;border-radius:2px;font-family:Caveat,cursive;font-size:46px;font-weight:700;box-shadow:4px 6px 12px rgba(0,0,0,.4);transform:rotate(2deg);position:relative}
.vis .q:before{content:'';position:absolute;left:-30px;top:-26px;width:110px;border-top:4px solid #d62828;transform:rotate(-24deg);transform-origin:right}
.prop{font-size:90px;right:0;top:0;bottom:auto}
.rxn span b{color:#d62828}.rxn{border-radius:3px;font-family:Caveat,cursive;font-size:46px;font-weight:700;background:#fff3a0;transform:rotate(-1deg);box-shadow:4px 6px 12px rgba(0,0,0,.4)}
.W{background:#111;padding:0 24px;align-self:flex-start;font-weight:700;text-transform:uppercase;transform:rotate(-2deg);box-shadow:5px 8px 12px rgba(0,0,0,.45)}.sat{font-size:44px;font-family:Plex,monospace}.pov{font-size:50px;font-family:Caveat,cursive;color:#fff3a0;text-shadow:2px 2px 0 #000}
.s1,.s2,.s3{box-shadow:3px 5px 8px rgba(0,0,0,.4);font-family:Caveat,cursive;border-radius:2px}.s1{font-size:62px}.s2,.s3{font-size:40px}.sw{font-family:Caveat,cursive;font-size:46px;border-radius:3px}
.opt,.sent,.ban,.g4 .c,.su .qr,.su .info{border:none;border-radius:2px;box-shadow:4px 6px 12px rgba(0,0,0,.4);font-family:Caveat,cursive}
.opt{font-size:50px}.opt i{border-radius:4px;background:#d62828;color:#fff;font-size:44px}.sent{font-size:54px;line-height:1.1}.ban{font-size:46px;font-weight:700;transform:rotate(-1deg)}
.g4 .c b{font-size:46px;font-weight:700;font-family:Caveat,cursive}.g4 .c u{font-size:32px}.g4 .c i{font-size:28px}.g4 .c em{font-size:30px}
.su .info{font-size:28px}.su .info h4{font-size:40px;font-family:Caveat,cursive;font-weight:700}.su .qr img{width:150px;height:150px}.su .qr div{font-size:26px}.note{font-size:26px;font-family:Caveat,cursive;color:#fff}
.T2,.T3{font-weight:700;color:#fff;text-shadow:3px 3px 0 #000}.T2 .k2,.T3 .k2{color:#fff3a0}
.vis.sm{height:215px}.vis.sm .mas{width:200px;height:200px;padding:8px 8px 34px}.vis.sm .q{font-size:36px}
""")


# ---------------------------------------------------------------- editorial skin (College Board-style: calm, navy serif, soft tint, one highlight colour)
PAL = {  # word -> (page tint, highlight, blob)
 'DRAW': ('#fff1ec', '#ffc7b4', '#ffdccf'), 'ACCOUNT': ('#eef6ff', '#bcdcff', '#d6e9ff'),
 'HOLD': ('#eefaf1', '#b4ecc6', '#d3f3df'), 'SUPPORT': ('#fdeffa', '#ffc4ea', '#ffdcf3'),
 'ADDRESS': ('#f1f1fd', '#cdd2ff', '#dfe2ff'), 'FIGURE': ('#fff6e4', '#ffdf84', '#ffecb8'),
 'CHARGE': ('#f4edff', '#d8c4ff', '#e7dbff'), 'MAINTAIN': ('#fffbe2', '#fbe55e', '#fff1a0'),
 'TRACE': ('#eaf7f6', '#a6e4dc', '#cbeee9'), 'BEAR': ('#fbf1e6', '#f2d2a6', '#f6e0c4')}
def _curve(c):
    import urllib.parse
    s = f"<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1350'><path d='M-20 1180 Q300 1010 560 1130 T1100 1060' fill='none' stroke='{c}' stroke-width='3' stroke-dasharray='14 12'/><path d='M1100 250 Q860 330 900 520' fill='none' stroke='{c}' stroke-width='3' stroke-dasharray='14 12'/></svg>"
    return 'url("data:image/svg+xml,' + urllib.parse.quote(s) + '")'

SKINS['edit'] = dict(
  vars='--ink:#14216b;--on:#14216b;--card:#fff;--a:#fbe55e;--a2:#14216b;--b:#fbe55e;--c1:#f4f4fb;--c2:#f4f4fb;--c3:#f4f4fb;--c4:#f4f4fb;--ft:SS,serif;--fb:IN,sans-serif',
  fonts=lambda: F('SS', 'source-serif-4', [700, 800]) + F('IN', 'inter', [300, 400, 600]),
  ts=(96, 0.56), wsz=(250, 0.78), t2=60, t3=60,
  css="""
.top img{background:#fff;box-shadow:0 2px 10px rgba(20,33,107,.12)}
.top span{font-family:IN;font-weight:600;color:#14216b}
.ft{font-family:IN;font-weight:400;color:#14216b;border-top:2px dashed #14216b55;opacity:1}
.mn{left:70px;right:70px;gap:18px;justify-content:center}
.no{background:transparent;border:4px solid #14216b;color:#14216b;width:76px;height:76px;font-size:44px;font-weight:800}
.of,.dom{background:transparent;border:none;padding:0;font-family:IN;font-weight:600;font-size:22px;letter-spacing:3px;color:#14216b99}
.em{font-size:76px;filter:none}
.T{font-family:SS;font-weight:800;color:#14216b;line-height:1.05;text-transform:none}
.en{font-family:IN;font-weight:300;font-size:36px;color:#14216b;line-height:1.3}
.mg{font-family:SS;font-weight:700;font-size:46px;background:var(--hl);color:#14216b;border-radius:10px;padding:8px 26px;transform:rotate(-1.2deg);box-shadow:0 6px 16px rgba(20,33,107,.12)}
.ex{font-family:IN;font-weight:300;font-size:38px;color:#14216b;line-height:1.35;border:none;background:transparent;padding:0 0 0 26px;border-left:8px solid var(--hl);border-radius:0}
.k{background:var(--hl);font-weight:600;border-radius:8px;padding:0 8px;font-size:1em}
.vis{height:330px;background:radial-gradient(ellipse 58% 62% at 56% 58%,var(--blob) 96%,transparent 100%)}
.vis .q{font-family:SS;font-weight:700;font-size:32px;border:3px solid #14216b;border-radius:30px;background:#fff;color:#14216b;box-shadow:0 8px 20px rgba(20,33,107,.12)}
.prop{font-size:92px;top:0;bottom:auto;right:14px}
.rxn{background:var(--hl);border:3px solid #14216b;border-radius:70px;color:#14216b;font-family:SS;font-weight:700;font-size:34px;padding:16px 40px;box-shadow:0 8px 18px rgba(20,33,107,.12)}
.rxn .lb{font-family:IN;font-size:17px;font-weight:600;opacity:.6}
.rxn span b{text-decoration:none;box-shadow:inset 0 -12px 0 #fff9}
.sat{font-family:SS;font-weight:800;font-size:50px;color:#14216b}.sat span{color:#14216b}
.pov{font-family:IN;font-weight:300;font-style:italic;font-size:38px;color:#14216b}
.W{font-family:SS;font-weight:800;color:#14216b;line-height:1}
.s1{background:var(--hl);color:#14216b;font-family:SS;font-weight:700;font-style:italic;font-size:50px;border-radius:12px;transform:rotate(-2deg);box-shadow:0 6px 16px rgba(20,33,107,.14)}
.s2{background:transparent;color:#14216b;font-family:IN;font-weight:600;font-size:26px;letter-spacing:2px;transform:none;padding:0}
.s3{background:#fff;color:#14216b;font-family:IN;font-weight:600;font-size:30px;border:3px solid #14216b;transform:none}
.sw{background:var(--hl);color:#14216b;font-family:SS;font-weight:700;font-size:34px;border:3px solid #14216b}
.T2,.T3{font-family:SS;font-weight:800;color:#14216b}.T2 .k2,.T3 .k2{color:#14216b;background:var(--hl);padding:0 12px;border-radius:10px}
.sent{font-family:IN;font-weight:300;border:none;background:transparent;padding:0 0 0 26px;border-left:8px solid var(--hl);border-radius:0;font-size:42px;color:#14216b}
.opt{font-family:IN;font-weight:400;border:3px solid #14216b;background:#fff;color:#14216b;font-size:36px}
.opt i{background:transparent;border:3px solid #14216b;color:#14216b;font-family:SS;font-weight:800}
.ban{background:var(--hl);color:#14216b;font-family:IN;font-weight:600;border-radius:16px;font-size:30px}
.g4{gap:0;border-top:2px dashed #14216b66}
.g4 .c{background:transparent;border:none;border-bottom:2px dashed #14216b66;border-radius:0;padding:14px 18px;color:#14216b}
.g4 .c:nth-child(odd){border-right:2px dashed #14216b66}
.g4 .c b{font-family:SS;font-weight:800;font-size:38px}.g4 .c u{font-family:IN;font-weight:600;font-size:25px}.g4 .c i{font-family:IN;font-weight:300;font-size:24px}.g4 .c em{font-family:IN;font-weight:600;font-size:25px;background:var(--hl);border-radius:6px;padding:0 8px;display:inline-block;margin-top:6px}
.su .qr,.su .info{border:3px solid #14216b;background:#fff;color:#14216b;font-family:IN}.su .info h4{font-family:SS;font-weight:800}.su .info{font-weight:400}.note{font-family:IN;font-weight:400}
"""
)

PLAN = {w: 'edit' for w in ('BEAR','DRAW','ACCOUNT','HOLD','SUPPORT','ADDRESS','FIGURE','CHARGE','MAINTAIN','TRACE')}

# ---------------------------------------------------------------- mascot with extra moods
FUR, LIGHT, DARK = gen38.FUR, gen38.LIGHT, gen38.DARK

def bear_base(mood):
    if mood in ('think', 'fruit', 'please', 'cost', 'ears', 'out', 'sun'):
        return gen38.bear(mood)
    ear = f'<circle cx="112" cy="70" r="40" fill="{FUR}"/><circle cx="288" cy="70" r="40" fill="{FUR}"/><circle cx="112" cy="72" r="21" fill="{LIGHT}"/><circle cx="288" cy="72" r="21" fill="{LIGHT}"/>'
    body = f'<ellipse cx="200" cy="318" rx="108" ry="88" fill="{FUR}"/><ellipse cx="200" cy="332" rx="62" ry="62" fill="{LIGHT}"/><ellipse cx="130" cy="396" rx="42" ry="17" fill="{DARK}"/><ellipse cx="270" cy="396" rx="42" ry="17" fill="{DARK}"/>'
    head = f'<circle cx="200" cy="165" r="108" fill="{FUR}"/><ellipse cx="200" cy="200" rx="56" ry="42" fill="{LIGHT}"/><ellipse cx="200" cy="178" rx="19" ry="13" fill="{DARK}"/>'
    op = ''.join(f'<circle cx="{x}" cy="145" r="12" fill="{DARK}"/><circle cx="{x+4}" cy="141" r="4" fill="#fff"/>' for x in (158, 242))
    big = ''.join(f'<circle cx="{x}" cy="142" r="17" fill="#fff" stroke="{DARK}" stroke-width="4"/><circle cx="{x}" cy="144" r="9" fill="{DARK}"/>' for x in (158, 242))
    smug = ''.join(f'<path d="M{x-16} 150 Q{x} 134 {x+16} 150 Z" fill="{DARK}"/><path d="M{x-18} 140 L{x+18} 140" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>' for x in (158, 242))
    shut = ''.join(f'<path d="M{x-16} 148 Q{x} 164 {x+16} 148" stroke="{DARK}" stroke-width="6" fill="none" stroke-linecap="round"/>' for x in (158, 242))
    worry = op + f'<path d="M138 120 L176 130 M262 120 L224 130" stroke="{DARK}" stroke-width="6" stroke-linecap="round"/>'
    smile = f'<path d="M168 214 Q200 242 232 214" stroke="{DARK}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    grin = f'<path d="M165 212 Q200 262 235 212 Z" fill="{DARK}"/><path d="M180 230 Q200 246 220 230 Q200 224 180 230" fill="#f26b6b"/>'
    flat = f'<path d="M172 226 Q186 216 200 226 Q214 236 228 226" stroke="{DARK}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    oh = f'<ellipse cx="200" cy="228" rx="26" ry="22" fill="{DARK}"/><ellipse cx="200" cy="236" rx="14" ry="9" fill="#f26b6b"/>'
    arm = lambda x, y, r=0: f'<ellipse cx="{x}" cy="{y}" rx="30" ry="62" fill="{FUR}" transform="rotate({r} {x} {y})"/>'
    paw = lambda x, y: f'<circle cx="{x}" cy="{y}" r="32" fill="{FUR}"/><circle cx="{x}" cy="{y}" r="15" fill="{LIGHT}"/>'
    hang = arm(100, 300, 12) + arm(300, 300, -12)
    up = arm(78, 235, -22) + arm(322, 235, 22) + paw(54, 180) + paw(346, 180)
    P = {
      'happy': body + up + head + ear + op + grin,
      'wow': body + up + head + ear + big + oh,
      'flex': body + arm(80, 250, -10) + arm(320, 250, 10) + paw(72, 192) + paw(328, 192) + head + ear + smug + grin,
      'point': body + arm(100, 300, 12) + arm(330, 262, 60) + paw(384, 228) + head + ear + smug + smile,
      'shrug': body + arm(70, 312, -55) + arm(330, 312, 55) + paw(19, 276) + paw(381, 276) + head + ear + worry + flat,
      'sleepy': body + hang + head + ear + shut + smile + '<text x="300" y="70" font-size="60" font-weight="900" fill="#60a5fa" font-family="Arial Black,sans-serif">Z</text><text x="344" y="30" font-size="40" font-weight="900" fill="#93c5fd" font-family="Arial Black,sans-serif">z</text>',
    }
    return f'<svg viewBox="-10 -10 420 420" xmlns="http://www.w3.org/2000/svg">{P[mood]}</svg>'



# ---------------------------------------------------------------- species: same skeleton, different animal
EAR0 = f'<circle cx="112" cy="70" r="40" fill="{FUR}"/><circle cx="288" cy="70" r="40" fill="{FUR}"/><circle cx="112" cy="72" r="21" fill="{LIGHT}"/><circle cx="288" cy="72" r="21" fill="{LIGHT}"/>'
HEAD0 = f'<circle cx="200" cy="165" r="108" fill="{FUR}"/>'
def tri(f, i, tall=1.0):
    y = 56 - 50 * tall
    return (f'<path d="M72 100 L92 {y:.0f} L158 60 Z" fill="{f}"/><path d="M328 100 L308 {y:.0f} L242 60 Z" fill="{f}"/>'
            f'<path d="M98 84 L102 {y+36:.0f} L134 62 Z" fill="{i}"/><path d="M302 84 L298 {y+36:.0f} L266 62 Z" fill="{i}"/>')
def beak(c): return f'<path d="M180 168 L220 168 L200 210 Z" fill="{c}" stroke="{DARK}" stroke-width="4" stroke-linejoin="round"/>'
SPECIES = {
 'DRAW': dict(fur='#f08a24', light='#fff1dc', behind=tri('#f08a24', '#3b2210'),
    over='<ellipse cx="206" cy="64" rx="84" ry="30" fill="#7c3aed"/><circle cx="216" cy="32" r="9" fill="#7c3aed"/><path d="M130 70 Q206 92 282 66" stroke="#5b21b6" stroke-width="5" fill="none"/>'),
 'ACCOUNT': dict(fur='#8a6a4a', light='#f3e2c0', behind=tri('#8a6a4a', '#d9b98a', .7), head='<ellipse cx="200" cy="158" rx="90" ry="62" fill="#fff7e0"/>',
    over=beak('#f5a623') + '<path d="M200 276 L164 256 L164 296Z M200 276 L236 256 L236 296Z" fill="#dc2626"/><circle cx="200" cy="276" r="9" fill="#991b1b"/>'),
 'HOLD': dict(fur='#9aa8b6', light='#dfe6ec', behind='<circle cx="52" cy="150" r="58" fill="#9aa8b6"/><circle cx="52" cy="150" r="36" fill="#f3b7c4"/><circle cx="348" cy="150" r="58" fill="#9aa8b6"/><circle cx="348" cy="150" r="36" fill="#f3b7c4"/>',
    over=f'<path d="M178 188 Q168 268 210 276 Q240 278 232 254 Q214 260 224 188 Z" fill="#8795a3" stroke="{DARK}" stroke-width="4" stroke-linejoin="round"/>'),
 'SUPPORT': dict(fur='#d9a066', light='#fff3e0', behind='<ellipse cx="92" cy="130" rx="34" ry="72" fill="#8a5a2b" transform="rotate(22 92 130)"/><ellipse cx="308" cy="130" rx="34" ry="72" fill="#8a5a2b" transform="rotate(-22 308 130)"/>',
    over=f'<path d="M186 230 Q200 276 214 230 Z" fill="#f26b6b" stroke="{DARK}" stroke-width="3"/><rect x="138" y="262" width="124" height="16" rx="8" fill="#dc2626"/><circle cx="200" cy="292" r="11" fill="#ffd43b" stroke="{DARK}" stroke-width="3"/>'),
 'ADDRESS': dict(fur='#9fb4c9', light='#eef3f8', behind='',
    over=beak('#fbbf24') + '<path d="M104 94 Q200 6 296 94 Z" fill="#1d4ed8"/><rect x="96" y="86" width="208" height="18" rx="9" fill="#1e3a8a"/><circle cx="200" cy="58" r="9" fill="#fbbf24"/>'),
 'FIGURE': dict(fur='#3d4f73', light='#ffffff', behind='', head='<ellipse cx="200" cy="170" rx="84" ry="74" fill="#ffffff"/>',
    over=beak('#fb923c') + '<rect x="112" y="262" width="176" height="24" rx="12" fill="#38bdf8"/><rect x="240" y="272" width="28" height="54" rx="12" fill="#38bdf8"/>'),
 'CHARGE': dict(fur='#8fa3b8', light='#dfe9f3', head='<rect x="108" y="104" width="184" height="110" rx="34" fill="#eaf6ff"/>',
    behind='<rect x="94" y="56" width="212" height="212" rx="52" fill="#8fa3b8"/><rect x="62" y="128" width="40" height="64" rx="10" fill="#6b7c8f"/><rect x="298" y="128" width="40" height="64" rx="10" fill="#6b7c8f"/><rect x="194" y="14" width="12" height="60" fill="#6b7c8f"/><circle cx="200" cy="14" r="18" fill="#ffd43b" stroke="#a16207" stroke-width="4"/>',
    over='<rect x="170" y="258" width="60" height="18" rx="6" fill="#6b7c8f"/>'),
 'MAINTAIN': dict(fur='#8a5a2c', light='#e9d3b0', behind='<circle cx="104" cy="96" r="30" fill="#5b3a1a"/><circle cx="296" cy="96" r="30" fill="#5b3a1a"/>',
    over=f'<rect x="184" y="214" width="32" height="32" rx="5" fill="#fff" stroke="{DARK}" stroke-width="4"/><path d="M200 214 V246" stroke="{DARK}" stroke-width="3"/><path d="M104 94 Q104 18 200 18 Q296 18 296 94 Z" fill="#facc15" stroke="#a16207" stroke-width="4"/><rect x="90" y="86" width="220" height="18" rx="9" fill="#eab308" stroke="#a16207" stroke-width="4"/><rect x="188" y="22" width="24" height="62" fill="#eab308"/>'),
 'TRACE': dict(fur='#b0b7c3', light='#f1f3f6', behind=tri('#b0b7c3', '#f4a6b8', .8),
    over='<path d="M188 172 L212 172 L200 190Z" fill="#f472b6"/><path d="M150 198 L84 184 M150 208 L80 210 M150 218 L88 236 M250 198 L316 184 M250 208 L320 210 M250 218 L312 236" stroke="#3b2210" stroke-width="4" stroke-linecap="round"/><path d="M200 102 L200 128 M178 106 L184 128 M222 106 L216 128" stroke="#6b7280" stroke-width="6" stroke-linecap="round"/><ellipse cx="200" cy="76" rx="126" ry="20" fill="#6b4423"/><path d="M130 76 Q132 14 200 14 Q268 14 270 76 Z" fill="#8b5e34"/><rect x="132" y="56" width="136" height="14" fill="#3b2210"/>'),
}
def bear2(mood):
    import chars
    if CUR.get('word') in chars.CAST: return chars.draw_kid(CUR['word'], mood)
    s = bear_base(mood)
    sp = SPECIES.get(CUR.get('word'))
    if not sp: return s
    assert EAR0 in s and HEAD0 in s, mood
    s = s.replace(EAR0, '').replace(HEAD0, HEAD0 + sp.get('head', ''))
    s = s.replace(FUR, sp['fur']).replace(LIGHT, sp['light'])
    i = s.index('>') + 1
    return s[:i] + sp['behind'].replace(FUR, sp['fur']) + s[i:-6] + sp['over'] + '</svg>'

# ---------------------------------------------------------------- builders
def hi(s, k):
    assert k in s, (k, s)
    return s.replace(k, f'<span class="k">{k}</span>')

def tsize(sk, title):
    base, cw = sk['ts']
    return int(min(base, 930 / (len(title) * cw)))

def mas(mood): return f'<div class="mas">{bear2(mood)}</div>'

def cover(W, D, sk):
    base, cw = sk['wsz']
    fs = int(min(base, 930 / (len(W) * cw)))
    return f"""<div class="hd"><div class="dom">DOMAIN · CRAFT AND STRUCTURE</div><div class="em">{D['cover_em']}</div></div>
<div class="sat"><span>SAT</span>&reg; Reading &amp; Writing</div>
<div class="pov">{D['pov']}</div>
<div class="W" style="font-size:{fs}px">{W}</div>
<div class="cv">{mas('sun')}<div class="stks"><div class="s1">6 MEANINGS 🤯</div><div class="s2">SKILL · Words in Context</div><div class="s3">{D['hook']}</div></div></div>
<div class="sw">Swipe to level up →</div>"""

def exp(i, X, sk):
    return f"""<div class="hd"><div class="l"><div class="no">{i}</div><div class="of">OF 6 MEANINGS</div></div><div class="em">{X['stick']}</div></div>
<div class="T" style="font-size:{tsize(sk, X['t'])}px">{X['t']}</div>
<div class="en">{X['en']}</div><div class="mg">{X['mg']}</div>
<div class="ex">{hi(X['ex'], X['key'])}</div>
<div class="vis{' rev' if i % 2 == 0 else ''}"><div class="q">{X['quip']}</div>{mas(X['mood'])}<div class="prop">{X['prop']}</div></div>
<div class="rxn"><span class="lb">YOUR TURN</span><span>{X['q']}</span></div>"""

def quiz(D, sk):
    Q = D['quiz']
    QP = re.sub(r'\s*[^\x00-\u2000]+\s*$', '', Q['quip'])
    o = ''.join(f'<div class="opt"><i>{a}</i><span>{b}</span></div>' for a, b in zip('ABC', Q['opts']))
    return f"""<div class="hd"><div class="dom">QUIZ · POLL TIME</div><div class="em">🤔</div></div>
<div class="T2" style="font-size:{sk['t2']}px">What does <span class="k2">“{Q['word']}”</span> mean here?</div>
<div class="sent">{hi(Q['sent'], Q['key'])}</div>
<div class="opts">{o}</div>
<div class="vis sm"><div class="q">{QP}</div>{mas('think')}</div>
<div class="rxn"><span>👇 Comment A, B or C below!</span></div>
<div class="note">Original Global Math Prep practice question. Not from the College Board.</div>"""

def tip(W, D, sk):
    Q = D['quiz']; letter = Q['ans']; text = Q['opts']['ABC'.index(letter)]
    cells = ''.join(f'<div class="c c{n}"><b>{a}</b><u>{b}</u><i>{x}</i><em>{d}</em></div>' for n, (a, b, x, d) in enumerate(D['cells'], 1))
    return f"""<div class="hd"><div class="dom">QUIZ ANSWER + SAT TRICK</div><div class="em">🎉</div></div>
<div class="ban">Answer: {letter} 🎯 “{Q['word']}” means {text}. Did you get it?</div>
<div class="T3" style="font-size:{sk['t3']}px">{W} has <span class="k2">4 hidden jobs</span></div>
<div class="g4">{cells}</div>
<div class="su"><div class="qr"><img src="{gen29.QR}"><div>Scan to sign up</div></div>
<div class="info"><h4>Comment “SAT” below</h4><div><b>English</b> · Tue · Thu · Sat · 20:00 to 21:20</div><div><b>Math</b> · Mon · Wed · Fri · 20:00 to 21:20</div><div style="opacity:.75">Ulaanbaatar, Mongolia time</div><div style="opacity:.75;white-space:nowrap">WhatsApp +1 428 880 1826</div></div></div>"""

CUR = {}
def make_css(a, s, t):
    sk = SKINS[CUR['skin']]
    pal = PAL.get(CUR['word'])
    extra = ''
    if CUR['skin'] == 'edit' and pal:
        extra = ':root{--hl:%s;--blob:%s}.pg{background:%s %s center/cover}.pg:before{background:%s}' % (pal[1], pal[2], _curve('#14216b44'), pal[0], pal[1])
        extra = extra.replace('background:url', 'background-image:url', 1).replace(' %s center/cover}' % pal[0], ';background-color:%s}' % pal[0])
    return gen29.CSS + sk['fonts']() + ':root{' + sk['vars'] + '}' + BASE + sk['css'] + extra

def page(C, n, T, body, tag):
    w = CUR['word']
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT R&amp;W · WORDS IN CONTEXT · {w}</span><span>{"Swipe →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''

gen30.css = make_css
gen30.page = page

def build(W):
    D = WORDS[W]; skin = PLAN[W]; sk = SKINS[skin]
    CUR.update(skin=skin, word=W)
    pages = [cover(W, D, sk)] + [exp(i, X, sk) for i, X in enumerate(D['exps'], 1)] + [quiz(D, sk), tip(W, D, sk)]
    return dict(key='W-' + W, prefix='GMP-SATWords-' + W, AC='#000', SOFT='#eee', TINT='#fff', nxt='New', pages=pages)

def run(W, video):
    post = build(W)
    gen30.render(post, video)
    out = HERE / ('out30-W-' + W)
    for f in sorted(out.glob('GMP-Transitions-*')):
        f.rename(out / f.name.replace('GMP-Transitions-W-' + W, 'GMP-SATWords-' + W))
    return out

if __name__ == '__main__':
    sel = [a for a in sys.argv[1:] if not a.startswith('--')] or list(PLAN)
    for w in sel:
        run(w, '--video' in sys.argv)
