# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
# Example 1:

# Input: x = 123
# Output: 321


class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        x = abs(x)
        num = 0
        while x:
            num *= 10
            num += x % 10
            x //= 10
            
        num *= neg
        if (-2 ** 31) <= num <= (2 ** 31 - 1):
            return num
        return 0
