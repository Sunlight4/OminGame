import pygame
from objects import *
from vector import Vector
class Scene(object):
    rendered=pygame.sprite.Group()
    updated=pygame.sprite.Group()
    def __init__(self, path):
        f=open(path).read_lines()
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
                g=self.__dict__[group]
                try:g.add(o)
                except:g.append(o)
    
            
        