# Problem: Add Binary
# Problem Link: https://leetcode.com/problems/add-binary/description/?envType=problem-list-v2&envId=math
# Date: 5th Sept 2026
# Time taken to solve: 45 mins

#solution
<
lass Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = ""

        while i >= 0 or j >= 0:
            if i >= 0:
                x = int(a[i])
            else:
                x = 0

            if j >= 0:
                y = int(b[j])
            else:
                y = 0

            total = x + y + carry

            if total == 0:
                ans = "0" + ans
                carry = 0
            elif total == 1:
                ans = "1" + ans
                carry = 0
            elif total == 2:
                ans = "0" + ans
                carry = 1
            else:
                ans = "1" + ans
                carry = 1

            i -= 1
            j -= 1

        if carry:
            ans = "1" + ans

        return ans
        
      >
#Notes
#Added two binary strings using bit-by-bit addition with carry.
