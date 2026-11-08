class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        roman = {'I':1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            temp = roman[s[i]]
            temp1 = roman[s[i+1]] if i+1 < len(s) else 0

            if temp < temp1:
                num -= temp
            else:
                num += temp
    
        return num
        
            