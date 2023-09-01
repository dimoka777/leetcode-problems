# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        for right in range(ln):
            if nums[right] >= 0:
                break
        
        left = right - 1
        res = []
        while right < ln or left >= 0:
            if left >= 0 and right < ln:
                if abs(nums[left]) > nums[right]:
                    res.append(nums[right]**2)
                    right += 1
                else:
                    res.append(nums[left]**2)
                    left -= 1
            elif left >= 0:
                res.append(nums[left]**2)
                left -= 1
            elif right < ln:
                res.append(nums[right]**2)
                right += 1
        return res
