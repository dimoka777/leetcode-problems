# Apple Oracle Microsoft
# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        cnt = Counter(arr)
        for num, val in cnt.items():
            if num == val:
                ans = max(ans, num)
        return ans
