# Amazon
# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

# Example 1:

# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = -1
        for k, v in cnt.items():
            if v > 1:
                continue
            res = max(res, k)
        return res
