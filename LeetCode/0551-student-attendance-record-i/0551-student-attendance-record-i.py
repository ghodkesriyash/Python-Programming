class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for i in s:
            if i == "A":
                count += 1
        if count >= 2:
            return False
        if "LLL" in s:
            return False
        return True