# Problem: Reverse String II
# Problem Link: https://leetcode.com/problems/reverse-string-ii/description/?envType=problem-list-v2&envId=string
# Date: 24th Nov 2026
# Time taken to solve: 20mins

#solution
<
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        for i in range(0, len(s), 2 * k):
            s[i:i+k] = reversed(s[i:i+k])

        return ''.join(s)
      >
#Note
#Reverse the first k characters in every 2k block using slicing.
