#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh, mm, ss, pmAM = [(s[0:2]), (s[3:5]), (s[6:8]), (s[8:])]
    
    if hh=='12' and pmAM=='PM':
        pass
    elif hh=='12' and pmAM=='AM':
        hh='00'
    elif pmAM=='PM':
        hh = str(int(hh) + 12)

    return hh+':'+mm+':'+ss
    
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
