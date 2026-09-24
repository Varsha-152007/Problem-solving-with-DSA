# Problem: Toeplitz Matrix
# Problem Link: https://leetcode.com/problems/toeplitz-matrix/description/
# Date: 24th Sept 2026
# Time taken to solve: 25 min

#solution
<
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True
      >
#Notes
#Checked each element with its top-left diagonal neighbor; if any differ, return false, otherwise return true.
