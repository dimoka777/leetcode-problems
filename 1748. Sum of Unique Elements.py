# Facebook Citi
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([num for num, v in Counter(nums).items() if v == 1])


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = {}
        result = 0
        for i in nums:
            if not unique.get(i, None) and unique.get(i) != 0:
                unique[i] = 1
                result += i
            else:
                unique[i] -= 1
                if unique[i] == 0:
                    result -= i
        return result
