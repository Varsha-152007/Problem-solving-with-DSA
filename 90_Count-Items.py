# Problem: Count Items Matching a Rule
# Problem Link: https://leetcode.com/problems/count-items-matching-a-rule/description/?envType=problem-list-v2&envId=array
# Date: 21st Nov 2026
# Time taken to solve: 35mins

#solution
<
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        index = {"type": 0, "color": 1, "name": 2}

        count = 0

        for item in items:
            if item[index[ruleKey]] == ruleValue:
                count += 1

        return count
      >
