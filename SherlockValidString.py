#!/bin/python3
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    c = Counter(s)
    
    freq_mode = {}
    for x in c.values():
        freq_mode[x] = freq_mode.get(x, 0) + 1
        
    mode = 0
    freq = 0
    for k in freq_mode.keys():
        if  freq_mode[k] > freq:
            freq = freq_mode[k]
            mode = k
            
    non_common = []
    for x in c.values():
        if x != mode:
            non_common.append(x)
    
    if len(non_common) > 1:
        return 'NO'
    if len(non_common) == 1:
        if non_common[0] != mode + 1 and non_common[0] != 1:
            return 'NO'
    
    return 'YES'

if __name__ == '__main__':

    s = 'abcdefghhgfedecba'

    print(isValid(s))
