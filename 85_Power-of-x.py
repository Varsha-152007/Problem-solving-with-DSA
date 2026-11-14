# Problem: Pow(x, n)
# Problem Link: https://leetcode.com/problems/powx-n/description/?envType=problem-list-v2&envId=math
# Date: 14th Nov 2026
# Time taken to solve: 45mins

#solution
<
class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        n = abs(n)

        result = 1

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        if negative:
            result = 1 / result

        return result
>
#Notes
#Calculate power using binary exponentiation and, if the exponent is negative, take the reciprocal of the final result.
