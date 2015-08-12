import pygame,math

class Entity:
    def __init__(self,name,x,y,image,hp,maxhp,equip):
        self.image = pygame.image.load(image)
        self.name = name
        self.path = image
        self.hp = hp
        self.maxl
        self.x = x
        self.y = y
        self.dead = False
        self.life = life
        self.equip = equip
    def onUpdate(self,screen):
        screen.blit(self.image,[self.x,self.y])
    def onDie(self):
        self.dead = True
        
