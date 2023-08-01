from collections import defaultdict


# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal,
# otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed)
# such that i != j and swapping the characters at s[i] and s[j].
#
# 	For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        tmp = defaultdict(int)
        if s == goal:
            for i in s:
                tmp[i] += 1
                if tmp[i] > 1:
                    return True
            return False

        a = b = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if a == -1:
                    a = i
                elif b == -1:
                    b = i
                else:
                    return False

        return s[a] == goal[b] and s[b] == goal[a]