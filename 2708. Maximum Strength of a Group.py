# You are given a 0-indexed integer array nums representing the score of students in an exam.
# The teacher would like to form one non-empty group of students with maximal strength,
# where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as
# nums[i0] * nums[i1] * nums[i2] * ... * nums[ik].
#
# Return the maximum strength of a group the teacher can create.
#
# Example 1:
#
# Input: nums = [3,-1,-5,2,5,-9]
# Output: 1350
# Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5].
# Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = None
        neg = []
        for i in nums:
            if i > 0:
                if res:
                    res *= i
                else:
                    res = i
            elif i < 0:
                neg.append(i)

        neg.sort()
        if len(neg) % 2 != 0:
            neg = neg[:-1]

        for i in neg:
            if res:
                res *= i
            else:
                res = i

        return res if res else 0