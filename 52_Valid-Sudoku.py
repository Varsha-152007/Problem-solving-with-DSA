# Problem: Valid Sudoku
# Problem Link: https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=array
# Date: 10th Oct 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                box = (i // 3) * 3 + (j // 3)

                if (num in rows[i] or
                    num in cols[j] or
                    num in boxes[box]):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

        return True
>

#Notes
#Used three sets for each row, column, and 3×3 box; traverse every cell, return False if a digit repeats, otherwise add it to the sets and return True after checking the entire board.
