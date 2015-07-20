import pygame
from vector import Vector
class Object(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, image=None, mass=0, *args):
        super(Object, self).__init__(*args)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.left=x
        self.rect.top=y
        self.forces=[]
        self.velocity=Vector(0,0)
        self.pos=Vector(x+(self.rect.width/2.0), y+(self.rect.height/2.0))
        self.mass=mass
    def update(self, args):
        super(Object, self).update()
        total_force=Vector(0,0)
        for f in self.forces:total_force+=f
        vel_change=total_force/float(self.mass)
        self.velocity+=vel_change
        self.pos+=self.velocity
        self.forces=[]
        self.rect.left=self.pos.x-(self.rect.width/2.0)
        self.rect.top=self.pos.y-(self.rect.height/2.0)
        
        