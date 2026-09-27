# Problem: Climbing Stairs
# Problem Link: https://leetcode.com/problems/climbing-stairs/description/?envType=problem-list-v2&envId=math
# Date: 27th Sept 2026
# Time taken to solve: 25 min

#solution
<
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):
            one, two = one + two, one

        return one
        
      >
#Notes
#Used two variables to store the previous two Fibonacci values and update them iteratively to find the number of ways to reach step n.
