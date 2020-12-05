#!/usr/bin/python

import sys

def print_help():
    print("HELP")

def hex_to_rgb(hexcolor):
    hexcolor = hexcolor.lstrip("#")
    return tuple(int(hexcolor[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def shade(hexcolor, percent):
    rgb = hex_to_rgb(hexcolor)
    if percent > 50:
        shade_factor = (100 - percent) * 0.02
        return rgb_to_hex(tuple(x * shade_factor for x in rgb))
    elif percent < 50:
        tint_factor = (100 - 2 * percent) / 100.0
        return rgb_to_hex(tuple(x + (255 - x) * tint_factor for x in rgb))
    else:
        return rgb_to_hex(rgb)

def main():
    num_args = len(sys.argv)

    if num_args == 1 or num_args > 3 or (num_args == 2 and sys.argv[1] == "-h"):
        print_help()
    elif num_args == 2:
        hexcolor = sys.argv[1]
        for percent in range(100, 0, -10):
            print(shade(hexcolor, percent))
    elif num_args == 3:
        hexcolor = sys.argv[1]
        percent = int(sys.argv[2])
        print(shade(hexcolor, percent))

if __name__ == "__main__":
    main()
