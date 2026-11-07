# Problem: Maximal Square
# Problem Link: https://leetcode.com/problems/maximal-square/description/?envType=problem-list-v2&envId=array
# Date: 7th Nov 2026
# Time taken to solve: 45 mins

#solution
<
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        maximum = 0

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == "1":

                    if i > 0 and j > 0:
                        matrix[i][j] = str(1 + min(
                            int(matrix[i-1][j]),
                            int(matrix[i][j-1]),
                            int(matrix[i-1][j-1])
                        ))

                    maximum = max(maximum, int(matrix[i][j]))

        return maximum * maximum
>
