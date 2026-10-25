# Problem: Simplify Path
# Problem Link: https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=string
# Date: 25th Oct 2026
# Time taken to solve: 30 mins

#solution
<
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)
>

#Note
#Split the path by /, use a stack to ignore . and empty parts, pop for .., and push valid directory names before joining them into the canonical path.
