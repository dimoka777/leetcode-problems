# Amazon Apple Google
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        i1 = i2 = 0
        result = ''

        while w1 > i1 or w2 > i2:
            if w1 > i1:
                result += word1[i1]
                i1 += 1
            if w2 > i2:
                result += word2[i2]
                i2 += 1

        return result
