# Problem: Find The Differnce
# Problem Link: https://leetcode.com/problems/find-the-difference/description/?envType=problem-list-v2&envId=sorting
# Date: 4th Oct 2026
# Time taken to solve: 25 mins

#solution
<
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for ch in s:
            result ^= ord(ch)

        for ch in t:
            result ^= ord(ch)

        return chr(result)
      >

#Notes:
#Use XOR on all characters of s and t; matching characters cancel out, leaving only the one extra character.
