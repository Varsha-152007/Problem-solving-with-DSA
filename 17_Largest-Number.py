# Problem: Largest Number
# Problem Link: https://leetcode.com/problems/largest-number/submissions/2130239492/?envType=problem-list-v2&envId=sorting
# Date: 4th Sept 2026
# Time taken to solve: 45 mins

#solution
<
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))

        if nums[0] == "0":
            return "0"

        return "".join(nums)
        
      >
#Notes
#sorting the numbers using custom comparator that compares a+b with b+a to determine which order produces the larger number.
