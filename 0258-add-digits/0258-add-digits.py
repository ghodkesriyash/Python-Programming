class Solution:
    def addDigits(self, num: int) -> int:
        result = 0
        if num < 10:
            return num
        for x in str(num):
            result += int(x)
        return self.addDigits(result)
