# Problem: Modify The Matrix
# Problem Link: https://leetcode.com/problems/modify-the-matrix/description/
# Date: 2nd Oct 2026
# Time taken to solve: 40 mins

#solution
<
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]

        return matrix
      >

#Notes:
#Find the maximum value of each column, then replace every -1 with its corresponding column maximum.
