# Problem: Intersection Of Two Arrays II
# Problem Link:https:/https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=problem-list-v2&envId=array
# Date: 23rd Sept 2026
# Time taken to solve: 35 min

#solution
<
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = {}
        result = []
    
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1


        for num in nums2:
            if freq.get(num, 0) > 0:
                result.append(num)
                freq[num] -= 1

        return result
      >
#Notes
#Used a frequency map to count elements in nums1 and find their matching occurrences in nums2.
