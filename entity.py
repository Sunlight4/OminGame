import collections
import objects,utils
class Character(objects.Object):
    skills=collections.defaultdict(int)
    moves=[]
    hp=0
    props={"skills":"[]Skill","moves":"[]Move","hp":"int","x":"int", "y":"int", "image":"image", "mass":"int", "fixed":"bool"}
    defs={"skills":collections.defaultdict(int),"moves":[], "hp":0, "x":0, "y":0, "image":"Wall.png", "mass":50, "fixed":False}
    def __init__(self, skills, moves, hp, *args, **kw):
        self.skills=skills
        self.moves=moves
        self.hp=hp
        super(Character, self).__init__(*args, **kw)