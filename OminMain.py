import main,pygame,Item,utils,Inventory

pygame.init()

screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Omin")
Inventory.itemInfo(screen,Item.BrassSword)

main.main(screen)
