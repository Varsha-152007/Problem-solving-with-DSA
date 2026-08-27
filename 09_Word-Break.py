# Problem: Word Break
# Problem Link: https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=array
# Date: 27th Aug 2026 
# Time taken to solve: 50 mins

#solution
<
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
    
        return dp[n]
      >

#Notes:
#Trying all possible word combinations recursively
