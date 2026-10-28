# Problem: Pascal's Triangle II
# Problem Link: https://leetcode.com/problems/pascals-triangle-ii/description/?envType=problem-list-v2&envId=array
# Date: 28th Oct 2026
# Time taken to solve: 20 mins

#solution
<
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]

        for i in range(rowIndex):
            row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]

        return row
>

#Note
#Start with [1] and repeatedly build the next row by adding adjacent elements and keeping 1 at both ends.
