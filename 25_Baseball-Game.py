# Problem: Baseball Game
# Problem Link: https://leetcode.com/problems/baseball-game/description/?envType=problem-list-v2&envId=stack
# Date: 12th Sept 2026
# Time taken to solve: 25 min

#solution
<
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
      >
#Notes
#Used a stack to efficiently track scores and handle +, D, and C operations.
