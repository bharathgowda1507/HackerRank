#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    countpos, countneg, count0 = [0, 0, 0]

    for i in arr:
        if i > 0:
            countpos += 1
        elif i < 0:
            countneg += 1
        else:
            count0 += 1

    print('%.6f' % float(countpos/len(arr)))
    print('%.6f' % float(countneg/len(arr)))
    print('%.6f' % float(count0/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
