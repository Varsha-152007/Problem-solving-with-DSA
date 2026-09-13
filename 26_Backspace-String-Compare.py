# Problem: Backspace String Compare
# Problem Link: https://leetcode.com/problems/backspace-string-compare/description/?envType=problem-list-v2&envId=stack
# Date: 13th Sept 2026
# Time taken to solve: 40 min

#solution
<
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(text):
            stack = []
            for ch in text:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

            return ''.join(stack)
        return process(s) == process(t)
      >
#Notes
#Used stack to simulate backspaces, then compare the final strings after processing both inputs.
