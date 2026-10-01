import gen11 as b
from playwright.sync_api import sync_playwright
R = [('#1b4a86','#1f7a66'),('#12366b','#135446'),('#0a2248','#0a3029'),('rgba(8,28,64','rgba(3,34,27'),
     ('#2f73c9','#34b38a'),('#cfe0f3','#d4efe6'),('rgba(127,214,232','rgba(140,230,200'),('#7fd6e8','#8fe6c8'),('#8fd8ff','#8fe6c8')]
def page(n,t,body):
    h=b.page(n,t,body)
    for a,c in R: h=h.replace(a,c)
    return h
out=b.g.HERE/'out13'; out.mkdir(exist_ok=True)
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':1080,'height':1350})
    for i,body in enumerate(b.S,1):
        pg.set_content(page(i,len(b.S),body)); pg.wait_for_timeout(250)
        pg.screenshot(path=str(out/f'SAT-Advice-green-{i}-of-8.png'))
    br.close()
