#!/bin/python3

import os
from functools import lru_cache


def getWays(n, c):
    @lru_cache(maxsize=None)
    def ways(n, i):
        if n == 0:
            return 1
        if n < 0 or len(c) == i:
            return 0
            
        take = ways(n - c[i], i)
        skip = ways(n, i+1)
    
        return take + skip
    
    return ways(n,0)

def getWays(n, coins):
    dp = [0] * (n+1)
    dp[0] = 1
    
    for c in coins:
        for i in range(c, n+1):
            dp[i] += dp[i-c]
    
    return dp[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
