class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        
        rem = []
        while num > 0:
            temp = num % 7
            rem.append(temp)
            num = num // 7
        
        rem.reverse()
        result = "".join(str(x) for x in rem)
        
        if negative:
            return "-" + result
        return result