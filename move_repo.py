from vector import Vector
import math
class Move(object):
    @staticmethod
    def run(e):pass

#Begin basic moves
class Jump(Move):
    @staticmethod
    def run(e):
        if e.grounded==None:return
        if e.energy<1:return
        else:e.energy-=1
        angle=math.degrees((e.pos-e.grounded.pos).direction)
        normal=e.grounded.normal((angle) % 360)
        a=(-normal).angle(e.velocity)
        mN = math.cos(a) * e.velocity.magnitude * e.grounded.bouncy * 10 * 50
        e.addforce(normal*mN)
class Walk(Move):
    @staticmethod
    def run(e, target):
        if e.grounded==None:return
        if e.energy<1:return
        else:e.energy-=1
        angle=math.degrees((e.pos-e.grounded.pos).direction)
        normal=e.grounded.normal((angle) % 360)
        if target.x<e.x:
            v=Vector(normal.y, -normal.x)*100
        else:
            v=Vector(-normal.y, normal.x)*100
        e.addforce(v)
move_dict={"basic/jump":Jump, "basic/walk":Walk}
