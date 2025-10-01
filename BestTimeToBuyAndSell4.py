class Solution:
    def maxProfit(self, k: int, prices) -> int:
     dp = [[0] * (k + 1)] * len(prices)
     



s = Solution()
prices = [1, 2, 3, 4]
k = 2
s.maxProfit(k, prices)