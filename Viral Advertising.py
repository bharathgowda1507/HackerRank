#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5
    liked = 2
    cumulative = 2

    if(n == 1):
        return cumulative

    for i in range(1,n):
        shared = liked * 3
        liked = int(math.floor(shared/2))
        cumulative += liked

    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
