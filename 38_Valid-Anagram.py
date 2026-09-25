# Problem: Valid Anagram
# Problem Link: https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=string
# Date: 25th Sept 2026
# Time taken to solve:30 min

#solution
<
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            if s.count(char) != t.count(char):
                return False

        return True
      >
#Notes
#Compared each character of s with unused characters in t, marking matches to verify whether the two strings are anagrams.



