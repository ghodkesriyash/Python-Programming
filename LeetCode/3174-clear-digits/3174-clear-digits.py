class Solution:
    def clearDigits(self, s: str) -> str:
        digits = ['1','2','3','4','5','6','7','8','9','0']
        stack = []
        for x in s:
            if x.isdigit():
                stack.pop()
            else:
                stack.append(x)
        
        return ''.join(stack)