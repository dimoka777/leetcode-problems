# Adobe Amazon Microso ft 
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for num in nums:
            if prev := cnt.get(num):
                ans += prev
            cnt[num] += 1
        return ans
