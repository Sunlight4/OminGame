import Item

def parseItemIndex(path):
    fl = open('path')

    lines = fl.readlines()
    new = []

    for line in lines:
        line = line.strip()

        idname = line.split('=')[0]
        name = line.split('=')[1]
        obj = eval('Item.'+name)

        new.append([idname,name,obj])
    return new

        
