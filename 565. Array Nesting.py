# You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].
#
# You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:
#
# The first element in s[k] starts with the selection of the element nums[k] of index = k.
# The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
# We stop adding right before a duplicate element occurs in s[k].
# Return the longest length of a set s[k].
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        s = set()
        for i, v in enumerate(nums):
            cnt = 0
            while v not in s:
                cnt += 1
                s.add(v)
                v = nums[v]
            if res < cnt:
                res = cnt
        return res