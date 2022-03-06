#!/bin/python3
# https://www.hackerrank.com/challenges/migratory-birds

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    counts = [0, 0, 0, 0, 0]
    
    for n in arr:
        counts[n - 1] += 1
    
    max_id = -1
    max_count = 0
    i = 1
        
    for c in counts:
        if c > max_count:
            max_count = c
            max_id = i
        i += 1
            
    return max_id
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
