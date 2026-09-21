# Problem: Count Prime
# Problem Link:https://leetcode.com/problems/count-primes/submissions/2148904041/?envType=problem-list-v2&envId=array
# Date: 21st Sept 2026
# Time taken to solve: 30 min

#solution
<
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0

        for num in range(2, n):
            prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break

            if prime:
                count += 1

        return count
      >
