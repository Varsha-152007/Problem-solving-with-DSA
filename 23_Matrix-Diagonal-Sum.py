# Problem: Matrix Diagonal Sum
# Problem Link: https://leetcode.com/problems/matrix-diagonal-sum/description/
# Date: 10th Sept 2026
# Time taken to solve: 30 min

#solution
<
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0

        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n - i - 1]

        if n % 2 == 1:
            ans -= mat[n // 2][n // 2]

        return ans
      >
#Notes
#Added both diagonals and subtracted the center element once if counted twice.
