# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign represents its direction
# (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if not stack or (stack[-1] < 0 and i < 0) or (stack[-1] > 0 and i > 0) or (stack[-1] < 0 and i > 0):
                stack.append(i)
            else:
                equal = None
                while stack and (not (stack[-1] < 0 and i < 0) and not (stack[-1] > 0 and i > 0)):
                    if (abs(i) > abs(stack[-1])):
                        stack.pop()
                        equal = False
                    else:
                        if (abs(i) == abs(stack[-1])):
                            stack.pop()
                        equal = True
                        break

                if equal == False:
                    stack.append(i)
        return stack
