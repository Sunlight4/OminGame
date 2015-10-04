import pygame, main, copy
from utils import *
from objects import *
from entity import Character
from vector import Vector
from collections import defaultdict
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
classes={"Object":Object, "Wall":Wall, "CircleWall":CircleWall, "SquareWall":SquareWall, "RightTriangleWall":RightTriangleWall}
f_dict={"Gravity":Gravity}
pygame.display.set_caption("Omin: Level Editor")
canvas=pygame.Surface(screen.get_size())
canvas=canvas.convert()
canvas.fill([0,0,0])

musicpath = ''
bgcolor = [0,0,0]

#main.titlescreen(screen)

print "Music on"
sc=Scene("empty.txt")
run=1
def represent(spr, value, kind):
    print "Saving property "+str(value)
    if kind=="str":
        v="\""+str(value)+"\""
    elif kind=="Vector":
        v="Vector(%s, %s)" %(value.x, value.y)
    elif kind=="image":
        print spr.path
        v="\""+spr.path+"\""
    else:
        v=str(value)
    print "Result was "+v
    return v
def save(scene, f):
    fle=open(f, "w")
    g=pygame.sprite.Group()
    g.name=None
    for gro in [scene.rendered, scene.updated, scene.forces]:
        for spr in gro.sprites():
            spr.add(g)
    for spr in g.sprites():
        print "Saving sprite"
        p=spr.props.copy()
        for k in spr.props.keys():
            exec "p[k]=represent(spr, spr."+k+", p[k])"
        string=spr.__class__.__name__
        for k in p.keys():
            string+=" "+k+"="+p[k]
        string+="##"
        names=[]
        for gro in spr.groups():
            if gro.name==None:continue
            names.append(gro.name)
        string+=" ".join(names)
        string+="\n"
        fle.write(string)
    fle.close()
        
def tool_donothing(*args):pass
def make_tool_create(kind, img):
    def tool_create(x, y):
        global sc
        o=kind(image=img, x=x//24*24, y=y//24*24)
        sc.rendered.add(o)
        sc.updated.add(o)
        del o
    return tool_create
def tool_delete(x, y):
    for o in sc.updated.sprites():
        if o.rect.collidepoint([x, y]):o.kill()
def tool_player(x,y):
    xpos=x//24*24
    ypos=y//24*24
    img="res/sprites/testplayer.png"
    #TODO:Editable skills
    skills=defaultdict(fighting=2, agility=2, charisma=2, healing=2, fortitude=2)
    moves=[]
    hp=10
    o=Character(skills=skills, moves=moves, hp=hp, x=xpos, y=ypos, img=img)
    sc.rendered.add(o)
    sc.updated.add(o)
    del o
def tool_edit(x,y):
    for o in sc.updated.sprites():
        if o.rect.collidepoint([x, y]):
            attrs = []
            for a in o.defs.keys():
                attrs.append(a)
            attr = choicebox(screen,attrs,"Choose attribute")
            val = enterbox(screen,"Set to:")
            try:
                p=o.props[attr]
                if p=="int":
                    value=int(val)
                if p=="str":
                    value=val
                if p=="Vector":
                    x, y=val.split("..")
                    x=int(x)
                    y=int(y)
                    value=Vector(x, y)
                if p=="bool":
                    if val.lower()=="true":
                        value=True
                    else:
                        value=False
            except:
                msgbox(screen, "Couldn't do that. Sorry!")
            

            exec "o."+attr+"=value"
tool=tool_donothing
pygame.mixer.music.load("res/music/LevelEditorBGM.ogg")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
while run:
    canvas.fill(bgcolor)
    sc.draw(canvas)
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            run=0
        elif event.type==pygame.MOUSEBUTTONDOWN:
            tool(*pygame.mouse.get_pos())
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_l:
                path="level/"+enterbox(screen, "Enter level path to load:")+".txt"
                sc=Scene(path)
            elif event.key==pygame.K_c:
                kind=classes[choicebox(screen, classes.keys(), "Select a type of object:")]
                img="res/sprites/"+enterbox(screen, "Enter image path to load:")+".png"
                tool=make_tool_create(kind, img)
            elif event.key==pygame.K_SPACE:
                tool=tool_player
            elif event.key==pygame.K_x:
                tool=tool_delete
            elif event.key==pygame.K_f:
                msgbox(screen, "Force Manager")
                forces=sc.forces.sprites()
                a=choicebox(screen, ["Add", "Manage"], "Add new or manage old?")
                if a=="Add":
                    kind=f_dict[choicebox(screen, f_dict.keys(), "Select a type of force:")]
                    props=kind.defs
                    sc.forces.add(kind(**props))
            elif event.key==pygame.K_s:
                levelname="level/"+enterbox(screen, "Enter level path to save as:")+".txt"
                save(sc, levelname)
                        
            elif event.key==pygame.K_p:
                levelname="level/"+enterbox(screen, "Enter level path to save as:")+".txt"
                save(sc, levelname)
                run=1
                while run == 1:
                    canvas.fill([0,0,0])
                    events=pygame.event.get()
                    for event in events:
                        if event.type==pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:run=0

                    sc.update(events)
                    sc.draw(canvas)
                    screen.fill([0,0,0])
                    screen.blit(canvas, [0,0])
                    pygame.display.flip()
                print "Exited Level"
                run=1
                sc=Scene(levelname)

            elif event.key==pygame.K_m:
                musicpath = "res/music/"+enterbox(screen,"Set music path:")+".ogg"
                pygame.mixer.music.stop()
                pygame.mixer.music.load(musicpath)
                pygame.mixer.music.play(-1)
            elif event.key==pygame.K_b:
                r = int(enterbox(screen,"Background Red value"))
                g = int(enterbox(screen,"Background Green value"))
                b = int(enterbox(screen,"Background Blue value"))

                sc.rgb_bg = [r,g,b]

                sc=oldsc
            elif event.key == pygame.K_e:
                tool = tool_edit

                
    screen.fill(bgcolor)
    screen.blit(canvas, [0,0])
    pygame.display.flip()
pygame.quit()
