# Problem: Maximum Gap
# Problem Link: https://leetcode.com/problems/maximum-gap/description/?envType=problem-list-v2&envId=array
# Date: 4th Nov 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()

        ans = 0

        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - nums[i-1])

        return ans
>
#Notes
#Sort the array and find the maximum difference between adjacent elements.
