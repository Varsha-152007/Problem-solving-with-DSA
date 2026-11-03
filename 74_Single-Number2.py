# Problem: Single Number II
# Problem Link: https://leetcode.com/problems/single-number-ii/description/?envType=problem-list-v2&envId=array
# Date: 3rd Nov 2026
# Time taken to solve: 15 mins

#solution
<
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            if count == 1:
                return num
>
#Notes
#Used a dictionary to count the frequency of each number and return the number whose frequency is 1.
