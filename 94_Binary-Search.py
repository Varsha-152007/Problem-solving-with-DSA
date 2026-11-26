# Problem: Binary Search
# Problem Link:https://leetcode.com/problems/binary-search/description/?envType=problem-list-v2&envId=array
# Date: 26th Nov 2026
# Time taken to solve: 20mins

#solution
<
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
      >
#Note
#Used Binary Search: Check the middle element and eliminate half of the sorted array until the target is found or the search space becomes empty.
