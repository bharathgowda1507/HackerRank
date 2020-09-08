#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = set(ar)
    dic = {}

    for i in colors:
        count = 0
        for j in ar:
            if i == j:
                count += 1
        dic[i] = count

    pairs = 0

    temp = dic.values()

    for i in temp:
        pairs += math.floor(i/2)

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
