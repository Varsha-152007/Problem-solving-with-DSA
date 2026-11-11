# Problem: Generate Parentheses
# Problem Link: https://leetcode.com/problems/generate-parentheses/description/
# Date: 11th Nov 2026
# Time taken to solve: 45mins

#solution
<
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def solve(s, open, close):
            if open == n and close == n:
                ans.append(s)
                return

            if open < n:
                solve(s + "(", open + 1, close)

            if close < open:
                solve(s + ")", open, close + 1)

        solve("", 0, 0)
        return ans
>
#Notes
#Add opening brackets until n, and add closing brackets only when opening brackets are greater than closing brackets.
