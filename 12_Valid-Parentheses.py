# Problem: Valid Parentheses
# Problem Link: https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack
# Date: 30th Aug 2026 
# Time taken to solve: 10 mins

#solution
<
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

        return s == ""
      >

#Notes:
#Brute force approach
