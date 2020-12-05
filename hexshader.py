#!/usr/bin/python

import sys

def print_help():
    print("HELP")


def tint(hexcolor, percent):
    hexcolor = hexcolor.lstrip("#")

    print(hexcolor)

def main():
    num_args = len(sys.argv)

    if num_args == 1 or num_args > 3 or (num_args == 2 and sys.argv[1] == "-h"):
        print_help()
    elif num_args == 2:
        print("-- 1")
    elif num_args == 3:
        hexcolor = sys.argv[1]
        percent = sys.argv[2]
        tint(hexcolor, percent)

if __name__ == "__main__":
    main()
