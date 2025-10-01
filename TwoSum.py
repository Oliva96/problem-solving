from typing import List


class Solution:
    def twoSum(self, nums, target: int):
        d = {}
        for (index,i) in enumerate(nums):
            d[target - i] = index
        
        for (index,i) in enumerate(nums):
            if i in d:
                if index == d[i]:
                    continue
                return [index, d[i]]

s = Solution()

nums = [3, 3]

print(s.twoSum(nums, 6))