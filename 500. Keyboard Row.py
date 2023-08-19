# MathWorks
# Given an array of strings words, return the words that can be typed using letters 
# of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
 
# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        al = {}
        res = []
        def fill_alphabet(s, row):
            for i in s:
                al[i] = row
        
        fill_alphabet("qwertyuiop", 1)
        fill_alphabet("asdfghjkl", 2)
        fill_alphabet("zxcvbnm", 3)

        for word in words:
            row = al.get(word[0].lower())
            for c in word.lower():
                if al.get(c) != row:
                    break
            else:
                res.append(word)
        return res
