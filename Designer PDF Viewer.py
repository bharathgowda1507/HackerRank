#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    char_list = [chr(x) for x in range(ord('a'), ord('z') + 1)] 
    heights = list()

    for i in range(len(word)):
        index = char_list.index(word[i])
        height = h[index]
        heights.append(height)

    return (max(heights)*len(word))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
