# Problem: Sqrt(x)
# Problem Link: https://leetcode.com/problems/sqrtx/description/
# Date: 15th Sept 2026
# Time taken to solve: 35 min

#solution
<
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
          
        return ans
      >
#Notes
#sqrt(x) problem's solution using binary search.
