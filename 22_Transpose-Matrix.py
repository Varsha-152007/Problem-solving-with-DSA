# Problem: Transpose Matrix
# Problem Link: https://leetcode.com/problems/transpose-matrix/description/
# Date: 9th Sept 2026
# Time taken to solve: 25 min

#solution
<
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        result = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]

        return result
      >
#Notes
#matrix transpose using row-column iteration.
