# Problem: https://leetcode.com/problems/reshape-the-matrix/description/
# Date: 1st Oct 2026
# Time taken to solve: 45 min

#solution
<
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        elements = [x for row in mat for x in row]

        return [elements[i * c:(i + 1) * c] for i in range(r)] 
        >
#Notes
#Checked if the total elements match, then flatten the matrix row-wise and rebuild it into the required r × c shape.
