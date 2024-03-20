'''
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Example


There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

Function Description

Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):

int a[n]: an array of integers
Returns

int: the length of the longest subarray that meets the criterion
Input Format

The first line contains a single integer , the size of the array .
The second line contains  space-separated integers, each an .

Constraints

The answer will be .
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    result = 0
    a = sorted(a)
    for i in range(len(a)):
        min_e = a[i]
        max_e = a[i]
        j= i+1
        
        while (j<len(a)) and (abs(a[j]-min_e) < 2) and (abs(a[j]-max_e) < 2):
            if min_e > a[j]:
                min_e = a[j]
            elif max_e < a[j]:
                max_e = a[j]
            j+=1
        
        if result < (j-i):
            result = (j-i)
    
    return result
                    
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
