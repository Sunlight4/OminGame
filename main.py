import pygame, utils, os, random
from utils import *
pygame.init()
pygame.mixer.init()
silliness=False
admin=0
class GameInstance:
    def __init__(self):
        self.level = 0
        self.hp = 0
        self.sp = 0
        self.inv = 0
        self.stealth = 0
        self.perception = 0

    def startGame(self,screen):
        s=titlescreen(screen)
        if s=="silly":return s
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
def titlescreen(screen,musicpath="res/music/TitleScreen.ogg"):
    run = 1
    # 1 for mainloop
    # 0 for quit
    # -1 for continue
    images=os.listdir("res/sprites/")
    if silliness:musicpath="res/music/sillymusic.ogg"
    pygame.mixer.init()
    pygame.mixer.music.load(musicpath)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    
    logo = pygame.image.load('logo.png')
    
    start = Button(text("Start",40,[128,32,2]),[320,320],True)
    new = Button(text("New",40,[128,32,2]),[320,360],True)
    load = Button(text("Continue",40,[128,32,2]),[320,400],True)
    developer = Button(text("Extras",40,[128,32,2]),[320,440],True)
    canvas=pygame.Surface(screen.get_size())
    canvas=canvas.convert()
    canvas.fill([0,0,0])
    imgs=[]
    print "Initializing Main Loop"
    while run == 1:
        
            
        canvas.fill([0,0,0])
        new.render(canvas)
        load.render(canvas)
        developer.render(canvas)
        
                
        blitcenter(logo,[320,128],canvas)
        if silliness:
            if random.random()<=0.5:
                imgs.append([random.randrange(640), 0, pygame.image.load("res/sprites/"+random.choice(images)), 0])
            nimgs=[]
            for img in imgs:
                x=img[0]
                y=img[1]
                image=img[2]
                speed=img[3]
                canvas.blit(image, [x, y])
                y+=speed
                speed+=1
                if y<=640:
                    nimgs.append([x, y, image, speed])
            imgs=nimgs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new.hover():
<<<<<<< HEAD
                    while 1:
                        usrname = utils.enterbox(screen,"Name:")
=======
                    usrname = utils.enterbox(screen,"Name:")

>>>>>>> origin/master
                    if usrname == 'OminAdmin108':
                        msgbox(screen,"You're an developer!?!", "Uh, yeah...")
                        pswd = passcodebox(screen,"Prove it.")

                        if pswd == "VSurvival":
                            msgbox(screen, "Access Granted")
                            admin=1
                        else:
                            msgbox(screen, "Go away.")
                            break

                    if os.path.isfile('users/'+usrname+'.txt'):
                        msgbox(screen, "Name is taken.")
                    else:
                        fl = open('users/'+usrname+'.txt','w+')
                        #Progress:Ch1()HP/SPD/XP/Skills/Moves/Items[]Next Character
                        fl.write("L1:LIONEL()8/1/0//Heal,WoodenSword,WoodenShield/")
                        fl.close()
<<<<<<< HEAD
                        if os.path.isfile('users/'+usrname+'.txt'):
                            msgbox(screen, "Name is taken.")
                            continue
                        cls = choicebox(screen,["Soldier:A powerful fighter","Scout:Specializes in exploration","Scholar:Well-learned character", "Sage:Magic specialist","Scoundrel:Rogue who lives by wits","Speaker:A diplomatic character"],"Choose a character type").split(":")[0]
                        if choicebox(screen,["Yes","Cancel"],cls+" named "+usrname+"?")=="Yes":break
                    #TODO:Save stuff
=======
>>>>>>> origin/master
                if load.hover():
                    namesfls = os.listdir('users/')
                    names = []

                    for i in namesfls:
                        if i.startswith('.'):
                            continue
                        names.append(i.strip('.txt'))

                    utils.choicebox(screen,names,"Choose a save file")
                if developer.hover():
                    #PASSCODE IS VSurvival
                    passcode = passcodebox(screen,"Password:")
                    if passcode=="VSurvival":
                        choice=choicebox(screen,["Silly Mode", "Level Editor","Crash Test"],"Developer Action?")
                        if choice=="Level Editor":
                            pygame.quit()
                            import editor
                        elif choice=="Silly Mode":
                            return "silly"
                        elif choice=="Crash Test":
                            raise Exception
                    else:
                        msgbox(screen,"Incorrect.")


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
        if developer.hover():
            developer = Button(text("Developers Only",45,[200,32,2]),[320,440],True)
        else:
            developer = Button(text("Developers Only",40,[128,32,2]),[320,440],True)
        
        pygame.display.flip()
    pygame.mixer.music.stop()

def main(screen):
    game = GameInstance()
    s=game.startGame(screen)
    if s=="silly":return s
if __name__=="__main__":
    screen=pygame.display.set_mode([640, 480])
    result=main(screen)
    print "Display On"
    if result=="silly":
        silliness=1
        main(screen)
    
        


