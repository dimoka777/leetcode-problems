# Goldman Sachs Google Oracle
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".


def remove_symbols(s):
    tmp = []
    for i in s:
        if i != '#':
            tmp.append(i)
        else:
            if len(tmp) > 0:
                tmp.pop()
    return tmp

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first = remove_symbols(s)
        second = remove_symbols(t)

        if len(first) != len(second):
            return False

        return first == second
