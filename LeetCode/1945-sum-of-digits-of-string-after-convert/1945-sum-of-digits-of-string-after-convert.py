import string
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = "".join(str(ord(x) - ord('a') + 1) for x in s)
        for i in range(k):
            final = sum(int(x) for x in temp)
            temp = str(final)
        return final

        

        