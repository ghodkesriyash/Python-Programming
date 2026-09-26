class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b))
        a = a.zfill(l)
        b = b.zfill(l)
        
        result = []
        for i in range(l):
            result.append(int(a[l - 1 - i]) + int(b[l - 1 - i]))
        
        result.append(0)  # extra slot in case of final carry
        
        for i in range(l):
            if result[i] >= 2:
                result[i] -= 2
                result[i + 1] += 1
        
        if result[-1] == 0:
            result.pop()
        
        result.reverse()
        return "".join(str(d) for d in result)
                
            
