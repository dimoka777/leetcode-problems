# Apple Amazon Bolt
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 
# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split(' ')
        if len(pattern) != len(lst):
            return False
            
        tmp = {}
        for p, val in zip(pattern, lst):
            p1 = p + '1'
            if tmp.get(val) and tmp[val] != p1 or tmp.get(p1) and tmp[p1] != val:
                return False
            elif not tmp.get(val):
                tmp[val] = p1
                tmp[p1] = val

        return True
