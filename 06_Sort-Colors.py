# Problem: Sort Colors
# Problem Link: https://leetcode.com/problems/sort-colors/description/?envType=problem-list-v2&envId=array
# Date: 24th Aug 2026
# Time taken to solve: 15 mins

#solution
<
class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums
      >

#Notes:
#Implement a solution for sorting colors using a bubble sort algorithm.
