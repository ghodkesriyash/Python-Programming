class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lambi = len(digits)
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            index = -1
            i = 1
            while i <= lambi:
                if digits[lambi - i] != 9:     
                    index = lambi - i           
                    break                       
                i += 1
            
            if index == -1:                     
                return [1] + [0] * lambi
            
            digits[index] += 1                  
            for x in range(index + 1, lambi):   
                digits[x] = 0
            return digits





        