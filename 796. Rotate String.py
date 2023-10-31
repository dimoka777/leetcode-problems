# Easy
# Apple Amazon Adobe
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
 
# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        queue = deque(list(s))
        goal = deque(goal)
        for i in range(len(s)):
            if queue == goal:
                return True
            else:
                left = queue.popleft()
                queue.append(left)
        return False
