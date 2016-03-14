import sys
import os


def my_sed(from_word, to_word, in_file):
    try:
        res = b""
        with open(in_file, "rb") as f:
            lines = f.readlines()
            for line in lines:
                res += line.replace(from_word.encode(), to_word.encode())
        with open(in_file, "wb") as f:
            f.write(res)
    except IOError:
        print(os.path.abspath(in_file) + " is Not Found")


if len(sys.argv) >= 4:
    my_sed(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("usage: python my_sed.py from_word to_word file")
