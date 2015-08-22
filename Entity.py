import pygame,math,objects
class Entity(objects.Object):
    props={"name":"str", "x":"int", "y":"int", "mass":"int", "image":"str", "hp":"int", "maxhp":"int", "moves":"[]Move", "ai":"Ai"}
    defs={"name":"Bob", "x":0, "y":0, "mass":50, "image":"Wall.png", "hp":1, "maxhp":1, "moves":[], "ai":None}
    def __init__(self,name="Bob",x=0,y=0,mass=50,image="Wall.png",hp=1,maxhp=1,moves=[],ai=None):
        self.name=name
        self.hp=hp
        self.maxhp=maxhp
        self.moves=moves
        self.ai=ai
        super(Entity, self).__init__(x, y, image, mass)
    
        
