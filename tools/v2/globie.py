"""Globie: GMP globe character + scenes with the kids."""
import chars
from gmp_mascots import NAVY, GOLD, emblem
def globie(mood='happy', cap=True):
    fk={'happy':'happy','wow':'wow','cool':'cool','think':'think','sleepy':'sleepy','smug':'smug'}[mood]
    f=chars.face(fk,'#fff','#14216b','#ff8fa3').replace('y="130"','y="150"')
    b=('<defs><radialGradient id="gg" cx="38%" cy="32%"><stop offset="0" stop-color="#7cc4ff"/><stop offset="1" stop-color="#2563eb"/></radialGradient></defs>'
       '<circle cx="200" cy="215" r="165" fill="url(#gg)" stroke="#14216b" stroke-width="7"/>'
       '<path d="M60 150 Q100 110 150 140 Q170 190 120 215 Q70 205 60 150Z M255 85 Q315 80 345 130 Q330 175 285 160 Q250 135 255 85Z M270 250 Q330 250 345 305 Q305 340 268 305Z" fill="#4ade80"/>'
       '<ellipse cx="200" cy="215" rx="165" ry="50" fill="none" stroke="#fff" stroke-width="3" opacity=".45"/>'
       f'<g transform="translate(0,0)"><rect x="52" y="262" width="296" height="50" rx="8" fill="{NAVY}" transform="rotate(-6 200 287)"/>'
       f'<text x="200" y="302" text-anchor="middle" font-size="40" font-weight="900" fill="{GOLD}" font-family="Arial Black,sans-serif" transform="rotate(-6 200 287)" letter-spacing="6">GMP</text></g>')
    c=(f'<g transform="translate(0,-18)"><path d="M105 80 L200 36 L295 80 L200 120Z" fill="{NAVY}"/><path d="M146 98 V128 Q200 152 254 128 V98 L200 120Z" fill="#0f1850"/><path d="M285 84 V132" stroke="{GOLD}" stroke-width="6"/><circle cx="285" cy="138" r="9" fill="{GOLD}"/></g>') if cap else ''
    return f'<svg viewBox="-10 -10 420 420" xmlns="http://www.w3.org/2000/svg">{b}{f}{c}</svg>'
def nest(svg,x,y,w,rot=0):
    s=svg.replace('<svg ',f'<svg x="{x}" y="{y}" width="{w}" height="{w}" ',1)
    return f'<g transform="rotate({rot} {x+w/2} {y+w/2})">{s}</g>' if rot else s
def scene(word, how):
    sp=chars.CAST[word]
    P={ # kid mood, kid x,y,w, globie x,y,w,rot,mood, extras
     'spin': ('out', 0,60,330, 250,0,230,8,'wow','<path d="M300 40 Q330 20 360 40 M290 20 Q330 -10 380 20" stroke="#14216b" stroke-width="5" fill="none" stroke-linecap="round"/>'),
     'hug':  ('happy',0,60,330, 150,170,230,0,'happy',''),
     'lean': ('think',0,60,330, 220,150,260,0,'cool',''),
     'juggle':('wow',0,60,330, 250,-20,200,-12,'wow','<path d="M300 200 L290 250 M340 210 L345 260 M380 200 L395 250" stroke="#14216b" stroke-width="5" stroke-linecap="round"/>'),
     'ride': ('flex',0,60,330, 200,200,250,0,'happy',''),
     'push': ('out',0,60,330, 235,130,270,10,'sleepy',''),
    }[how]
    m,kx,ky,kw,gx,gy,gw,gr,gm,ex=P
    kid=chars.kid(sp,m)
    gl=globie(gm)
    order = (nest(gl,gx,gy,gw,gr)+nest(kid,kx,ky,kw)) if how=='lean' else (nest(kid,kx,ky,kw)+nest(gl,gx,gy,gw,gr))
    if how=='hug': order=nest(kid,kx,ky,kw)+nest(gl,gx,gy,gw,gr)
    return f'<svg viewBox="0 0 520 440" xmlns="http://www.w3.org/2000/svg" width="520" height="440">{order}{ex}</svg>'
if __name__=='__main__':
    jobs=[('DRAW','spin'),('HOLD','push'),('TRACE','lean'),('ACCOUNT','juggle'),('FIGURE','hug'),('CHARGE','ride')]
    cells=''.join(f'<div style="background:#fff7ec;border-radius:20px;padding:6px;text-align:center;font:700 20px Inter,Arial"><div style="filter:drop-shadow(0 0 0 #fff)">{scene(w,h)}</div>{w} · {h}</div>' for w,h in jobs)
    open('/home/claude/preview/globie.html','w').write(f'<body style="margin:0;background:#e8eefc"><div style="display:grid;grid-template-columns:repeat(3,540px);gap:12px;padding:12px;width:1680px">{cells}</div>')
