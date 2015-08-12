import pygame
from utils import *
from objects import *
from vector import Vector
from main import titlescreen, runlevel
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Omin: Level Editor")

screen=pygame.display.set_mode([640, 480])
#titlescreen(screen)
pygame.mixer.music.load("music/LevelEditorBGM.ogg")
pygame.mixer.music.play(-1)
canvas=pygame.Surface(screen.get_size())
canvas=canvas.convert()
canvas.fill([0,0,0])
objects=[]
selected=[]
run=1
def tool_quickedit(xo, yo, objects):
    nobjects=[]
    selected=[]
    for o in objects:
        print o
        r=pygame.image.load(o[1]["image"]).get_rect()
        if o[1]["x"]<=xo<=o[1]["x"]+r.width:
            if o[1]["y"]<=yo<=o[1]["y"]+r.height:
                selected.append(o)
                continue
        nobjects.append(o)
    for s in selected:
        inp=enterbox(screen, "Enter key=value")
        k, v=inp.split("=")
        s[1][k]=eval(v, globals(), locals())
        nobjects.append(s)
    return nobjects
def tool_select(xo, yo, objects):
    nobjects=[]
    for o in objects:
        r=pygame.image.load(o[1]["image"]).get_rect()
        if o[1]["x"]<=xo<=o[1]["x"]+r.width:
            if o[1]["y"]<=yo<=o[1]["y"]+r.height:
                selected.append(o)
                continue
        nobjects.append(o)
    for s in selected:
        nobjects.append(s)
    return nobjects
def tool_delete(xo, yo, objects):
    nobjects=[]
    for o in objects:
        r=pygame.image.load(o[1]["image"]).get_rect()
        if o[1]["x"]<=xo<=o[1]["x"]+r.width:
            if o[1]["y"]<=yo<=o[1]["y"]+r.height:
                continue
        nobjects.append(o)
    return nobjects
def make_tool_create(kind, image):
    def tool_create(xo, yo, objects):
        xd=xo//24.0*24
        yd=yo//24.0*24
        nobjects=objects
        d={}
        d.update(kind.defs)
        d["x"]=xd
        d["y"]=yd
        d["image"]=image
        print d
        nobjects.append([kind, d, ["rendered", "updated"]])
        return nobjects
    return tool_create
def save(objects):
    global levelname
    if levelname==None:levelname=enterbox(screen, "Enter level path to save as:")
    f=open(levelname, "w")
    for o in objects:
        d=""
        for k in o[1].keys():
            v=o[1][k]
            inst=v
            should=o[0].props[k]
            if should=="str":
                inst=repr(v)
            elif should=="int":
                inst=repr(v)
            elif should=="bool":
                inst=repr(v)
            elif should=="Vector":
                inst="Vector("+str(v.x)+","+str(v.y)+")"
            print str(k), str(v), str(inst)
            d=d+k+"="+inst+" "
        d=d[:-1]
        f.write(o[0].__name__+" "+d+"##"+" ".join(o[2])+"\n")
    f.close()
tool=tool_select
levelname = None
selected_border = pygame.image.load('selected.png')
while run == 1:
    canvas.fill([0,0,0])
    for o in objects:
        if "rendered" in o[2]:
            d=o[1]
            xp=d["x"]
            yp=d["y"]
            img=pygame.image.load(d["image"])
            canvas.blit(img, [xp, yp]) # Fixes image glitching on some displays

    for s in selected:
        canvas.blit(selected_border,[int(s[1]["x"]),int(s[1]["y"])])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            objects=tool(x, y, objects)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tool=tool_select
            elif event.key == pygame.K_c:
                classes={"Object":Object, "Wall":Wall, "CircleWall":CircleWall, "SquareWall":SquareWall, "RightTriangleWall":RightTriangleWall}
                s=classes[choicebox(screen, classes.keys(), "Select a type of object:")]
                i=enterbox(screen, "Enter image path:")
                tool=make_tool_create(s, i)
            elif event.key==pygame.K_s:save(objects)
            elif event.key==pygame.K_p:
                save(objects)
                runlevel(screen, levelname, True)
            elif event.key==pygame.K_x:
                tool=tool_delete
            elif event.key==pygame.K_f:
                forces=[]
                for o in objects:
                    if "forces" in o[2]:
                        forces.append(o)
                choices=[]
                for f in forces:
                    choices.append(f[0].__name__)
                choices.append("Create new")
                choice=choicebox(screen, choices, "Force Manager")
                if choice=="Create new":
                    kind={"Gravity":Gravity}
                    k=kind[choicebox(screen, kind.keys(), "Select a type of force:")]
                    #TODO:Change props
                    objects.append([k, k.defs, ["forces"]])
            elif event.key==pygame.K_l:
                levelname=enterbox(screen, "Enter level path to load:")
                f=open(levelname)
                lines=f.readlines()
                objects=[]
                for line in lines:
                    print line
                    if line.startswith("//"):continue
                    code, groups=line.split("##")
                    groups=groups.split(" ")
                    code=code.split(" ")
                    kind=eval(code[0], globals(), locals())
                    code=code[1:]
                    d=kind.defs
                    for item in code:
                        print item
                        try:
                            k, v = item.split("=")
                            try:d[k] = eval(v)
                            except:d[k] = v
                        except:pass
                    objects.append([kind, d, groups])
            elif event.key==pygame.K_q:
                tool=tool_quickedit
            elif event.key==pygame.K_RSHIFT:
                pass
    screen.fill([0,0,0])
    screen.blit(canvas, [0,0])



    pygame.display.flip()
