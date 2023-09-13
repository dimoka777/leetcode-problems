# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        ans = left = right = 0
        for right, v in enumerate(s):
            cnt[v] += 1
            while cnt[v] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
