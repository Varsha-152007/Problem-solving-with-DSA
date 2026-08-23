# Problem: Remove Element
# Problem Link: https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array
# Date: 23rd Aug 2026
# Time taken to solve: 20 mins

#solution
<
class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
      >

#Notes:
#Remove Element using single pass 
