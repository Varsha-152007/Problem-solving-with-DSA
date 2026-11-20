# Problem: Target Sum
# Problem Link: https://leetcode.com/problems/target-sum/description/
# Date: 20th Nov 2026
# Time taken to solve: 1hr 5mins

#solution
<
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}

        def solve(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in memo:
                return memo[(i, total)]

            plus = solve(i + 1, total + nums[i])
            minus = solve(i + 1, total - nums[i])

            memo[(i, total)] = plus + minus

            return memo[(i, total)]

        return solve(0, 0)
      >
