import Item,pygame,utils
from utils import *

class Inventory:
    def __init__(self,items):
        self.items = items

def itemInfo(screen,item):
    run = 1

    print item.itemattrs
    img = pygame.image.load(item.path)
    canvas=pygame.Surface(screen.get_size())
    canvas=canvas.convert()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = 0
                elif event.key == pygame.K_ESCAPE:
                    run = 0

        canvas.fill([0,0,0])

        utils.blitcenter(text(item.name,50,[255,255,255]),[320,128],canvas)
        
        utils.blitcenter(img,[320,240],canvas)

        y = 280

        for attr in item.itemattrs:
            if attr == 'image' or attr == 'path' or attr == 'name':
                continue
            canvas.blit(text(attr+': '+str(getattr(item,attr)),25,[255,0,0]),[120,y])
            y+=32
        screen.blit(canvas,[0,0])
        pygame.display.flip()


        
        
