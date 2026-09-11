# Problem: Intersection of two arrays
# Problem Link: https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=sorting
# Date: 11th Sept 2026
# Time taken to solve: 15 min

#solution
<
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = set()

        for num in nums2:
            if num in set1:
                result.add(num)

        return list(result)
      >
#Notes
#HashSet based solution for array intersection
