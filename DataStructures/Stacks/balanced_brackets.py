#!/bin/python3
# https://www.hackerrank.com/challenges/balanced-brackets/problem

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
class Stack:
    def __init__(self):
        self.count = 0
        self.items = {}

    def push(self, el):
        self.items[self.count] = el
        self.count += 1

    def pop(self):
        if self.isEmpty():
            return None
        self.count -= 1
        last = self.items[self.count]
        del self.items[self.count]
        return last

    def isEmpty(self):
        return self.count == 0

def isBalanced(string):
    # Write your code here
    stack = Stack()
    length = len(s)
    
    # if there's an odd number of brackets we know they're not matched
    if (length % 2 == 1):
        return 'NO'

    match = 'YES'

    for sym in string:
        if sym in ['(', '[', '{']:
            stack.push(sym)
        else:
            head = stack.pop()
            if head == None:
                match = 'NO'
                break
            if sym == ')':
                if head == '(':
                    continue
                else:
                    match = 'NO'
                    break                    
            if sym == ']':
                if head == '[':
                    continue
                else:
                    match = 'NO'
                    break                    
            if sym == '}':
                if head == '{':
                    continue
                else:
                    match = 'NO'
                    break                    

    if not stack.isEmpty():
        match = 'NO'

    return match

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
