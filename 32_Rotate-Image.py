# Problem:  Rotate Image
# Problem Link: https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=array
# Date: 19th Sept 2026
# Time taken to solve: 45 min

#solution
<
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
    
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
            
        for i in range(n):
            matrix[i].reverse()
      >
#Notes
#Rotated the matrix 90° clockwise by swapping across the diagonal and reversing each row.
