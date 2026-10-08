# Problem: Add Digits
# Problem Link: https://leetcode.com/problems/add-digits/description/?envType=problem-list-v2&envId=math
# Date: 8th Oct 2026
# Time taken to solve: 25 mins

#solution
<
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            num = total

        return num
>

#Notes
#Repeatedly extract each digit using % 10, add them together, and continue until the number becomes a single digit.
