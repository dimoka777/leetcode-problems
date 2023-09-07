# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        
        ans = curr
        for right in range(k, len(s)):
            if s[right - k] in vowels:
                curr -= 1
            if s[right] in vowels:
                curr += 1
            ans = max(ans, curr)
        return ans
