from functools import lru_cache


def coinChange(coins, amount: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return 2**31

            ret = 2**31
            for c in coins:
                ret = min(ret, dfs(amount - c) + 1)
            
            return ret
        
        dfs.cache_clear()
        ans = dfs(amount)

        return ans if ans != 2**31 else -1


def coinChange(coins, amount: int) -> int:
    dp = [2**31] * (10**4 +1)
    dp[0] = 0
    for x in range(1, 10**4 +1):
        for c in coins:
            if x - c >= 0:
                dp[x] = min(dp[x], dp[x-c]+1)
    
    return -1 if dp[amount] == 2**31 else dp[amount]