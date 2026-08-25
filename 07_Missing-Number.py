# Problem: Missing Number
# Problem Link: https://leetcode.com/problems/missing-number/description/
# Date: 25th Aug 2026
# Time taken to solve: 5 mins

#solution
<
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
      >

#Notes:
#Solve Missing Number using sorting
