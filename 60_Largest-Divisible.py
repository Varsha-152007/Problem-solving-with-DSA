# Problem: Largest Divisible Subset
# Problem Link: https://leetcode.com/problems/largest-divisible-subset/description/?envType=problem-list-v2&envId=sorting
# Date: 19th Oct 2026
# Time taken to solve: 55 mins

#solution
<
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[x] for x in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]

        return max(dp, key=len)
>

