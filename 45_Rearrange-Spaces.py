# Problem: Rearrange Spaces Between Words
# Problem Link: https://leetcode.com/problems/rearrange-spaces-between-words/description/
# Date: 3rd Oct 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()

        if len(words) == 1:
            return words[0] + ' ' * spaces

        between = spaces // (len(words) - 1)
        extra = spaces % (len(words) - 1)

        return (' ' * between).join(words) + ' ' * extra
      >

#Notes:
#Count the spaces, split into words, evenly distribute spaces between words, and append any remaining spaces at the end.
