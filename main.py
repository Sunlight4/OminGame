import pygame, utils
from utils import *

def runlevel(screen, path):
    canvas=pygame.Surface(screen.get_size())
    canvas=canvas.convert()
    canvas.fill([0,0,0])
    sc=utils.Scene(path)
    run=1
    while run:
        canvas.fill([0,0,0])
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                run=0
        
        sc.update(events)
        sc.draw(canvas)
        screen.fill([0,0,0])
        screen.blit(canvas, [0,0])
        pygame.display.flip()
    print "Exited Level"
def titlescreen(screen,path):
    run = 1
    # 1 for mainloop
    # 0 for quit
    # -1 for continue


    logo = pygame.image.load('logo.png')

    start = Button(text("Start",40,[128,32,2]),[320,320],True)
    
    while run == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.hover():
                    run = -1

        screen.fill([0,0,0])
        blitcenter(logo,[320,128],screen)

        start.render(screen)

        pygame.display.flip()

    if run == 0:
        pygame.quit()
    elif run == -1:
        runlevel(screen,path)
pygame.init()
path="testlevel/map.txt"
screen=pygame.display.set_mode([640, 480])
pygame.display.set_caption("Omin")
titlescreen(screen,path)
