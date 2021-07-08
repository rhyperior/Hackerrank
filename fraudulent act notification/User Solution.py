#!/bin/python3
import time
start_time = time.time()
import math
import os
import random   
import re
import sys
from bisect import bisect_left, insort_left

def activityNotifications(expenditure, d):
    n = len(expenditure)
    t = expenditure
    noti = 0

    lastd = sorted(t[:d])
    def med():
        return lastd[d//2] if d % 2 == 1 else ((lastd[d//2] + lastd[d//2-1])/2)

    for i in range(d, n):
        if t[i] >= 2*med():
            noti += 1
        del lastd[bisect_left(lastd,t[i-d])]
        insort_left(lastd, t[i])
    print(noti)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open(r'D:\\Trial_Projects_Python\\Hackerrank\\fraudulent act notification\\input01.txt', 'r')

    first_multiple_input = fptr.read().rstrip().split('\n')
    

    n = int(first_multiple_input[0].rstrip().split()[0])
    
    d = int(first_multiple_input[0].rstrip().split()[1])
    
    expenditure = list(map(int, first_multiple_input[1].rstrip().split()))
    
    result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    fptr.close()
    print("Time:-- %s seconds"% (time.time() - start_time))
