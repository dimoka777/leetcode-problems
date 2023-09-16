# Uber Google C3 IoT 
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 
# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = [0]
        for num in nums:
            pref.append(num + pref[-1])
        
        cnt = defaultdict(int)
        ans = 0
        for num in pref:
            ans += cnt[num]
            cnt[num + goal] += 1
        
        return ans
