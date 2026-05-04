import os
import sys
import json  # F401: imported but unused

def main():
    print("Hello from dsc190-tools-assignment-5!")

def foo(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):  # E501 if long enough + too many args
    l = []  # E741: ambiguous variable name 'l'
    if a == True:  # E712: comparison to True
        pass
    return l

if __name__ == "__main__":
    main()
    x=1+2  # E225: missing whitespace around operator
    y = {'key' : 'value'}  # E203: whitespace before ':'
    