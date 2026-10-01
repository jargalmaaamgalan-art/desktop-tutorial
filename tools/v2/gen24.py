import gen23 as G
from gen18 import *
INK = '#16121f'
C = G.C + """
.bx{background:#fff;border:3px solid #16121f;border-radius:18px;box-shadow:7px 7px 0 #16121f;overflow:hidden;font-family:Arial,Helvetica,sans-serif;color:#1e1e1e}
.bxh{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:14px 22px 12px}
.bxh .s1{font-size:21px;font-weight:700}
.bxh .s2{font-size:16px;margin-top:4px}
.bxh .tm{text-align:center;font-size:28px;font-weight:700}
.bxh .hide{display:inline-block;border:1.5px solid #1e1e1e;border-radius:14px;font-size:13px;font-weight:700;padding:1px 12px;margin-top:4px}
.bxh .tl{display:flex;gap:20px;justify-content:flex-end;font-size:14px;text-align:center}
.dash{height:4px;background:repeating-linear-gradient(90deg,#1e1e1e 0 14px,transparent 14px 20px)}
.bxb{padding:0 34px 24px}
.qrow{display:flex;align-items:center;gap:14px;background:#f0f0f0;margin:0 -34px;padding:8px 34px;border-bottom:2px solid #d9d9d9}
.qrow .n{background:#1e1e1e;color:#fff;font-weight:700;font-size:23px;min-width:40px;height:38px;display:flex;align-items:center;justify-content:center;padding:0 6px}
.qrow .mr{font-size:20px}
.qrow .abc{margin-left:auto;border:2px solid #1e1e1e;border-radius:6px;padding:0 6px;font-size:16px;font-weight:700;text-decoration:line-through}
.bxs{font-family:S,serif;font-size:33px;line-height:1.5;margin-top:20px}
.bxd{text-align:center;font-family:S,serif;font-size:36px;margin:22px 0 4px}
.bxc{display:flex;flex-direction:column;gap:14px;margin-top:22px}
.bxc div{display:flex;align-items:center;gap:18px;border:2px solid #1e1e1e;border-radius:10px;padding:12px 18px;font-family:S,serif;font-size:31px}
.bxc span.l{flex:none;width:38px;height:38px;border:2px solid #1e1e1e;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:Arial;font-size:19px;font-weight:700}
.bxf{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:14px 22px;font-size:18px;font-weight:700}
.bxf .qx{background:#1e1e1e;color:#fff;border-radius:8px;padding:7px 16px}
.bxf .bt{display:flex;gap:12px;justify-content:flex-end}
.bxf .bt span{background:#324dc7;color:#fff;border-radius:22px;padding:8px 24px}
"""
ICAL = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#1e1e1e" stroke-width="1.8"><rect x="4" y="2.5" width="16" height="19" rx="2"/><rect x="7" y="5.5" width="10" height="4"/><circle cx="8.5" cy="13" r=".9" fill="#1e1e1e"/><circle cx="12" cy="13" r=".9" fill="#1e1e1e"/><circle cx="15.5" cy="13" r=".9" fill="#1e1e1e"/><circle cx="8.5" cy="17" r=".9" fill="#1e1e1e"/><circle cx="12" cy="17" r=".9" fill="#1e1e1e"/><circle cx="15.5" cy="17" r=".9" fill="#1e1e1e"/></svg>'
IREF = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#1e1e1e" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><text x="12" y="16" text-anchor="middle" font-size="9" font-family="Georgia" font-style="italic" stroke="none" fill="#1e1e1e">x²</text></svg>'
IMORE = '<svg width="30" height="30" viewBox="0 0 24 24" fill="#1e1e1e"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>'
BOOK = '<svg width="20" height="24" viewBox="0 0 24 28" fill="none" stroke="#1e1e1e" stroke-width="2.4"><path d="M4 2h16v24l-8-6-8 6z"/></svg>'

def bluebook(n, qnum, disp, stem, choices, secs='31:24'):
    ch = ''.join(f'<div><span class="l">{l}</span><span>{c}</span></div>' for l, c in zip('ABCD', choices))
    return f'''<div class="bx"><div class="bxh"><div><div class="s1">Section 1, Module 1: Math</div><div class="s2">Directions &#8964;</div></div>
<div class="tm">{secs}<br><span class="hide">Hide</span></div>
<div class="tl"><div>{ICAL}<br>Calculator</div><div>{IREF}<br>Reference</div><div>{IMORE}<br>More</div></div></div><div class="dash"></div>
<div class="bxb"><div class="qrow"><div class="n">{qnum}</div>{BOOK}<span class="mr">Mark for Review</span><span class="abc">ABC</span></div>
{f'<div class="bxd">{disp}</div>' if disp else ''}<div class="bxs">{stem}</div><div class="bxc">{ch}</div></div>
<div class="dash"></div><div class="bxf"><span>Global Math Prep</span><span class="qx">Question {qnum} of 22 &#8963;</span><div class="bt"><span>Back</span><span>Next</span></div></div></div>'''
G.bluebook = bluebook
import importlib
