# Medium 
# Amazon Yandex Facebook
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.
 
# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = prefix = 0
        tmp = {0: 1}
        for num in nums:
            prefix += num

            if prefix - k in tmp:
                ans += tmp[prefix - k]

            if prefix not in tmp:
                tmp[prefix] = 1
            else:
                tmp[prefix] += 1
        return ans
