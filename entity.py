import collections,pygame,vector
import objects,utils,move_repo
class AI(object):
    def update_obj(self,e, args):
        pass
class DoNothingAI(object):
    def update_obj(self, e, args):
        pass
class GeoJumperAI(object):
    def update_obj(self, e, args):
        for event in args["events"]:
            if event.type==pygame.MOUSEBUTTONDOWN:
                move_repo.Jump.run(e)
ai_dict={"basic/nothing":DoNothingAI, "test/geojumper":GeoJumperAI}
class Entity(objects.Object):
    skills=collections.defaultdict(int)
    hp=0
    moves=[]
    energy=0
    ai=DoNothingAI
    def __init__(self, x, y, who=""):
        f=file("entities/"+who+".txt", "r")
        setup=f.read().split(',')
        for command in setup:
            key=command.split(':')
            if key[0]=="HP":
                self.hp=int(key[1])
            if key[0]=="IMG":
                image="res/sprites/"+key[1]+".png"
            if key[0]=="AI":
                self.ai=ai_dict[key[1]]()
            if key[0]=="MOVE":
                self.moves.append(move_repo.move_dict[key[1]])
        super(Entity, self).__init__(x=x, y=y, image=image)
    def update(self, args):
        self.energy+=1
        if self.hp==0:self.kill()
        self.ai.update_obj(self, args)
        super(Entity, self).update(args)
