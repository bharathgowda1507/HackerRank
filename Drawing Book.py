#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    pages = []
    countf, countb = [0,0]
    i = 0
    while i<=n:
        pages.append([i,i+1])
        i += 2

    for i in range(len(pages)):
        if (pages[i][0] == p) or (pages[i][1] == p):
            break
        else:
            countf += 1
            continue
    
    for i in range(len(pages)-1,-1,-1):
       if (pages[i][0] == p) or (pages[i][1] == p):
           break
       else:
           countb += 1
           continue

    return min(countf, countb)

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
