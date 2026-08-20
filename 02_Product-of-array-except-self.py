# Problem: Product of Array Except Self
# Problem Link: https://leetcode.com/problems/product-of-array-except-self/submissions/2113609413/
# Date: 20th Aug 2026
# Time taken to solve: 45 mins

#solution
<
class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        p=[1]*n

        l_p=1
        for i in range(n):
            p[i]=l_p
            l_p*=nums[i]

        r_p=1
        for i in range(n-1,-1,-1):
            p[i]*=r_p
            r_p*=nums[i]

        return p 
      >

#Notes:
#Used prefix ans suffix product approach
