# Problem: Permutations
# Problem Link: https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=array
# Date: 13th Nov 2026
# Time taken to solve: 45mins

#solution
<
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)

                    backtrack(path)

                    path.pop()

        backtrack([])
        return result
>
#Notes
#Use backtracking to select unused elements, build permutations, and remove the last element to explore other possibilities.
