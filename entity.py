import collections
import objects,utils
class Entity(objects.Object):
    skills=collections.defaultdict(int)
    hp=0
    moves=[]
    def __init__(self, x, y, who=""):
        f=file("entities/"+who+".txt", "r")
        setup=f.read().split(',')
        for command in setup:
            key=command.split(':')
            if key[0]=="HP":
                self.hp=int(key[1])
            if key[0]=="IMG":
                image="res/sprites/"+key[1]+".png"
        super(Entity, self).__init__(x=x, y=y, image=image)
        