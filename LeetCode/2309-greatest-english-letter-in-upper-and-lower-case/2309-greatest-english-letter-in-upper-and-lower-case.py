class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(s)
        low = "abcdefghijklmnopqrstuvwxyz"
        great = []
        for i in low:
            if i in seen and i.upper() in seen:
                great.append(i.upper())
        great = sorted(great)
        if great:
            return great[-1]
        else:
            return ""