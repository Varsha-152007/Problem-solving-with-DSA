# Problem: Detect Capital
# Problem Link: https://leetcode.com/problems/detect-capital/description/?envType=problem-list-v2&envId=string
# Date: 22nd Nov 2026
# Time taken to solve: 25mins

#solution
<
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (word.isupper() or
                word.islower() or
                word[0].isupper() and word[1:].islower())
      >
#Note
#Check whether all letters are uppercase, all lowercase, or only the first letter is uppercase.
