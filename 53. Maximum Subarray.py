# Amazon Microsoft Adobe
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tmp = 0
        for val in nums:
            tmp = max(tmp, 0) + val
            res = max(tmp, res)
        return res
