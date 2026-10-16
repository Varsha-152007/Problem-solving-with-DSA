# Problem: Third Maximum Number
# Problem Link: https://leetcode.com/problems/third-maximum-number/description/?envType=problem-list-v2&envId=sorting
# Date: 16th Oct 2026
# Time taken to solve: 25 mins

#solution
<
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = None

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if first is None or num > first:
                first, second, third = num, first, second
            elif second is None or num > second:
                second, third = num, second
            elif third is None or num > third:
                third = num

        return third if third is not None else first
>

#Notes
#Track the three largest distinct numbers in one pass, skipping duplicates and returning the third maximum if it exists; otherwise, return the overall maximum.
