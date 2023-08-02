# Given an array nums of integers, return how many of them contain an even number of digits.
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for i in nums if len(str(i)) % 2 == 0])
