# Problem: Unique Paths
# Problem Link: https://leetcode.com/problems/unique-paths/description/?envType=problem-list-v2&envId=math
# Date: 16th Nov 2026
# Time taken to solve: 25 mins

#solution
<
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
      >

#Notes:
#Initialize the first row and column with 1, then fill the remaining cells by adding the top and left values.
