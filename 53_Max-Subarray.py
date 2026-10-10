# Problem: Maximum Subarray
# Problem Link: https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=array
# Date: 11th Oct 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
>

#Notes
#Used Kadane’s Algorithm approach.
