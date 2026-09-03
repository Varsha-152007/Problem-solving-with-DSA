# Problem: Contains Duplicate
# Problem Link: https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=hash-table
# Date: 3rd Sept 2026 
# Time taken to solve: 15 mins

#solution
<
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        
      >

