# Problem: Roman to Integer
# Problem Link: https://leetcode.com/problems/roman-to-integer/description/?envType=problem-list-v2&envId=hash-table
# Date: 31st Aug 2026 
# Time taken to solve: 30 mins

#solution
<
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        return sum(values[x] for x in s)
      >

#Notes:
#Roman to Integer using string replacement and value mapping.
