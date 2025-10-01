#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w) -> str:
    pivot  = -1
    for i in range(len(w)-1, 0,-1):
        if w[i] > w[i-1]:
            pivot = i-1
            break
    
    if pivot == -1:
        return 'no answer'
    
    swap_index = -1
    for i in range(len(w)-1, pivot, -1):
        if w[i] > w[pivot]:
            swap_index = i
            break

    # w_list = list(w)
    # w_list[pivot], w_list[swap_index] = w_list[swap_index], w_list[pivot]
    # w = ''.join(w_list)
    # print(pivot)
    # print(swap_index)
    w[pivot], w[swap_index] = w[swap_index], w[pivot]
    print(w[:pivot + 1], w[len(w)-1: pivot: -1], sep = '\n')

    ret = w[:pivot + 1] + w[len(w)-1: pivot: -1]
    
    return ret
    
    
    

if __name__ == '__main__':
    
    w = [2, 4, 3, 1]
    print(biggerIsGreater(w))
#1 e c
#2 f d
#3 g h
#4 h k

# 4123
# 4132

# 4213