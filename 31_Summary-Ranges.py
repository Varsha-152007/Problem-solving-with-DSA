# Problem:  Summary Ranges
# Problem Link: https://leetcode.com/problems/summary-ranges/description/?envType=problem-list-v2&envId=array
# Date: 18th Sept 2026
# Time taken to solve: 40 min

#solution
<
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        start = 0

        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == i:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + "->" + str(nums[i]))

                start = i + 1

        return ans
      >
#Notes
#Grouping consecutive numbers and add each group as a range when the sequence breaks.
