from entity import AI, MoveGoal, Entity, PlayerAI

class Player(Entity):
    def __init__(self, x, y, who="", savefile=""):
        who='users/'+savefile+'/characters/'+who
        self.ai=PlayerAI()

