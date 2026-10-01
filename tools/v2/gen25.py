import math, re
import gen24, gen23 as G
from gen18 import *
DC = G.DC
C = gen24.C + """
.dm{background:#fff;border:3px solid #16121f;border-radius:18px;box-shadow:7px 7px 0 #16121f;overflow:hidden;font-family:Arial,Helvetica,sans-serif}
.dmt{height:54px;background:#2a2a2a;display:flex;align-items:center;gap:14px;padding:0 18px;color:#fff;font-size:22px}
.dmt .sep{width:1.5px;height:26px;background:#666}
.dmg{position:relative}
.dmbtn{position:absolute;right:12px;width:52px;height:52px;border-radius:8px;background:#f2f2f2;border:1.5px solid #ccc;display:flex;align-items:center;justify-content:center}
.dmtb{height:52px;background:linear-gradient(#f7f7f7,#e9e9e9);border-top:1.5px solid #d4d4d4;border-bottom:1.5px solid #d4d4d4;display:flex;align-items:center;justify-content:space-between;padding:0 20px}
.dmr{display:flex;border-bottom:1.5px solid #e2e2e2;min-height:66px}
.dmr .gt{flex:none;width:74px;background:#f0f0f0;position:relative;display:flex;align-items:center;justify-content:center}
.dmr .gt .no{position:absolute;left:5px;top:3px;font-size:14px;color:#333}
.dmr .ex{flex:1;display:flex;align-items:center;justify-content:space-between;padding:6px 20px;font-family:'Times New Roman',S,serif;font-size:31px}
.dmr .ex i{font-family:'Times New Roman',S,serif}
.dmr .val{font-family:Arial;font-size:21px;color:#333;background:#eee;border-radius:6px;padding:3px 10px}
"""
FOLDER = '<svg width="34" height="28" viewBox="0 0 34 28" fill="none" stroke="#fff" stroke-width="2.4"><path d="M2 5h10l3 3h17v18H2z"/><path d="M2 12h30"/></svg>'
WRENCH = '<svg width="28" height="28" viewBox="0 0 24 24" fill="#555"><path d="M21 7a5 5 0 0 1-6.6 4.7L6.5 19.6a2 2 0 1 1-2.8-2.8l7.9-7.9A5 5 0 0 1 17 3l-3 3 1 3 3 1z"/></svg>'
HOME = '<svg width="28" height="28" viewBox="0 0 24 24" fill="#555"><path d="M12 3l10 9h-3v9h-5v-6h-4v6H5v-9H2z"/></svg>'
TB = '<svg width="30" height="30" viewBox="0 0 24 24" stroke="#555" stroke-width="3"><path d="M12 3v18M3 12h18"/></svg>'
UNDO = '<svg width="34" height="26" viewBox="0 0 34 26" fill="#555"><path d="M2 12l9-9v6c10 0 18 4 21 14-4-6-10-8-21-8v6z"/></svg>'
REDO = '<svg width="34" height="26" viewBox="0 0 34 26" fill="#bbb"><path d="M32 12l-9-9v6C13 9 5 13 2 23c4-6 10-8 21-8v6z"/></svg>'
GEAR = '<svg width="30" height="30" viewBox="0 0 24 24" fill="#555"><path d="M19.4 13a7.5 7.5 0 0 0 0-2l2.1-1.6-2-3.5-2.5 1a7.7 7.7 0 0 0-1.7-1L15 3.3h-4l-.4 2.6a7.7 7.7 0 0 0-1.7 1l-2.5-1-2 3.5L6.6 11a7.5 7.5 0 0 0 0 2l-2.1 1.6 2 3.5 2.5-1a7.7 7.7 0 0 0 1.7 1l.4 2.6h4l.4-2.6a7.7 7.7 0 0 0 1.7-1l2.5 1 2-3.5zM12 15.5a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7z"/></svg>'
CHEV = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="2.6"><path d="M5 5l7 7 7-7M5 12l7 7 7-7"/></svg>'

def icon(col, kind='wave'):
    c = DC[col]
    if kind == 'pt':
        return f'<svg width="48" height="48" viewBox="0 0 48 48"><circle cx="24" cy="24" r="21" fill="{c}"/><circle cx="24" cy="24" r="6" fill="#fff"/></svg>'
    if kind == 'num':
        return f'<svg width="48" height="48" viewBox="0 0 48 48"><circle cx="24" cy="24" r="21" fill="#fff" stroke="#bbb" stroke-width="2"/></svg>'
    return f'<svg width="48" height="48" viewBox="0 0 48 48"><circle cx="24" cy="24" r="21" fill="{c}"/><path d="M9 28c4-14 9-14 12-4s8 10 12-4 6-4 6-4" fill="none" stroke="#fff" stroke-width="4.2" stroke-linecap="round"/></svg>'

def graph(items, xr, yr, W=962, H=360):
    html = G.desmos([], items, xr, yr, W=W, H=H)
    svg = re.search(r'<svg.*</svg>', html, re.S).group(0)
    svg = svg.replace('font-size="17" fill="#333"', 'font-size="21" fill="#111"')
    return svg

def dm(title, exprs, items, xr, yr, H=290):
    rows = ''.join(f'<div class="dmr"><div class="gt"><span class="no">{i}</span>{icon(c, k)}</div><div class="ex"><span>{t}</span>{f"<span class=val>= {v}</span>" if v else ""}</div></div>' for i, (c, k, t, v) in enumerate(exprs, 1))
    return f'''<div class="dm"><div class="dmt">{FOLDER}<span class="sep"></span><span>{title}</span></div>
<div class="dmg">{graph(items, xr, yr, H=H)}<div class="dmbtn" style="top:12px">{WRENCH}</div><div class="dmbtn" style="top:74px">{HOME}</div></div>
<div class="dmtb">{TB}<span style="display:flex;gap:26px">{UNDO}{REDO}</span><span style="display:flex;gap:22px">{GEAR}{CHEV}</span></div>{rows}</div>'''
