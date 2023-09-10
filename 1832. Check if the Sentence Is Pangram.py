# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        cnt = 0
        for i in sentence:
            if not d.get(i):
                cnt += 1
                d[i] = 1
        return True if cnt == 26 else False
