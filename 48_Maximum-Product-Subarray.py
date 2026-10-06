# Problem: Maximum Product Subarray
# Problem Link: https://leetcode.com/problems/maximum-product-subarray/description/?envType=problem-list-v2&envId=array
# Date: 6th Oct 2026
# Time taken to solve: 42 mins

#solution
<
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_max = cur_min = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            ans = max(ans, cur_max)

        return ans
>

#Note:
#Track both the maximum and minimum product ending at each index because a negative number can turn the smallest product into the largest.



