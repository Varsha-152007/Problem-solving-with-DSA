# Problem: Count and Say
# Problem Link: https://leetcode.com/problems/count-and-say/description/?envType=problem-list-v2&envId=string
# Date: 24th Oct 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            res = ""
            i = 0

            while i < len(s):
                count = 1

                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1

                res += str(count) + s[i]
                i += 1

            s = res

        return s
>

#Note
#Start with "1" and repeatedly count consecutive identical digits, appending each count followed by its digit to generate the next sequence.
