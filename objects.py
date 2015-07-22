import pygame, math
from vector import Vector
class Object(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, image=None, mass=0, fixed=None, *args):
        "Create an object with specified x, y, image, and mass. Calculate rect and mask for later, and make pos and velocity vectors"
        super(Object, self).__init__(*args)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.left=x
        self.rect.top=y
        self.forces=[]
        self.fixed=fixed
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity=Vector(0,0)
        self.pos=Vector(x+(self.rect.width/2.0), y+(self.rect.height/2.0))
        self.mass=mass
    def update(self, args):
        "Check our forces, and change velocity accordingly, then change our position"
        super(Object, self).update()
        if self.fixed==None:
            total_force=Vector(0,0)
            for f in self.forces:total_force+=f
            vel_change=total_force/float(self.mass)
            self.velocity+=vel_change
            self.pos+=self.velocity
        self.forces=[]
        self.rect.left=self.pos.x-(self.rect.width/2.0)
        self.rect.top=self.pos.y-(self.rect.height/2.0)
    def addForce(self, v):
        self.forces.append(v)
class Wall(Object):
    def __init__(self, bouncy=1, rotation=0, **kw):
        "Create a wall with specified bounciness, rotated by the given amount of degrees"
        super(Wall, self).__init__(**kw)
        self.bouncy=bouncy
        self.rotation=rotation
    def update(self, args):
        "Handle wall-object collisions: use our normal function, then move the object out of us, then do bounciness pushback"
        #TODO:Bounciness
        for spr in pygame.sprite.spritecollide(self, args["updated"], False):
            if isinstance(spr, Wall):continue
            print type(spr)
            #get normal force
            angle=math.degrees((spr.pos-self.pos).direction)
            normal=self.normal((angle-self.rotation) % 360)
            angle=math.degrees((spr.pos-self.pos).direction)
            normal=self.normal((angle-self.rotation) % 360)
            a=(-normal).angle(spr.velocity)
            mN = math.cos(a) * spr.velocity.magnitude * self.bouncy * spr.mass
            spr.addForce(normal*mN)
            print mN
            #move the object so it isn't penetrating me
            while pygame.sprite.collide_mask(self, spr):
                spr.pos+=normal
                spr.rect.left=spr.pos.x-(spr.rect.width/2.0)
                spr.rect.top=spr.pos.y-(spr.rect.height/2.0)
            spr.pos+=(normal/2.0)
            spr.rect.left=spr.pos.x-(spr.rect.width/2.0)
            spr.rect.top=spr.pos.y-(spr.rect.height/2.0)
            #TODO:fix this
            
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
        if a<135:a=45
        if 135<=a<=225:
            a=180
        if 225<=a<=315:
            a=270
        else:
            a=45
        return super(RightTriangleWall, self).normal(a)
class Gravity(pygame.sprite.Sprite):
    def __init__(self, strength=None):
        super(Gravity, self).__init__()
        self.strength=strength
    def update(self, args):
        for spr in args["updated"].sprites():
            spr.addForce(self.strength*spr.mass)
            
        
        
        
        
        