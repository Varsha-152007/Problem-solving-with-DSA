# Problem: Sum in a Matrix
# Problem Link: https://leetcode.com/problems/sum-in-a-matrix/description/
# Date: 9th Oct 2026
# Time taken to solve: 25 mins

#solution
<
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)

        score = 0
        for col in range(len(nums[0])):
            score += max(row[col] for row in nums)

        return score
        
>

#Notes
#Sort each row in descending order, then add the maximum element of each column to get the final score.


