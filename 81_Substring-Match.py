# Problem: Substring Matching Pattern
# Problem Link: https://leetcode.com/problems/substring-matching-pattern/description/
# Date: 10th Nov 2026
# Time taken to solve: 30mins

#solution
<
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        a, b = p.split('*')

        i = s.find(a)

        if i == -1:
            return False

        j = s.find(b, i + len(a))

        return j != -1
>
#Notes
#Split the pattern at *, find the first part in the string, then search for the second part after the first part ends.
