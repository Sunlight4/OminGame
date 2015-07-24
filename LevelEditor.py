import pygame, main, easygui
from utils import *
from objects import *
from vector import Vector
pygame.init()

screen = pygame.display.set_mode([640,480])

enterbox(screen,"hi")

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
                levelname=enterbox(screen,"Enter level path to save as:")
                f=open(levelname, "w+")
                for o in objects:
                    d=""
                    for k in o[1].keys():
                        v=o[1][k]
                        d=d+k+"="+str(v)+" "
                    f.write(o[0].__name__+" "+d+"##"+" ".join(o[2]))
                    f.write("\n")
            if event.key==pygame.K_p:
                if levelname==None:
                    levelname=easygui.enterbox("Enter level path to save as:")
                    f=open(levelname, "w")
                    for o in objects:
                        d=""
                        for k in o[1].keys():
                            v=o[1][k]
                            d=d+k+"="+str(v)+" "
                        f.write(o[0].__name__+" "+d+"##"+" ".join(o[2]))
                        f.write("\n")
                main.loadlevel(screen, levelname)
    screen.fill([0,0,0])
    screen.blit(canvas, [0,0])
    pygame.display.flip()
    print objects
                
