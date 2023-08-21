# Microsoft
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.

 
# Example 1:

# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        max_res = -1
        for i in nums:
            if -(i) in s and max_res < abs(i):
                max_res = abs(i)
            else:
                s.add(i)
        return max_res 
