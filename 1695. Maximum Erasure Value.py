# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 
# Example 1:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pref = []
        cnt = set()
        ans = left = 0
        for right in range(len(nums)):
            pref.append(nums[right] + pref[-1] if len(pref) else nums[right])
            while nums[right] in cnt:
                cnt.discard(nums[left])
                left += 1
            cnt.add(nums[right])
            ans = max(ans, pref[right] - pref[left] + nums[left])
        return ans
