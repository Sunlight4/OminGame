import pygame, math, random

class Item:
    def __init__(self,name,image,reuseable,value):
        self.image=pygame.image.load(image)
        self.path = image
        self.name = name
        self.x=0
        self.y=0
        self.reusable = reuseable
        self.value = value
        self.rect = [self.x,self.y,self.image.get_size()[0],self.image.get_size()[1]]
    def onUse(self):
        pass
    def onThrow(self):
        pass

class Weapon(Item):
    def __init__(self,name,image,value,damage,maxdamage,speed):
        super(Weapon,self).__init__('Weapon',image,True,value)
        self.damage=damage
        self.maxdamage=maxdamage
        self.speed = speed # Cooldown in frames
        self.cooldown = 0
    def onUpdate(self):
        self.cooldown -= 1
    def onUse(self,targetEntity):
        if self.cooldown > 0:
            return
        self.cooldown = speed
        targetEntity.hp-=random.range(damage,maxdamage)

        if targetEntity.hp <= 0:
            targetEntity.onDie()
    def onThrow(self):
        pass

class BasicSword(Weapon):
    def __init__(self):
        super(Weapon,self).__init__('BasicSword',image,True,value,5,15,12)
        
        
