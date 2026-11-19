# Problem: Decode Ways
# Problem Link: https://leetcode.com/problems/decode-ways/description/
# Date: 19th Nov 2026
# Time taken to solve: 1hr 15mins

#solution
<
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):

            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if i >= 2:
                num = int(s[i - 2:i])

                if 10 <= num <= 26:
                    dp[i] += dp[i - 2]

        return dp[n]
      >
