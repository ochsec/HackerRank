#!/bin/python3
# https://www.hackerrank.com/challenges/equal-stacks/problem

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    # make an array of sums
    sums = list(map(sum, (h1, h2, h3)))
    while h1 and h2 and h3:
        min_sum = min(sums)
        while sums[0] > min_sum:
            sums[0] -= h1.pop(0)
        while sums[1] > min_sum:
            sums[1] -= h2.pop(0)
        while sums[2] > min_sum:
            sums[2] -= h3.pop(0)
        if (sums[0] == sums[1] == sums[2]):
            return sums[0]
    return 0            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()