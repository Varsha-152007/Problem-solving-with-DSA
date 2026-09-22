# Problem: Contains Duplicate II
# Problem Link:https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=array
# Date: 22nd Sept 2026
# Time taken to solve: 25 min

#solution
<
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_index = {}

        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True

            last_index[num] = i

        return False
      >
#Notes
#Used a hash map to store the last index of each number and checked if the index difference is <= k.
