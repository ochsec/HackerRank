#A Discrete Mathematics professor has a class of N students. Frustrated with their lack of discipline, he decides to cancel class if fewer than 
#K students are present when class starts.

#Given the arrival time of each student, determine if the class is canceled.

#Input Format: The first line of input contains T, the number of test cases.

#Each test case consists of two lines. The first line has two space-separated integers, N (students in the class) and K (the cancelation threshold). 
#The second line contains N space-separated integers (a1, a2, ..., aN) describing the arrival times for each student.

#Note: Non-positive arrival times (ai <= 0) indicate the student arrived early or on time; positive arrival times (ai > 0) 
#indicate the student arrived  minutes late.

#Output Format: For each test case, print the word YES if the class is canceled or NO if it is not.

#Note:  If a student arrives exactly on time (ai = 0), the student is considered to have entered before the class started.

#Sample Input
#2
#4 3
#-1 -3 4 2
#4 2
#0 -1 2 1 

#Sample Output
#YES
#NO

#!/bin/python3

import sys

def on_time(s):
    if s <= 0:          # on time or early
        return True
    else:
        return False

def threshold(count, k):
    if count >= k:
        print('NO')     # is not cancelled
    else:
        print('YES')    # is cancelled

def has_class(a, k):
    count = 0
    for s in a:
        if on_time(s) == True:
            count += 1
    threshold(count, k)

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    has_class(a, k)
    


