# Problem: 3Sum Closest
# Problem Link: https://leetcode.com/problems/3sum-closest/description/?envType=problem-list-v2&envId=array
# Date: 28th Aug 2026 
# Time taken to solve: 55 mins

#solution
<
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                curr = nums[i] + nums[left] + nums[right]

                if abs(curr - target) < abs(closest - target):
                    closest = curr

                if curr < target:
                    left += 1
                elif curr > target:
                    right -= 1
                else:
                    return curr
            

        return closest
      >

#Notes:
#Used two pointers approach
