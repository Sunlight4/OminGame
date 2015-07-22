import pygame, utils

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
path="testlevel/map.txt"
screen=pygame.display.set_mode([640, 480])
runlevel(screen, path)
