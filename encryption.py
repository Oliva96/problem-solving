#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s: str):
    s = s.strip().replace(' ', '')
    l = len(s)
    c = math.ceil(l ** (0.5))
    
    ans = ''
    for i in range(c):
        c_i = ''
        for j in range(i, l, c):
            c_i += s[j]
        ans += c_i + ' '
    
    return ans[:len(ans)-1]


if __name__ == '__main__':

    s = 'haveaniceday'

    print(encryption(s))
