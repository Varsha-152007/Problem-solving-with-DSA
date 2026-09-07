# Problem: Length of Last Word
# Problem Link: https://leetcode.com/problems/length-of-last-word/description/
# Date: 7th Sept 2026
# Time taken to solve: 2 min

#solution
<
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
      >
#Notes
#Used split function to recognize the last word of a sentence
