#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    spottings = dict()
    types = set(arr)

    for i in types:
        count = 0
        for j in arr:
            if j == i:
                count += 1
        spottings[i] = count

    return max(spottings, key=spottings.get)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
