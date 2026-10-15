# Problem: Nim Game
# Problem Link: https://leetcode.com/problems/nim-game/description/?envType=problem-list-v2&envId=math
# Date: 15th Oct 2026
# Time taken to solve: 15 mins

#solution
<
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
>

#Notes
#If n % 4 == 0, return false; otherwise, return true, since the first player can always force a win by leaving a multiple of 4 stones for the opponent.


