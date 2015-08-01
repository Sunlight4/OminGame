import Item,pygame

class Container:
    def __init__(self,items):
        self.items = items
class Chest:
    def __init__(self,image,x,y,items):
        self.image = pygame.image.load(image)
        
