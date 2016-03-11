import sys

def my_sed(from_word, to_word, in_file):
    print(from_word)
    print(to_word)
    print(in_file)



if len(sys.argv) >= 4:
    my_sed(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("usage: python my_find.py from_word to_word file")