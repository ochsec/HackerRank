#Given a time in AM/PM format, convert it to military (-hour) time.

#Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.

#Input Format: A single string containing a time in -hour clock format (i.e.:  or ), where .

#Output Format: Convert and print the given time in -hour format, where .

#Sample Input
#07:05:45PM

#Sample Output
#19:05:45

#!/bin/python3

import sys

time = input().strip()
# split the time string by the colon
time_pieces = time.split(':')
# get the AM or PM part of the last piece of the time string
am_or_pm = ''.join(filter(lambda x: x.isalpha(), time_pieces[2]))
# set a boolean to indicate whether the original time was pm
is_pm = False if am_or_pm.lower() == "am" else True
# add 12 to the first part of the string if it was pm and the number is less than 12
if (is_pm == True):
    if (int(time_pieces[0]) < 12):
        time_pieces[0] = str(int(time_pieces[0]) + 12)
# make 12 am '00'
if (is_pm == False):
    if (int(time_pieces[0]) == 12):
        time_pieces[0] = '00'
# put the pieces back together and drop the 'AM' or 'PM'
print("{0}:{1}:{2}".format(time_pieces[0], time_pieces[1], ''.join(filter(lambda x: x.isdigit(), time_pieces[2]))))
