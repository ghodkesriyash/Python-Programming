class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        seen = set(word)
        low = "abcdefghijklmnopqrstuvwxyz"
        for i in low:
            if i in seen and i.upper() in seen:
                count += 1
        return count
