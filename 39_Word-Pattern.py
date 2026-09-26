# Problem: Word Pattern
# Problem Link: https://leetcode.com/problems/word-pattern/description/?envType=problem-list-v2&envId=string
# Date: 26th Sept 2026
# Time taken to solve: 45 min

#solution
<
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, word in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != word:
                return False

            if word in word_to_char and word_to_char[word] != c:
                return False

            char_to_word[c] = word
            word_to_char[word] = c

        return True
        
      >
#Notes
#Use two dictionaries to maintain a character-to-word and word-to-character mapping, ensuring a unique one-to-one relationship.
