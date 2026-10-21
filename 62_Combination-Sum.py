# Problem: Combination Sum
# Problem Link: https://leetcode.com/problems/combination-sum/description/?envType=problem-list-v2&envId=array
# Date: 21st Oct 2026
# Time taken to solve: 55 mins

#solution
<
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                backtrack(i, path, total + candidates[i])

                path.pop()

        backtrack(0, [], 0)
        return res
>

#Note
#Used backtracking to try each candidate, recursively reuse it while the sum is within the target, save valid combinations, and backtrack by removing the last chosen number.
