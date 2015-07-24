import pygame, main
from utils import *
from objects import *
from vector import Vector
pygame.init()

screen = pygame.display.set_mode([640,480])


pygame.display.set_caption("Omin: Level Editor")


main.titlescreen(screen)
canvas=pygame.Surface(screen.get_size())
canvas=canvas.convert()
canvas.fill([0,0,0])

objects=[]
selected=Object
image="Wall.png"
run=1
levelname=None
images=[None, None, None, None, None, None, None, None, None, None]
while run:
    canvas.fill([0,0,0])
    for o in objects:
        d=o[1]
        xp=d["x"]
        yp=d["y"]
        img=pygame.image.load(d["image"])
        canvas.blit(img, [xp, yp])
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            run=0
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                x, y=pygame.mouse.get_pos()
                diction={}
                diction.update(selected.defs)
                diction["x"]=x//24*24
                diction["y"]=y//24*24
                diction["image"]=image
                objects.append([selected, diction, ["rendered", "updated"]])
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                levelname=enterbox(screen, "Enter level path to save as:")
                f=open(levelname, "w")
                for o in objects:
                    d=""
                    for k in o[1].keys():
                        v=o[1][k]
                        d=d+k+"="+str(v)+" "
                    f.write(o[0].__name__+" "+d+"##"+" ".join(o[2]))
                    f.write("\n")
                f.close()
            if event.key==pygame.K_p:
                if levelname==None:
                    levelname=enterbox(screen, "Enter level path to save as:")
                    f=open(levelname, "w")
                    for o in objects:
                        d=""
                        for k in o[1].keys():
                            v=o[1][k]
                            d=d+k+"="+str(v)+" "
                        f.write(o[0].__name__+" "+d+"##"+" ".join(o[2]))
                        f.write("\n")
                    f.close()
                main.loadlevel(screen, levelname)
            if event.key==pygame.K_TAB:
                selected=classes[choicebox(classes.keys())]
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
            
    screen.fill([0,0,0])
    screen.blit(canvas, [0,0])
    pygame.display.flip()
    print objects
                
