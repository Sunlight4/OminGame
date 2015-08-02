import pygame, utils, os
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
    new = Button(text("New",40,[128,32,2]),[320,360],True)
    load = Button(text("Continue",40,[128,32,2]),[320,400],True)
    canvas=pygame.Surface(screen.get_size())
    canvas=canvas.convert()
    canvas.fill([0,0,0])
    while run == 1:
        canvas.fill([0,0,0])
        new.render(canvas)
        load.render(canvas)
        blitcenter(logo,[320,128],canvas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new.hover():
                    usrname = utils.enterbox(screen,"Name:")

                    if os.path.isfile('users/'+usrname+'.txt'):
                        msgbox("Name is taken.")
                    else:
                        fl = open('users/'+usrname+'.txt','w+')

                        fl.write('''level=level/origins/level1.txt
hp=0
sp=0
inv=[]
stealth=0
perception=0
''')
                        # Indentation much?

                        fl.close()
                if load.hover():
                    namesfls = os.listdir('users/')
                    names = []

                    for i in namesfls:
                        if i.startswith('.'):
                            continue
                        names.append(i.strip('.txt'))

                    utils.choicebox(screen,names,"Choose a save file")
                    


        screen.fill([0,0,0])
        screen.blit(canvas, [0,0])
        
        if new.hover():
            new = Button(text("New Game",45,[200,32,2]),[320,360],True)
        else:
            new = Button(text("New Game",40,[128,32,2]),[320,360],True)
        if load.hover():
            load = Button(text("Continue",45,[200,32,2]),[320,400],True)
        else:
            load = Button(text("Continue",40,[128,32,2]),[320,400],True)
        
        pygame.display.flip()
    pygame.mixer.music.stop()

def main(screen):
    game = GameInstance()
    game.startGame(screen)

        


