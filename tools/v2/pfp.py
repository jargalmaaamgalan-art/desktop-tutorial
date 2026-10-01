import cine, gen18
from playwright.sync_api import sync_playwright
NAVY='#0b2a40'; GOLD='#f5a623'; CREAM='#fff8ec'
def globe(cx,cy,r,col,sw):
    g=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}"/>'
    g+=f'<line x1="{cx-r}" y1="{cy}" x2="{cx+r}" y2="{cy}" stroke="{col}" stroke-width="{sw}"/>'
    g+=f'<line x1="{cx}" y1="{cy-r}" x2="{cx}" y2="{cy+r}" stroke="{col}" stroke-width="{sw}"/>'
    for k in (0.5,):
        g+=f'<ellipse cx="{cx}" cy="{cy}" rx="{r*k}" ry="{r}" fill="none" stroke="{col}" stroke-width="{sw}"/>'
    for dy in (-0.55,0.55):
        import math; hw=r*math.sqrt(1-dy*dy)
        g+=f'<line x1="{cx-hw}" y1="{cy+dy*r}" x2="{cx+hw}" y2="{cy+dy*r}" stroke="{col}" stroke-width="{sw}"/>'
    return g
def book(cx,top,w,col,col2):
    h=w*0.32; s=''
    for i,(dy,c) in enumerate([(0,col),(h*0.28,col2),(h*0.56,col)]):
        y=top+dy
        s+=f'<path d="M{cx},{y+h*0.35} C{cx-w*0.18},{y} {cx-w*0.38},{y-h*0.05} {cx-w/2},{y+h*0.12} L{cx-w/2},{y+h*0.42} C{cx-w*0.36},{y+h*0.25} {cx-w*0.17},{y+h*0.3} {cx},{y+h*0.65} Z" fill="{c}"/>'
        s+=f'<path d="M{cx},{y+h*0.35} C{cx+w*0.18},{y} {cx+w*0.38},{y-h*0.05} {cx+w/2},{y+h*0.12} L{cx+w/2},{y+h*0.42} C{cx+w*0.36},{y+h*0.25} {cx+w*0.17},{y+h*0.3} {cx},{y+h*0.65} Z" fill="{c}"/>'
    return s
def mark(cx,cy,s,gc='#fff'):
    return globe(cx,cy-s*0.12,s*0.42,gc,s*0.045)+book(cx,cy+s*0.08,s*0.95,GOLD,'#ffc85a')
A=f'<svg viewBox="0 0 1080 1080" width="1080" height="1080"><rect width="1080" height="1080" fill="{NAVY}"/>{mark(540,560,600)}</svg>'
B=f'''<div style="width:1080px;height:1080px;background:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center">
<svg viewBox="340 20 400 300" width="400" height="300">{mark(540,170,300)}</svg>
<div style="font-family:S,serif;font-weight:700;font-size:230px;color:#fff;letter-spacing:6px;line-height:1;margin-top:-10px">GMP</div>
<div style="font-family:M,sans-serif;font-weight:800;font-size:58px;color:{GOLD};letter-spacing:14px;margin-top:22px">SAT PREP</div></div>'''
C=f'''<div style="width:1080px;height:1080px;background:{GOLD};display:flex;flex-direction:column;align-items:center;justify-content:center">
<div style="font-family:IN,M,sans-serif;font-weight:900;font-size:430px;color:{NAVY};letter-spacing:-18px;line-height:.9">+1%</div>
<div style="font-family:M,sans-serif;font-weight:800;font-size:64px;color:{NAVY};letter-spacing:10px;margin-top:30px">GMP · SAT</div></div>'''
D=f'''<div style="width:1080px;height:1080px;background:{NAVY};display:flex;align-items:center;justify-content:center">
<div style="width:820px;height:820px;border-radius:50%;background:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center">
<div style="font-family:S,serif;font-weight:700;font-size:520px;color:#fff;line-height:.85">G</div>
<svg viewBox="0 0 400 140" width="480" height="168">{book(200,30,380,GOLD,'#ffc85a')}</svg></div></div>'''
css=cine.ff+gen18.serif+'*{margin:0;padding:0}body{width:1080px;height:1080px;overflow:hidden}'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1080})
    for n,h in [('A-globe-book',A),('B-GMP-wordmark',B),('C-plus-1-percent',C),('D-G-monogram',D)]:
        pg.set_content(f'<html><head><meta charset=utf-8><style>{css}</style></head><body>{h}</body></html>'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'pfp/GMP-profile-{n}.png')
    b.close()
from PIL import Image, ImageDraw
import glob
fs=sorted(glob.glob('pfp/GMP-profile-*.png')); W=260
S=Image.new('RGB',(len(fs)*(W+40)+40,W+80),'white'); m=Image.new('L',(W,W),0); ImageDraw.Draw(m).ellipse((0,0,W,W),fill=255)
for i,f in enumerate(fs): S.paste(Image.open(f).convert('RGB').resize((W,W)),(40+i*(W+40),40),m)
S.save('pfp/preview-circles.png')
