#!/bin/python3

#Sherlock Holmes suspects his archenemy, Professor Moriarty, is once again plotting something diabolical. 
#Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, 
#The Beast.

#Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast with 
#a virus; however, he also gives him a clue—a number, N. Sherlock determines the key to removing the virus is to 
#find the largest Decent Number having N digits.

#A Decent Number has the following properties:
#   1. Its digits can only be 3's and/or 5's.
#   2. The number of 3's it contains is divisible by 5.
#   3. The number of 5's it contains is divisible by 3.
#   4. If there are more than one such number, we pick the largest one.

#Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. Your task is to 
#help Sherlock find the key before The Beast is destroyed!

#Constraints
# 1 <= T <= 20
# 1 <= N <= 100000

#Input Format
#The first line is an integer, T, denoting the number of test cases.
#The T subsequent lines each contain an integer, N, detailing the number of digits in the number.

#Output Format
#Print the largest Decent Number having  digits; if no such number exists, tell Sherlock by printing -1.

#Sample Input
# 4
# 1
# 3
# 5
# 11

#Sample Output
# -1
# 555
# 33333
# 55555533333

#Explanation
#For N=1, there is no decent number having 1 digit (so we print -1).
#For N=3, 555 is the only possible number. The number 5 appears three times in this number, so our count of 5's 
#is evenly divisible by 3 (Decent Number Property 3).
#For N=5, 33333 is the only possible number. The number 3 appears five times in this number, so our count of 3's 
#is evenly divisible by 5 (Decent Number Property 2).
#For N=11, 55555533333 and all permutations of these digits are valid numbers; among them, the given number 
#is the largest one.

import sys

def decent(n):
    fives = 0
    threes = 0
    while n > 5 and n > 3:
        if ((n-3)%3 == 0 or (n-3)%5 == 0):
            n = n - 3
            threes += 1
        elif ((n-5)%3 == 0 or (n-5)%5 == 0):
            n = n - 5
            fives += 1
        else:
            print('-1')
            break
    else:
        if n == 3:
            threes += 1
            print_result(threes, fives)
        elif n == 5:
            fives += 1
            print_result(threes, fives)
        else:
            print('-1')
            

def print_result(threes, fives):
    result = ''
    while threes > 0:
        result = result + '555'
        threes = threes - 1
    while fives > 0:
        result = result + '33333'
        fives = fives - 1
    print(result)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    decent(n)


    