# Problem: Subsets II
# Problem Link: https://leetcode.com/problems/subsets-ii/description/?envType=problem-list-v2&envId=array
# Date: 12th Nov 2026
# Time taken to solve: 45mins

#solution
<
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        def solve(i, path):
            ans.append(path[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                path.append(nums[j])
                solve(j+1, path)
                path.pop()

        solve(0, [])
        return ans
>
#Notes
#Use backtracking to generate all subsets and skip duplicate elements after sorting the array
