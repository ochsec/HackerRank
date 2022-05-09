#!/bin/python3
# https://www.hackerrank.com/challenges/game-of-two-stacks/problem

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

class Stack:
    def __init__(self, array):
        self.count = 0
        self.items = {}
        for n in reversed(array):
            self.push(n)

    def push(self, el):
        self.items[self.count] = el
        self.count = self.count + 1

    def pop(self):
        if self.isEmpty():
            return None
        self.count = self.count - 1
        last = self.items[self.count]
        del self.items[self.count]
        return last

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[self.count - 1]

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

def twoStacks(maxSum, a, b):
    # Write your code here
    my_sum = 0
    count = 0
    A = Stack(a)
    B = Stack(b)
    C = Stack([])

    i = 0
    j = 0
    m = A.size()
    n = B.size()

    while i < m and my_sum + A.peek() <= maxSum:
        C.push(A.peek())
        my_sum += A.pop()
        i += 1
        count += 1

    while j < n and i >= 0:
        my_sum += B.pop()
        j += 1
        while my_sum > maxSum and i > 0:
            i -= 1
            my_sum -= C.pop()
        if my_sum <= maxSum and i + j > count:
            count = i + j
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
