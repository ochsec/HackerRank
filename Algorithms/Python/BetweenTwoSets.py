#!/bin/python3
# https://www.hackerrank.com/challenges/between-two-sets/problem

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    factors = []
    min_x = 100
    min_n = 100
    
    for x in a:
        if x < min_x:
            min_x = x

    for n in b:
        if n < min_n:
            min_n = n
        
    for i in range(min_x, min_n + 1):
        is_factor = True
        for x in a:
            if i % x == 0:
                continue
            else:
                is_factor = False
                break
        
        if is_factor:
            for n in b:
                if n % i == 0:
                    continue
                else:
                    is_factor = False
                    break
        
        if is_factor:
            factors.append(i)
            
    return len(factors)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    fptr.write(str(total) + '\n')
    fptr.close()

