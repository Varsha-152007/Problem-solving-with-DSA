# Problem: Set Mismatch
# Problem Link: https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=sorting
# Date: 13th Oct 2026
# Time taken to solve: 30 mins

#solution
<
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        duplicate = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                return [duplicate, i]
>

#Notes
#Use a set to detect the duplicate in one pass, then find the missing number by checking which number from 1 to n is absent.
