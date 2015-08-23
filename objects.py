import pygame, math, os
from vector import Vector

class Object(pygame.sprite.Sprite): # Base class
    props={"x":"int", "y":"int", "image":"image", "mass":"int", "fixed":"bool"}
    defs={"x":0, "y":0, "image":"Wall.png", "mass":50, "fixed":False}
    def __init__(self, x=0, y=0, image="Wall.png", mass=50, fixed=False, *args):
        "Create an object with specified x, y, image, and mass. Calculate rect and mask for later, and make pos and velocity vectors"
        super(Object, self).__init__(*args)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.left=x
        self.rect.top=y
        self.forces=[]
        self.fixed=fixed
        self.velocity=Vector(0,0)
        self.pos=Vector(x+(self.rect.width/2.0), y+(self.rect.height/2.0))
        self.mass=mass
        self.path=image
    def update(self, args):
        "Check our forces, and change velocity accordingly, then change our position"
        super(Object, self).update()
        if not self.fixed:
            total_force=Vector(0,0)
            for f in self.forces:total_force+=f
            vel_change=total_force/float(self.mass)
            self.velocity+=vel_change
            self.pos+=self.velocity
        self.forces=[]
        self.rect.left=self.pos.x-(self.rect.width/2.0)
        self.rect.top=self.pos.y-(self.rect.height/2.0)
    def addforce(self, v):
        self.forces.append(v)
    def _x(self):return self.pos.x
    def _y(self):return self.pos.y
    x=property(_x)
    y=property(_y)
class AnimatedObject(Object): # Animated object!
    props={"x":"int", "y":"int", "image":"image", "mass":"int", "fixed":"bool", "animation":"str","speed":"int"}
    defs={"x":0, "y":0, "image":"Wall.png", "mass":50, "fixed":False, "animation":"test.anim","speed":1}
    def __init__(self,anim='test.anim',**kw):
        super(Object, self).__init__(**kw)
        self.frame=0
        defs["animation"] = anim
        self.animpath = defs["animation"]
        self.frames = []
        self.anim = open(anim,'r')
        self.speed = 1

        for line in self.anim.readlines():
            line = line.strip()
            if not line.startswith('#'):
                if line.startswith('~'):
                    line = line.strip('~')

                    if line.startswith('speed'):
                        self.speed = int(line.split('=')[1])
                        defs["speed"] = int(line.split('=')[1])
                else:
                    frames.append(line)
                    
    def update(self, args):
        "Check our forces, and change velocity accordingly, then change our position"
        super(Object, self).update()
        self.frame += 1
        if self.frame == len(self.frames)-1:
            self.frame = 0
        if not self.fixed:
            total_force=Vector(0,0)
            for f in self.forces:total_force+=f
            vel_change=total_force/float(self.mass)
            self.velocity+=vel_change
            self.pos+=self.velocity
        self.forces=[]
        self.rect.left=self.pos.x-(self.rect.width/2.0)
        self.rect.top=self.pos.y-(self.rect.height/2.0)
    def getImage(self):
        return pygame.image.load(self.frames[self.frame])
    
    
class Wall(Object):
    props={"bouncy":"int", "x":"int", "y":"int", "image":"image", "mass":"int", "fixed":"bool"}
    defs={"x":0, "y":0, "image":"Wall.png", "mass":0, "fixed":True, "bouncy":1}
    def __init__(self, bouncy=1, **kw):
        "Create a wall with specified bounciness, rotated by the given amount of degrees"
        self.bouncy=bouncy
        super(Wall, self).__init__(**kw)
    def update(self, args):
        "Handle wall-object collisions: use our normal function, then move the object out of us, then do bounciness pushback"
        #TODO:Bounciness
        for spr in pygame.sprite.spritecollide(self, args["updated"], False):
            if isinstance(spr, Wall):continue
            print type(spr)
            #get normal force
            angle=math.degrees((spr.pos-self.pos).direction)
            normal=self.normal((angle) % 360)
            a=(-normal).angle(spr.velocity)
            mN = math.cos(a) * spr.velocity.magnitude * self.bouncy * spr.mass
            spr.addforce(normal*mN)
            print mN
            opos=spr.pos
            #move the object so it isn't penetrating me
            while pygame.sprite.collide_mask(self, spr):
                spr.pos+=normal
                spr.rect.left=spr.pos.x-(spr.rect.width/2.0)
                spr.rect.top=spr.pos.y-(spr.rect.height/2.0)
            spr.pos+=(normal/2.0)
            spr.rect.left=spr.pos.x-(spr.rect.width/2.0)
            spr.rect.top=spr.pos.y-(spr.rect.height/2.0)
            diff=spr.pos-opos
            spr.pos=opos
            spr.rect.left=spr.pos.x-(spr.rect.width/2.0)
            spr.rect.top=spr.pos.y-(spr.rect.height/2.0)
            spr.addforce(diff*spr.mass)
            #TODO:fix this
            
    def normal(self, angle):
        "Default normal function: simply return up vector"
        return Vector(0, -1)
class CircleWall(Wall):
    "Special class for circle walls. Simply changes the normal function to pushback based on the exact angle"
    def normal(self, angle):
        a=math.radians(angle) 
        print Vector(math.cos(a), math.sin(a))
        return Vector(math.cos(a), math.sin(a))
class SquareWall(CircleWall):
    "Special class for square walls. Rounds angle, then passes it to the circle normal function."
    def normal(self, angle):
        a=angle
        if a<45:
            a=0
        elif 45<=a<=135:
            a=90
        elif 135<=a<=225:
            a=180
        elif 225<=a<=315:
            a=270
        else:
            a=0
        return super(SquareWall, self).normal(a)
class RightTriangleWall(CircleWall):
    def normal(self, angle):
        a=angle
        if a<135:a=45
        if 135<=a<=225:
            a=180
        if 225<=a<=315:
            a=270
        else:
            a=45
        return super(RightTriangleWall, self).normal(a)
class Gravity(pygame.sprite.Sprite):
    props={"strength":"Vector"}
    defs={"strength":Vector(0, 1)}
    def __init__(self, strength=None):
        super(Gravity, self).__init__()
        self.strength=strength
    def update(self, args):
        for spr in args["updated"].sprites():
            spr.addforce(self.strength*spr.mass)
    
            
        
        
        
        
        
