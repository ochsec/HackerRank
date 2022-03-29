#!/bin/python3
# https://www.hackerrank.com/challenges/maximum-element/problem

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    stack = []
    print_items = []
    max_n = 0
    last_maxes = []
    for op in operations:
        args = op.split(' ')
        if args[0] == '1':
            stack.append(int(args[1]))
            if int(args[1]) >= max_n:
                last_maxes.append(max_n)
                max_n = int(args[1])
        elif args[0] == '2':
            popped = stack.pop()
            if max_n == popped:
                max_n = last_maxes.pop()
        else:
            print_items.append(max_n)
            
    return print_items

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
