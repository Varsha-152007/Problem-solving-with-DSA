# Problem: Jump Game II
# Problem Link: https://leetcode.com/problems/jump-game-ii/description/?envType=problem-list-v2&envId=array
# Date: 22nd Oct 2026
# Time taken to solve: 55 mins

#solution
<
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest

        return jumps
>

#Note
#Track the farthest reachable index and increase the jump count whenever you reach the end of the current jump range.
