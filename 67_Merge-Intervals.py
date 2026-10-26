# Problem: Merge Intervals
# Problem Link: https://leetcode.com/problems/merge-intervals/description/?envType=problem-list-v2&envId=array
# Date: 26th Oct 2026
# Time taken to solve: 30 mins

#solution
<
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = []

        for start, end in intervals:
            if not result or result[-1][1] < start:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)

        return result
>

#Note
#Sort intervals by start time, then merge overlapping intervals by updating the previous interval's ending value.
