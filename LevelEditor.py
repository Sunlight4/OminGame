import pygame, main
from utils import *
from objects import *
pygame.init()

screen = pygame.display.set_mode([640,480])

pygame.display.set_caption("Omin: Level Editor")

main.titlescreen(screen)


objects=[]
selected=None
