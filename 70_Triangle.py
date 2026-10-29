# Problem: Triangle
# Problem Link: https://leetcode.com/problems/triangle/description/?envType=problem-list-v2&envId=array
# Date: 29th Oct 2026
# Time taken to solve: 25 mins

#solution
<
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
>

#Note
#Use bottom-up DP, adding each element to the minimum of its two adjacent values in the row below.
