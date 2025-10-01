from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        
        for x in d.values():
            ans.append(x)

        return ans
    
s = Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))