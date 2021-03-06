import pygame, math, os, random
from vector import Vector

class Atomic(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.left=x
        self.rect.top=y
        super(Atomic, self).__init__()
    def remove(self):
        self.kill()
    def moveto(self, x, y, camera):
        self.rect.left=x-(self.rect.width/2.0)-camera.x
        self.rect.top=y-(self.rect.height/2.0)-camera.y
    def limbo(self, limbo):
        self.status=self.groups()
        self.remove()
        limbo.add(self)
    def unlimbo(self):
        self.remove()
        for g in self.status:
            g.add(self)
class Object(Atomic): # Base class
    props={"x":"int", "y":"int", "image":"image", "mass":"int", "fixed":"bool"}
    defs={"x":0, "y":0, "image":"Wall.png", "mass":50, "fixed":False}
    grounded=None
    def __init__(self, x=0, y=0, image="Wall.png", mass=50, fixed=False, *args):
        "Create an object with specified x, y, image, and mass. Calculate rect and mask for later, and make pos and velocity vectors"
        super(Object, self).__init__(x, y, image, *args)
        self.forces=[]
        self.fixed=fixed
        self.velocity=Vector(0,0)
        self.pos=Vector(x+(self.rect.width/2.0), y+(self.rect.height/2.0))
        self.mass=mass
        self.path=image
    def update(self, args):
        camera=args["camera"]
        if (camera.x>self.pos.x) or (camera.x+640<self.pos.x) or (camera.y>self.pos.y) or (camera.y+480<self.pos.y):
            self.limbo(args["limbo"])
            return
            
        "Check our forces, and change velocity accordingly, then change our position"
        super(Object, self).update()
        self.grounded=None
        if not self.fixed:
            total_force=Vector(0,0)
            for f in self.forces:total_force+=f
            vel_change=total_force/float(self.mass)
            self.velocity+=vel_change
            self.pos+=self.velocity
        self.forces=[]
        self.moveto(self.pos.x, self.pos.y, args["camera"])
    def addforce(self, v):
        self.forces.append(v)
    def _x(self):return self.pos.x
    def draw(self, canvas, camera):
        x=self.pos.x-camera.x
        y=self.pos.y-camera.y
        canvas.blit(self.image, [x, y])
    def _y(self):return self.pos.y
    def limbo_check(self, args):
        camera=args["camera"]
        if (camera.x<self.pos.x) and (camera.x+640>self.pos.x) and (camera.y<self.pos.y) and (camera.y+480>self.pos.y):
            self.remove()
            self.unlimbo()
            return
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
        
        self.rect.top=self.pos.y-(self.rect.height/2.0)-args["camera"].y
    def getImage(self):
        return pygame.image.load(self.frames[self.frame])
    
    
class Wall(Object):
    props={"bouncy":"int", "x":"int", "y":"int", "image":"image", "mass":"int", "fixed":"bool", "friction":"int"}
    defs={"x":0, "y":0, "image":"Wall.png", "mass":0, "fixed":True, "bouncy":1, "friction":0.5}
    def __init__(self, bouncy=1, friction=0.5, **kw):
        "Create a wall with specified bounciness, rotated by the given amount of degrees"
        self.bouncy=bouncy
        self.friction=friction
        super(Wall, self).__init__(**kw)
    def update(self, args):
        "Handle wall-object collisions: use our normal function, then move the object out of us, then do bounciness pushback"
        #TODO:Bounciness
        for spr in pygame.sprite.spritecollide(self, args["updated"], False):
            if isinstance(spr, Wall):continue
            
            spr.addforce((-spr.velocity)*self.friction)
            #get normal force
            angle=math.degrees((spr.pos-self.pos).direction)
            normal=self.normal((angle) % 360)
            a=(-normal).angle(spr.velocity)
            mN = math.cos(a) * spr.velocity.magnitude * self.bouncy * spr.mass
            spr.addforce(normal*mN)
            
            opos=spr.pos
            
            #enforce non-penetration constant
            while pygame.sprite.collide_rect(self, spr):
                spr.pos+=normal
                
                
                spr.moveto(spr.pos.x, spr.pos.y, args["camera"])
            
            spr.grounded=self
            #TODO:fix this
        super(Object, self).update(args)

    def normal(self, angle):
        "Default normal function: simply return up vector"
        return Vector(0, -1)

class CircleWall(Wall):
    "Special class for circle walls. Simply changes the normal function to pushback based on the exact angle"
    def normal(self, angle):
        a=math.radians(angle) 
        
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
        a=(angle+90)%360
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
        
        
