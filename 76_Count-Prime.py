# Problem: Count Primes
# Problem Link: https://leetcode.com/problems/count-primes/description/?envType=problem-list-v2&envId=math
# Date: 5th Nov 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False

        return sum(prime)
>
