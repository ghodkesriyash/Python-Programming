class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count = 0
        new = ""
        for x in range(0,len(s),k):
            if count % 2 == 0:
                new += s[x:x + k][::-1]
            else:
                new += s[x:x + k]    
            count += 1
        return new
        