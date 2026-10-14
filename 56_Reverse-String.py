# Problem: Reverse String
# Problem Link: https://leetcode.com/problems/reverse-string/description/?envType=problem-list-v2&envId=string
# Date: 14th Oct 2026
# Time taken to solve: 30 mins

#solution
<
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
>

#Notes
#Use two pointers at opposite ends, swap their characters, and move both pointers inward until they meet.
