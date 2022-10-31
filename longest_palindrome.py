from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        palindromes = matches = 0

        for i, word in enumerate(words):
            
            words[i] = 0

            if word == word[::-1]:
                
                if word in words:
                    matches += 4
                    words.remove(word[::-1])
                else:
                    palindromes += 2

            elif word[::-1] in words:
                matches += 4
                words.remove(word[::-1])
        
        return matches + (palindromes > 0) * 2
            
            
            

sol = Solution()

input = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]

print(sol.longestPalindrome(input))

