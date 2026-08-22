# Problem: Single Number
# Problem Link: https://leetcode.com/problems/single-number/description/
# Date: 22st Aug 2026
# Time taken to solve: 10 mins

#solution
<
class Solution(object):
    def singleNumber(self, nums):
        frequencies = {}

        for element in nums:
            frequencies[element] = frequencies.get(element, 0) + 1
        
        for k, v in frequencies.items():
            if v == 1:
                return k
      >

#Notes:
Implemented frequency map approach
