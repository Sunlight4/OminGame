import Item,pygame,utils

class Container:
    def __init__(self,items):
        self.items = items
class Chest:
    def __init__(self,image,x,y,items):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        
    def render(self,screen):
        screen.blit(self.image,[self.x,self.y])

    def itemgui(self,screen):
        pass
