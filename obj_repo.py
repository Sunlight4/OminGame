from objects import Object, Wall
import pygame
class RightPushForce(pygame.sprite.Sprite):
    props={}
    defs={}
    def __init__(self):
        super(RightPushForce, self).__init__()
    def update(self, args):
        for spr in args["updated"].sprites():
            if not spr.fixed:
                spr.velocity.x=2
class Spike(Object):
    def update(self, args):
        for spr in pygame.sprite.spritecollide(self, args["updated"], False):
            try:
                spr.hp-=1
            except:pass
repo={"test/pushforce":[RightPushForce, True], "general/spike":[Spike,False]}
