import pygame,math,objects
from vector import Vector
class Entity(objects.Object):
    energy=0
    props={"name":"str", "x":"int", "y":"int", "mass":"int", "image":"str", "hp":"int", "maxhp":"int", "moves":"[]Move", "ai":"AI", "speed":"int"}
    defs={"name":"Bob", "x":0, "y":0, "mass":50, "image":"Wall.png", "hp":1, "maxhp":1, "moves":[], "ai":None, "speed":1}
    def __init__(self,name="Bob",x=0,y=0,mass=50,image="Wall.png",hp=1,maxhp=1,moves=[],ai=None,speed=1):
        self.name=name
        self.hp=hp
        self.maxhp=maxhp
        self.moves=moves
        self.ai=ai
        self.speed=speed
        super(Entity, self).__init__(x, y, image, mass)
    def update(self, args):
        self.energy+=self.speed
        if self.ai!=None:self.ai.update(self, args)
        super(Entity, self).update(args)
class Move(object):
    name="None"
    kind="None"
    keys={pygame.K_SPACE:"space"}
    @staticmethod
    def run(o, args, key=None):
        pass
class M_Move(object):
    name="Move"
    kind="Move"
    keys={pygame.K_LEFT:"left", pygame.K_RIGHT:"right"}
    @staticmethod
    def run(o, args, key=None):
        if o.energy==0:return
        else:o.energy-=1
        if key=="left":
            o.forces.append(Vector(-2, 0))
        if key=="right":
            o.forces.append(Vector(2, 0))
class AIPlayer(object):
    def update(self, o, args):
        for event in args["events"]:
            if event.type==pygame.KEYDOWN:
                if event.key in M_Move.keys and M_Move in o.moves:
                    M_Move.run(self, args, key=M_Move.keys[event.key])
                else:
                    for m in o.moves:
                        if event.key in m.keys:
                            m.run(self, args, key=m.keys[event.key])
class Player(Entity):
    props={"name":"str", "x":"int", "y":"int", "mass":"int", "image":"str", "hp":"int", "maxhp":"int", "moves":"[]Move", "ai":"AI", "speed":"int"}
    defs={"name":"Bob", "x":0, "y":0, "mass":50, "image":"Wall.png", "hp":1, "maxhp":1, "moves":[], "ai":AIPlayer, "speed":1}
    def __init__(self, *args, **kw):
        super(Player, self).__init__(*args, **kw)
        if self.ai==None:self.ai==AIPlayer
        
        
        
