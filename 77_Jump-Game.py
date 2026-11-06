# Problem: Jump Game
# Problem Link: https://leetcode.com/problems/jump-game/?envType=problem-list-v2&envId=array
# Date: 6th Nov 2026
# Time taken to solve: 30 mins

#solution
<
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

        return True
>
