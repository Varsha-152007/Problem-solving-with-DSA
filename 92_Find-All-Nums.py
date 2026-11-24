# Problem: Find All Numbers Disappeared in an Array
# Problem Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/?envType=problem-list-v2&envId=array
# Date: 23rd Nov 2026
# Time taken to solve: 25mins

#solution
<
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in s:
                result.append(i)

        return result
      >
#Note
#Use a set to store existing numbers, then check numbers from 1 to n and collect the missing ones.
