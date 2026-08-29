# Problem: Group Anagrams
# Problem Link: https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=array
# Date: 29th Aug 2026 
# Time taken to solve: 45 mins

#solution
<
Class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []
            

            groups[key].append(s)

        return list(groups.values())
      >

#Notes:
#Solved using Python dictionary.
