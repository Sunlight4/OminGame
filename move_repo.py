from vector import Vector
class Move(object):
    @staticmethod
    def run(e):pass

#Begin basic moves
class Walk(Move):
    @staticmethod
    def run(e, args, target):
        movement=Vector(target.x-e.x, 0)
        if not e.grounded:return
        else:
            if e.energy>=1:
                e.energy-=1
                e.forces.append(movement.truncate(100/e.mass))
            else:
                pass
move_dict={"walk":Walk}
