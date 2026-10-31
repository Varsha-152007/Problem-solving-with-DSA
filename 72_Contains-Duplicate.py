# Problem: Contains Duplicate
# Problem Link: https://leetcode.com/problems/contains-duplicate/description/
# Date: 31st Oct 2026
# Time taken to solve: 25 mins

#solution
<
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         return len(nums) != len(set(nums))

>

