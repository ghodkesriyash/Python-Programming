class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(' : ')', '{' : '}', '[' : ']'}
        for x in range(len(s)):
            if(s[x] in '({['):
                stack.append(s[x])
            else:
                if not stack or pairs[stack.pop()] != s[x]:  
                    return False
        return len(stack)==0