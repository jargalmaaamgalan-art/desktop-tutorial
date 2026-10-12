import chars
T,G='#1b3b48','#f3b045'
def logo_mark(face=True, arms='wave'):
    wave = '' if arms is None else {'wave':'<path d="M70 190 Q30 160 40 110" /><path d="M330 190 Q370 160 360 110"/>','hips':'<path d="M70 200 Q30 240 80 270"/><path d="M330 200 Q370 240 320 270"/>','up':'<path d="M72 170 Q20 120 50 60"/><path d="M328 170 Q380 120 350 60"/>'}[arms]
    hands = [] if arms is None else {'wave':[(40,110),(360,110)],'hips':[(80,270),(320,270)],'up':[(50,60),(350,60)]}[arms]
    h=''.join(f'<circle cx="{x}" cy="{y}" r="16" fill="#fff" stroke="{T}" stroke-width="5"/>' for x,y in hands)
    return (f'<svg viewBox="-10 -10 420 420" xmlns="http://www.w3.org/2000/svg">'
     f'<g fill="none" stroke="{T}" stroke-width="18" stroke-linecap="round">{wave}</g>{h}'
     f'<circle cx="200" cy="160" r="135" fill="{T}" stroke="#fff" stroke-width="12"/>'
     '<g fill="none" stroke="#fff" stroke-width="7" opacity=".85"><ellipse cx="200" cy="160" rx="62" ry="135"/><path d="M200 25 V295"/><path d="M75 110 Q200 150 325 110"/><path d="M75 215 Q200 255 325 215"/></g>'
     + (""+'<circle cx="158" cy="150" r="24" fill="#fff"/><circle cx="242" cy="150" r="24" fill="#fff"/><circle cx="164" cy="154" r="12" fill="#14232c"/><circle cx="248" cy="154" r="12" fill="#14232c"/><circle cx="168" cy="149" r="4" fill="#fff"/><circle cx="252" cy="149" r="4" fill="#fff"/>'
     f'<path d="M160 200 Q200 240 240 200 Z" fill="{G}" stroke="#14232c" stroke-width="5" stroke-linejoin="round"/><circle cx="116" cy="196" r="14" fill="#ff8fa3" opacity=".8"/><circle cx="284" cy="196" r="14" fill="#ff8fa3" opacity=".8"/>' if face else '') +
     f'<path d="M50 330 Q120 280 200 340 Q280 280 350 330 L335 375 Q270 335 200 385 Q130 335 65 375Z" fill="{G}" stroke="{T}" stroke-width="6" stroke-linejoin="round"/><path d="M200 340 V385" stroke="{T}" stroke-width="5"/>'
     '</svg>')
def nest(svg,x,y,w): return svg.replace('<svg ',f'<svg x="{x}" y="{y}" width="{w}" height="{w}" ',1)
def hoodie(sp):
    sp=dict(sp); sp['outfit']=T; sp['sleeve']=T
    emb=('<g transform="translate(200,330) scale(.19) translate(-200,-200)">'+logo_mark(face=False,arms=None).replace('<svg viewBox="-10 -10 420 420" xmlns="http://www.w3.org/2000/svg">','').replace('</svg>','')+'</g>')
    sp['torso_extra']=emb
    sp['hat']=sp.get('hat','')
    return sp
def scene(word,mood,mm,side='r'):
    kid=chars.kid(hoodie(chars.CAST[word]),mood)
    return (f'<svg viewBox="0 0 560 440" xmlns="http://www.w3.org/2000/svg" width="560" height="440">'
            +nest(kid,0,50,340)+nest(logo_mark(arms=mm),270,110,280)+'</svg>')
if __name__=='__main__':
    jobs=[('DRAW','out','wave'),('HOLD','happy','up'),('TRACE','think','hips')]
    cells=''.join(f'<div style="background:#fbf6ec;border-radius:20px;padding:8px;text-align:center;font:700 20px Arial">{scene(w,m,a)}{w}</div>' for w,m,a in jobs)
    hdr='<div style="background:#1b3b48;border-bottom:8px solid #f3b045;color:#fff;font:700 34px Georgia,serif;padding:18px 28px;letter-spacing:2px">GLOBAL MATH PREP <span style="color:#f3b045;font-size:22px;margin-left:16px">JARGALMAA AMGALAN</span></div>'
    open('/home/claude/preview/logomas.html','w').write(f'<body style="margin:0;background:#dfe7ee;width:1760px">{hdr}<div style="display:grid;grid-template-columns:repeat(3,576px);gap:12px;padding:12px">{cells}</div>')
