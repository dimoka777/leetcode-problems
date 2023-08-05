# Given an integer array nums, return 0 if the sum of the digits of the minimum integer in nums is odd, or 1 otherwise.
#
# company
# Amazon
# Example 1:
#
# Input: nums = [34,23,1,24,75,33,54,8]
# Output: 0
# Explanation: The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.
from typing import List


class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        return 1 if sum([int(i) for i in str(min(nums))]) % 2 == 0 else 0