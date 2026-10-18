# Problem: Fibonacci Numbers
# Problem Link: https://leetcode.com/problems/fibonacci-number/description/?envType=problem-list-v2&envId=math
# Date: 18th Oct 2026
# Time taken to solve: 15 mins

#solution
<
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b

        return a
>

#Notes
#Used an iterative approach, updating two variables to calculate each Fibonacci number until reaching F(n).
