from typing import List
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        d = defaultdict(int)
        ans = unpaired = 0

        for w in words:

            if w[0] == w[1]:
                if d[w] > 0:
                    ans += 4
                    d[w] -= 1
                    unpaired -= 1
                else:
                    unpaired += 1
                    d[w] += 1
            else:
                if d[w[::-1]] > 0:
                    ans += 4
                    d[w[::-1]] -= 1
                else:
                    d[w] += 1
        if unpaired > 0: ans += 2
        return ans

sol = Solution()

input = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]

print(sol.longestPalindrome(input))

