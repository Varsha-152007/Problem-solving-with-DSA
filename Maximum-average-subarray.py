# Problem: Maximum Average Subarray I
# Problem Link: https://leetcode.com/problems/maximum-average-subarray-i/
# Date: 19th Aug 2026
# Time taken to solve: 40 mins

#solution
<
class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        ans = curr_sum / float(k)

        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]

            ans = max(ans, curr_sum / float(k))

        return ans
      >

#Notes:
#Used sliding window technique
