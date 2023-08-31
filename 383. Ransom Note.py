# Facebook Amazon Adobe
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(magazine)
        for i in ransomNote:
            if cnt.get(i, None) is None or (cnt[i] - 1) < 0:
                return False
            cnt[i] -= 1
        return True
