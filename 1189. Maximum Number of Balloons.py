# Tesla Microsoft Adobe
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:

# Input: text = "nlaebolko"
# Output: 1


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for c in text:
            if c in cnt:
                if c == 'l' or c == 'o':
                    cnt[c] += 0.5
                else:
                    cnt[c] += 1
            
        return int(min(cnt.values()))
