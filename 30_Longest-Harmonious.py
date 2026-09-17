# Problem:  Longest Harmonious Subsequence
# Problem Link: https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=problem-list-v2&envId=sliding-window
# Date: 17th Sept 2026
# Time taken to solve: 40 min

#solution
<
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()

        left = 0
        ans = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1

            if nums[right] - nums[left] == 1:
                ans = max(ans, right - left + 1)

        return ans
      >
#Notes
#Used sliding window approach.
