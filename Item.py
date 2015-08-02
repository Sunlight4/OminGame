import pygame, math, random

class Item(object):
    def __init__(self,itemname,image,reuseable,value):
        self.image=pygame.image.load(image)
        self.itemattrs = ['name','image','reuseable','value']
        self.path = image
        self.name = itemname
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
    def __init__(self,itemname,image,value,damage,maxdamage,speed):
        super(Weapon,self).__init__('Weapon',image,True,value)
        self.itemattrs = ['name','image','damage','maxdamage','value','speed']
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
        pass # TODO: Add throwing weapons

class BrassSword(Weapon):
    def __init__(self):
        super(BrassSword,self).__init__('item.weapon.brass_sword','testlevel/Ball.png',15,3,10,12)
        
        
