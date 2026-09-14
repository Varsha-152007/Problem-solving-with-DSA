# Problem: Isomorphic Strings
# Problem Link: https://leetcode.com/problems/isomorphic-strings/description/?envType=problem-list-v2&envId=hash-table
# Date: 14th Sept 2026
# Time taken to solve: 15 min

#solution
<
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
      >
#Notes
#Used zip function to pair up corresponding characters from both strings.
