import pygame, main
from utils import *
from objects import *
from vector import Vector
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
classes={"Object":Object, "Wall":Wall, "CircleWall":CircleWall, "SquareWall":SquareWall, "RightTriangleWall":RightTriangleWall}
pygame.display.set_caption("Omin: Level Editor")
canvas=pygame.Surface(screen.get_size())
canvas=canvas.convert()
canvas.fill([0,0,0])
#main.titlescreen(screen)
pygame.mixer.music.load("music/LevelEditorBGM.ogg")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
sc=Scene("empty.txt")
run=1
def tool_donothing(*args):pass
def make_tool_create(kind, img):
    def tool_create(x, y):
        global sc
        o=kind(image=img, x=x//24*24, y=y//24*24)
        sc.rendered.add(o)
        sc.updated.add(o)
    return tool_create
def tool_delete(x, y):
    for o in sc.updated.sprites():
        if o.rect.collidepoint([x, y]):o.kill()
tool=tool_donothing
while run:
    canvas.fill([0,0,0])
    sc.draw(canvas)
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            run=0
        elif event.type==pygame.MOUSEBUTTONDOWN:
            tool(*pygame.mouse.get_pos())
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_l:
                path=enterbox(screen, "Enter level path to load:")
                sc=Scene(path)
            elif event.key==pygame.K_c:
                kind=classes[choicebox(screen, classes.keys(), "Select a type of object:")]
                img=enterbox(screen, "Enter image path to load:")
                tool=make_tool_create(kind, img)
            elif event.key==pygame.K_x:
                tool=tool_delete
            elif event.key==pygame.K_p:
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
                
    screen.fill([0,0,0])
    screen.blit(canvas, [0,0])
    pygame.display.flip()
    
