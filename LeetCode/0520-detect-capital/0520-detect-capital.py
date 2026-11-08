class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag = False
        if word == word.upper():
            flag = True
        elif word == word.lower():
            flag = True
        elif word[0] == word[0].upper() and word[1:] == word[1:].lower():
            flag = True
        return flag 