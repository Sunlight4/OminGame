import pygame, main
from utils import *
from objects import *
from vector import Vector
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640,480])


pygame.display.set_caption("Omin: Level Editor")

print "Omin Level Editor"

classes={"Object":Object, "Wall":Wall, "CircleWall":CircleWall, "SquareWall":SquareWall, "RightTriangleWall":RightTriangleWall,"AnimatedObject":AnimatedObject}
main.titlescreen(screen)
canvas=pygame.Surface(screen.get_size())
canvas=canvas.convert()
canvas.fill([0,0,0])
pygame.mixer.music.load("music/LevelEditorBGM.ogg")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
objects=[]
selected=Object
image="Wall.png"
run=1
selected_icn = pygame.image.load("lvleditor_res/selected.png")
levelname=None
saved = None
images=[None, None, None, None, None, None, None, None, None, None]
while run:
    canvas.fill([0,0,0])
    for o in objects:
        try:
            d=o[1]
            xp=d["x"]
            yp=d["y"]
            img=pygame.image.load(d["image"])
            canvas.blit(img, [xp, yp]) # Fixes image glitching on some displays
        except:pass
    canvas.blit(selected_icn,[24,24])
    try:
        canvas.blit(pygame.image.load(image),[28,28])
    except:
        pass
    
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            run=0
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                levelname=None
                x, y=pygame.mouse.get_pos()

                delete = False
                
                for o in objects:
                    obj = o[1]

                    if x-x%24 == obj['x']:
                        if y-y%24 == obj['y']:
                            objects.remove(o)
                            print "Deleted Object"
                            delete = True

                if not delete:
                    diction={}
                    diction.update(selected.defs)
                    diction["x"]=x//24*24
                    diction["y"]=y//24*24
                    diction["image"]=image
                    objects.append([selected, diction, ["rendered", "updated"]])
            elif event.button==3:
                x, y=pygame.mouse.get_pos()

                x -= x%24
                y -= y%24
                for o in objects:
                    obj = o[1]
                    keys = []

                    for key in obj:
                        keys.append(key)

                    if x == obj['x']:
                        if y == obj['y']:
                            attr = choicebox(screen,keys,'Set value of:')
                            val = enterbox(screen,"Set value to:")

                            try:
                                val = float(val)
                            except:
                                if val == 'True':
                                    val = True
                                elif val == 'False':
                                    val = False
                                else:
                                    val = str(val)
                            
                            obj[attr] = val
                            print [o[0],obj,keys]
                            objects[objects.index(o)] = [o[0],obj,keys]
                            

                            
                    

                    

                    
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                levelname=enterbox(screen, "Enter level path to save as:")
                print levelname
                saved=levelname
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
                        d=d+k+"="+inst+" "

                    f.write(o[0].__name__+" "+d+"##"+" ".join(o[2]))
                    f.write("\n")
                f.close()
            if event.key==pygame.K_p:
                if levelname==None:
                    levelname=enterbox(screen, "Enter level path to save as:")
                    saved=levelname
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
                            d=d+k+"="+inst+" "
                        f.write(o[0].__name__+" "+d+"##"+" ".join(o[2]))
                        f.write("\n")
                    f.close()
                main.runlevel(screen, levelname)
            if event.key==pygame.K_TAB:
                selected=classes[choicebox(screen, classes.keys(), "Select a type of object:")]
            if event.key==pygame.K_1:
                if images[1]==None:
                    images[1]=enterbox(screen, "Enter image path to load:")
                else:
                    image=images[1]
            if event.key==pygame.K_2:
                if images[2]==None:
                    images[2]=enterbox(screen, "Enter image path to load:")
                else:
                    image=images[2]
            if event.key==pygame.K_3:
                if images[3]==None:
                    images[3]=enterbox(screen, "Enter image path to load:")
                else:
                    image=images[3]
            if event.key==pygame.K_4:
                if images[4]==None:
                    images[4]=enterbox(screen, "Enter image path to load:")
                else:
                    image=images[4]
            if event.key==pygame.K_5:
                if images[5]==None:
                    images[5]=enterbox(screen, "Enter image path to load:")
                else:
                    image=images[5]
            if event.key==pygame.K_l:
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
            if event.key==pygame.K_g:
                objects.append([Gravity, {"strength":Vector(0, 1)}, ["forces"]])
            if event.key==pygame.K_f:
                if not saved == None:
                    main.runlevel(screen,saved)
                else:
                    msgbox(screen,"Please save level first")
                    levelname=enterbox(screen, "Enter level path to save as:")
                    saved=levelname
                    f=open(levelname, "w")
                    for o in objects:
                        d=''
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
                            d=d+k+"="+inst+" "
                        f.write(o[0].__name__+" "+d+"##"+" ".join(o[2]))
                        f.write("\n")
                    f.close()

    screen.fill([0,0,0])
    screen.blit(canvas, [0,0])
    pygame.display.flip()
