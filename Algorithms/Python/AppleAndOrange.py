#!/bin/python3
# https://www.hackerrank.com/challenges/apple-and-orange/problem

# import math
# import os
# import random
# import re
# import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_fell_on_house = 0
    oranges_fell_on_house = 0
    for apple in apples:
        if fell_on_house(s, t, a, apple):
            apples_fell_on_house = apples_fell_on_house + 1
    for orange in oranges:
        if fell_on_house(s, t, b, orange):
            oranges_fell_on_house = oranges_fell_on_house + 1
    print(apples_fell_on_house)
    print(oranges_fell_on_house)

def fell_on_house(x, y, tree_loc, loc):
    drop_loc = tree_loc + loc
    if (drop_loc >= min(x, y) and drop_loc <= max(x, y)):
        return True
    else:
        return False;
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
