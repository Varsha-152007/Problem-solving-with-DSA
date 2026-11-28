# Problem: Array Partition
# Problem Link: https://leetcode.com/problems/array-partition/description/?envType=problem-list-v2&envId=array
# Date: 28th Nov 2026
# Time taken to solve: 20mins

#solution
<
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        total = 0

        for i in range(0, len(nums), 2):
            total += nums[i]

        return total
      >
# Key idea: Sort the array and add elements at indices
