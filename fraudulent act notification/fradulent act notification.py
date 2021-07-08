#!/bin/python3

import math
import os
import random   
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
        n = len(expenditure)
        # expenditure.sort()
        median = 0
        notif = 0
        if(d >= n):
            return 0
        else:
            if d % 2 == 0:
                for index in range(0, n-d):
                    expense = sorted(expenditure[index:index+d])
                    print(len(expense))
                    print(int(d/2)+index)
                    median = (expense[int(d/2) -1] + expense[int(d/2)])/2
                    if expenditure[d+index] >= 2*median :
                             notif+=1
            else:
                for index in range(0, n-d):
                    expense = sorted(expenditure[index:index+d])
                    median = expense[int(d/2)]
                    if expenditure[d+index] >= 2*median :
                             notif+=1
        print(notif)                     
        return notif
                        
                
            

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open(r'D:\\Trial_Projects_Python\\Hackerrank\\fraudulent act notification\\input01.txt', 'r')

    first_multiple_input = fptr.read().rstrip().split('\n')
    

    n = int(first_multiple_input[0].rstrip().split()[0])
    
    d = int(first_multiple_input[0].rstrip().split()[1])
    
    expenditure = list(map(int, first_multiple_input[1].rstrip().split()))
    
    result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    # fptr.close()
