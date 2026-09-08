# Problem: Happy Numbers
# Problem Link: https://leetcode.com/problems/happy-number/description/
# Date: 8th Sept 2026
# Time taken to solve: 35 min

#solution
<
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return True
      >
#Notes
#solution for Happy Number problem using cycle detection and digit-square sum.
