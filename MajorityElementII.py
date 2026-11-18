# Problem: Majority Element II
# Problem Link: https://leetcode.com/problems/majority-element-ii/description/
# Date: 18th Nov 2026
# Time taken to solve: 45 mins

#solution
<
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = []
        n = len(nums)

        for num in count:
            if count[num] > n // 3:
                result.append(num)

        return result
      >
