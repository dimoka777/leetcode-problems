# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.

# Return s after reversing it.
 
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        right = len(s) - 1
        left = 0
        while left < right:
            if not (65 <= ord(s[left]) <= 90) and not (97 <= ord(s[left]) <= 122):
                left += 1
            elif not (65 <= ord(s[right]) <= 90) and not (97 <= ord(s[right]) <= 122):
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
