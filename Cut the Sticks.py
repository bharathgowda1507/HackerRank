#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr,n):
    ans = [n]
    while n>1:
        minHeight = min(arr)
        arr = [x-minHeight for x in arr]
        while (arr.count(0)): 
            arr.remove(0)
        n = len(arr)
        if n!=0:
            ans.append(n)

    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr,n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
