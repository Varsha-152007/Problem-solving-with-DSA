# Problem: Pascal's Triangle
# Problem Link: https://leetcode.com/problems/pascals-triangle/submissions/2120887204/?envType=problem-list-v2&envId=array
# Date: 26th Aug 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle
      >

#Notes:
#Implemented Pascal's Triangle using the previous row to calculate middle elements.
