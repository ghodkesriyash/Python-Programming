class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        lst = list(word)
        seen = set(word)
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in seen and i.upper() in seen:
                last_lower = max([x for x in range(len(lst)) if lst[x] == i])
                first_upper = lst.index(i.upper())
                if last_lower < first_upper:
                    count += 1
        return count