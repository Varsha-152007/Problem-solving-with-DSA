# Problem: Longest Palindromic Substring
# Problem Link: https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=stringy
# Date: 12th Oct 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1

                if r - l - 1 > len(res):
                    res = s[l + 1:r]

        return res
>

#Notes
#Start from each possible center, expand while characters match, and store the longest palindrome found.
