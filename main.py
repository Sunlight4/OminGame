import pygame, utils
from utils import *

pygame.mixer.init()

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
def titlescreen(screen,musicpath="music/TitleScreen.ogg"):
    run = 1
    # 1 for mainloop
    # 0 for quit
    # -1 for continue
<<<<<<< HEAD

    pygame.mixer.init()
    pygame.mixer.music.load("music/TitleScreen.ogg")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
=======
    pygame.mixer.music.load(musicpath)
    pygame.mixer.music.play(-1)

>>>>>>> origin/master
    logo = pygame.image.load('logo.png')

    start = Button(text("Start",40,[128,32,2]),[320,320],True)
    canvas=pygame.Surface(screen.get_size())
    canvas=canvas.convert()
    canvas.fill([0,0,0])
    while run == 1:
        canvas.fill([0,0,0])
        start.render(canvas)
        blitcenter(logo,[320,128],canvas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.hover():
                    run = -1


        screen.fill([0,0,0])
        screen.blit(canvas, [0,0])
        

        
        pygame.display.flip()
    pygame.mixer.music.stop()

    
