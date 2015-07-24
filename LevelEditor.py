import pygame
from utils import *

pygame.init()

screen = pygame.display.set_mode([640,480])

pygame.display.set_caption("Omin: Level Editor")

def titlescreen():
    run = 1
    # 1 for mainloop
    # 0 for quit
    # -1 for create new level
    # -2 for edit existing level

    logo = pygame.image.load('logo.png')

    start1 = Button(text("Create new",40,[128,32,2]),[320,320],True)
    start2 = Button(text("Edit existing",40,[128,32,2]),[320,360],True)
    
    
    while run == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start1.hover():
                    run = -1
                if start2.hover():
                    run = -2
                

        screen.fill([0,0,0])
        blitcenter(logo,[320,128],screen)

        start1.render(screen)
        start2.render(screen)

        pygame.display.flip()

    if run == 0:
        pygame.quit()

titlescreen()

