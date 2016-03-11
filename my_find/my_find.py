import sys

def my_find(dir, suffix):
    print (dir)
    print (suffix)


if len(sys.argv) >= 3:
    my_find(sys.argv[1], sys.argv[2])
else:
    print ("usage: python my_find.py directory extension")