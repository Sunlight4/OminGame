import pygame
from objects import *
from vector import Vector
class Scene(object):
    rendered=pygame.sprite.Group()
    updated=pygame.sprite.Group()
    forces=pygame.sprite.Group()
    def __init__(self, path):
        f=open(path).readlines()
        for line in f:
            if line.startswith("//"):continue
            code, groups=line.split("##")
            groups=groups.split(" ")
            code=code.split(" ")
            setup=code[0]
            code=code[1:]
            code=setup+"("+",".join(code)+")"
            o=eval(code, globals(), locals())
            
            for group in groups:
                try:exec "g = self."+group
                except:
                    g=pygame.sprite.Group()
                    exec "self."+group+" = g"
                try:g.add(o)
                except:g.append(o)
    def update(self, events):
        rendered=self.rendered
        updated=self.updated
        self.forces.update({"events":events, "rendered":rendered, "updated":updated})
        self.updated.update({"events":events, "rendered":rendered, "updated":updated})
    def draw(self, canvas):
        self.rendered.draw(canvas)

def blitcenter(surf,pos,screen): # Blit pygame.Surface with center anchor
    screen.blit(surf,[pos[0]-surf.get_size()[0]/2,pos[1]-surf.get_size()[1]/2])
def getnew(img,z):

    size = list(img.get_size())
    
    for i in range(0,1281):
        size[0]+=1
        size[1]+=1

    if size[0]-z < 0:
        size[0] = z
    if size[1]-z < 0:
        size[1] = z

    return pygame.transform.scale(img,[size[0]-z,size[1]-z])
def distance(x1,y1,x2,y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

def sortobjs(objs):
    new = []

    for i in objs:
        new.append(i.pos[1])

    new.sort()

    final = []

    for i in new:
        for obj in objs:
            if obj.pos[1] == i:
                final.append(obj)
    return final
def getangle(x1,y1,x2,y2):
    a = x2-x1
    b = y2-y1

    h = math.sqrt(a**2+b**2)

    theta = math.asin(b/float(h))

    return math.degrees(theta)
def text(text,size,color,font=None):
        
        
    font = pygame.font.Font(font,size)

    txt = font.render(text,1,color)

    return txt

class Button:
    def __init__(self,surf,pos,center=False):
        self.surf = surf
        
        if center:
            pos = [pos[0]-surf.get_size()[0]/2,pos[1]-surf.get_size()[1]/2]

        self.pos = pos
            
    def hover(self):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        sizex = self.surf.get_size()[0]
        sizey = self.surf.get_size()[1]
        if x>=self.pos[0] and x<=self.pos[0]+sizex:
            if y>=self.pos[1] and y<=self.pos[1]+sizey:
                return True
    def render(self,screen):
        screen.blit(self.surf,self.pos)

def msg(message): # Broken
    okbutton = Button(text(text='OK',color=[200,0,0]),[601,640])
    txt = text(text=message,color=[200,0,0],size=64)
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if okbutton.hover():
                    run = False

        fill([38,24,0])
        okbutton.render()
        blitcenter(txt,[640,320])
        flip()


                
def enterbox(screen,title):
    okbutton = Button(text("OK",50,[255,255,0]),[320,360],True)
    title = text(text=title,color=[200,0,0],size=50)
    txt = ''
    run = True

    chars = ['a','b','c','d','e','f','g','h','i',
             'j','k','l','m','n','o','p','q','r',
             's','t','u','v','w','x','y','z',
             '.','/',
             '1','2','3','4','5','6','7','8','9','0']
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if okbutton.hover():
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if not txt == '':
                        txt = txt[:len(txt)-1]
                elif event.key == pygame.K_SPACE:
                    txt += ' '
                elif event.key < 256:
                    key = event.key

                    if chr(key) in chars:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            txt+=chr(key).capitalize()
                        else:
                            txt+=chr(key)

        screen.fill([0,0,0])
        okbutton.render(screen)
        blitcenter(title,[320,128],screen)
        blitcenter(text(txt,50,[255,255,255]),[320,240],screen)
        pygame.display.flip()
    return txt


    
            
        
