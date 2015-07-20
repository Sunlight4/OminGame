import pygame
from objects import *
from vector import Vector
class Scene(object):
    rendered=pygame.sprite.Group()
    updated=pygame.sprite.Group()
    forces=pygame.sprite.Group()
    def __init__(self, path):
        f=open(path).readlines()
        for line in f:
            if line.startswith("//"):continue
            code, groups=line.split("##")
            groups=groups.split(" ")
            code=code.split(" ")
            setup=code[0]
            code=code[1:]
            code=setup+"("+",".join(code)+")"
            o=eval(code, globals(), locals())
            
            for group in groups:
                try:exec "g = self."+group
                except:
                    g=pygame.sprite.Group()
                    exec "self."+group+" = g"
                try:g.add(o)
                except:g.append(o)
    def update(self, events):
        rendered=self.rendered
        updated=self.updated
        self.forces.update({"events":events, "rendered":rendered, "updated":updated})
        self.updated.update({"events":events, "rendered":rendered, "updated":updated})
    def draw(self, canvas):
        self.rendered.draw(canvas)
                
    
            
        