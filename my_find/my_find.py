import sys, os

def my_find(dir, suffix):
    ls =  os.listdir(dir)
    for i in ls:
        item = os.path.join(dir, i)
        if os.path.isfile(item):
            if item.find(suffix) == len(item) - len(suffix):
                print (item)
        else:
            my_find(item, suffix)


if len(sys.argv) >= 3:
    my_find(sys.argv[1], sys.argv[2])
else:
    print ("usage: python my_find.py directory extension")