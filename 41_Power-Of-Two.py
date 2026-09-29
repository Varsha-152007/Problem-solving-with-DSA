# Problem: Power Of Two
# Problem Link: https://leetcode.com/problems/power-of-two/description/?envType=problem-list-v2&envId=math
# Date: 28th Sept 2026
# Time taken to solve: 20 min

#solution
<
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n //= 2

        return n == 1
        
      >
#Notes
#Used repeated division by 2; if the number reduces exactly to 1, it is a power of two.
