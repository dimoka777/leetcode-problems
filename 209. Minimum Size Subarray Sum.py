# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.
# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0
        ans = float('inf')
        for right, val in enumerate(nums):
            curr += val
            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1

        return ans if ans != float('inf') else 0
