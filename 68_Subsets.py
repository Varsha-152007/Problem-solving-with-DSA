# Problem: Merge Intervals
# Problem Link: https://leetcode.com/problems/subsets/description/?envType=problem-list-v2&envId=array
# Date: 27th Oct 2026
# Time taken to solve: 30 mins

#solution
<
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]

        for num in nums:
            new_subsets = []

            for subset in result:
                new_subsets.append(subset + [num])

            result.extend(new_subsets)

        return result
>

#Note
#Start with an empty subset and, for each number, create new subsets by adding that number to every existing subset.
