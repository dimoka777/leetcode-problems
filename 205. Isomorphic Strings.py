# Apple Amazon Bolt
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 
# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        for first, second in zip(s, t):
            if (first not in s_t) and (second not in t_s):
                s_t[first] = second
                t_s[second] = first
            elif s_t.get(first) != second or t_s.get(second) != first:
                return False
        return True
