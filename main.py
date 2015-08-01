import pygame, utils
from utils import *

pygame.mixer.init()

class GameInstance:
    def __init__(self):
        self.level = 0
        self.hp = 0
        self.sp = 0
        self.inv = 0
        self.stealth = 0
        self.perception = 0

    def startGame(self,screen):
        titlescreen(screen)
        msgbox(screen,"Omin Origins","Start")
        runlevel(screen,'level/origins/level1.txt')

def runlevel(screen,path,game=GameInstance()):
    canvas=pygame.Surface(screen.get_size())
    canvas=canvas.convert()
    canvas.fill([0,0,0])
    sc=utils.Scene(path)
    run=1
    while run == 1:
        canvas.fill([0,0,0])
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                run=0
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if editor:
                        run = -2
                    else:
                        run = -1
        
        sc.update(events)
        sc.draw(canvas)
        screen.fill([0,0,0])
        screen.blit(canvas, [0,0])
        pygame.display.flip()
    print "Exited Level"
    if run == 0:
        pygame.quit()
        raise SystemExit
    if run == -2:
        return
    if run == -1:
        pass # Go to pause menu
def titlescreen(screen,musicpath="music/TitleScreen.ogg"):
    run = 1
    # 1 for mainloop
    # 0 for quit
    # -1 for continue


    pygame.mixer.init()
    pygame.mixer.music.load("music/TitleScreen.ogg")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    pygame.mixer.music.load(musicpath)
    pygame.mixer.music.play(-1)

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
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.hover():
                    run = -1


        screen.fill([0,0,0])
        screen.blit(canvas, [0,0])
        
        if start.hover():
            start = Button(text("Start",45,[200,32,2]),[320,320],True)
        else:
            start = Button(text("Start",40,[128,32,2]),[320,320],True)
        
        pygame.display.flip()
    pygame.mixer.music.stop()

def main(screen):
    game = GameInstance()
    game.startGame(screen)

        


