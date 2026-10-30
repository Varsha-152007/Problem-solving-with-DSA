# Problem: Rotate Array
# Problem Link: https://leetcode.com/problems/rotate-array/description/?envType=problem-list-v2&envId=array
# Date: 30th Oct 2026
# Time taken to solve: 20 mins

#solution
<
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

>

#Note
#Reverse the entire array, then reverse the first k elements and the remaining elements separately to rotate the array right by k positions.
