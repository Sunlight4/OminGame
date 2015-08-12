import pygame, main
from utils import *
from objects import *
from vector import Vector
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
classes={"Object":Object, "Wall":Wall, "CircleWall":CircleWall, "SquareWall":SquareWall, "RightTriangleWall":RightTriangleWall}
f_dict={"Gravity":Gravity}
pygame.display.set_caption("Omin: Level Editor")
canvas=pygame.Surface(screen.get_size())
canvas=canvas.convert()
canvas.fill([0,0,0])

musicpath = ''
bgcolor = [0,0,0]

#main.titlescreen(screen)
pygame.mixer.music.load("music/LevelEditorBGM.ogg")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
print "Music on"
sc=Scene("empty.txt")
run=1
def tool_donothing(*args):pass
def make_tool_create(kind, img):
    def tool_create(x, y):
        global sc
        o=kind(image=img, x=x//24*24, y=y//24*24)
        sc.rendered.add(o)
        sc.updated.add(o)
    return tool_create
def tool_delete(x, y):
    for o in sc.updated.sprites():
        if o.rect.collidepoint([x, y]):o.kill()
def tool_edit(x,y):
    for o in sc.updated.sprites():
        if o.rect.collidepoint([x, y]):
            attrs = []
            for a in o.defs:
                attrs.append(a)
            attr = choicebox(screen,attrs,"Choose attribute")
            val = enterbox(screen,"Set to:")

            if type(val) == int:
                val = int(val)
            elif val.lower() == 'false' or val.lower() == 'true':
                if val.lower() == 'true':
                    val = True
                else:
                    val = Falses

            o.defs[attr] = val
tool=tool_donothing
while run:
    canvas.fill(bgcolor)
    sc.draw(canvas)
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            run=0
        elif event.type==pygame.MOUSEBUTTONDOWN:
            tool(*pygame.mouse.get_pos())
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_l:
                path=enterbox(screen, "Enter level path to load:")
                sc=Scene(path)
            elif event.key==pygame.K_c:
                kind=classes[choicebox(screen, classes.keys(), "Select a type of object:")]
                img=enterbox(screen, "Enter image path to load:")
                tool=make_tool_create(kind, img)
            elif event.key==pygame.K_x:
                tool=tool_delete
            elif event.key==pygame.K_f:
                msgbox(screen, "Force Manager")
                forces=sc.forces.sprites()
                a=choicebox(screen, ["Add", "Manage"], "Add new or manage old?")
                if a=="Add":
                    kind=f_dict[choicebox(screen, f_dict.keys(), "Select a type of force:")]
                    props=kind.defs
                    for prop in props.keys():
                        change=choicebox(screen, ["Change", "OK"], prop+" is "+str(props[prop])+". OK or change?")=="Change"
                        if change:
                            new = eval(enterbox(screen, "Enter new value:"), globals(), locals())
                            props[prop] = new
                    sc.forces.add(kind(**props))
            elif event.key==pygame.K_s:
                levelname=enterbox(screen, "Enter level path to save as:")
                f=open(levelname, "w")
                full=pygame.sprite.Group()
                for g in [sc.rendered, sc.updated, sc.forces]:
                    for o in g.sprites():
                        full.add(o)
                for s in full.sprites():
                    s.save(f)
                f.close()
                        
            elif event.key==pygame.K_p:
                oldsc=sc
                run=1
                while run == 1:
                    canvas.fill([0,0,0])
                    events=pygame.event.get()
                    for event in events:
                        if event.type==pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:run=0

                    sc.update(events)
                    sc.draw(canvas)
                    screen.fill([0,0,0])
                    screen.blit(canvas, [0,0])
                    pygame.display.flip()
                print "Exited Level"
                run=1

            elif event.key==pygame.K_m:
                musicpath = enterbox(screen,"Set music path:")
                pygame.mixer.music.stop()
                pygame.mixer.music.load(musicpath)
                pygame.mixer.music.play(-1)
            elif event.key==pygame.K_b:
                r = int(enterbox(screen,"Background Red value"))
                g = int(enterbox(screen,"Background Green value"))
                b = int(enterbox(screen,"Background Blue value"))

                sc.rgb_bg = [r,g,b]

                sc=oldsc
            elif event.key == pygame.K_e:
                tool = tool_edit

                
    screen.fill(bgcolor)
    screen.blit(canvas, [0,0])
    pygame.display.flip()
pygame.quit()
