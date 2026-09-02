# Problem: Majority Element
# Problem Link: https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=hash-table
# Date: 2nd Sept 2026 
# Time taken to solve: 15 mins

#solution
<
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
        
      >

#Notes:
#Used sorting method
