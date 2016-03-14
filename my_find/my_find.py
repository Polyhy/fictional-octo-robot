import sys
import os


def my_find(directory, suffix):
    path = os.path.abspath(directory)
    ls = os.listdir(path)
    for i in ls:
        item = os.path.join(path, i)
        if os.path.isfile(item):
            if item.find(suffix) == len(item) - len(suffix):
                print(item)
        else:
            my_find(item, suffix)


if len(sys.argv) >= 3:
    my_find(sys.argv[1], sys.argv[2])
else:
    print("usage: python my_find.py directory extension")
