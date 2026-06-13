class Solution:
    def isHappy(self, n: int, seen=None) -> bool:
        if seen is None:
            seen = set()
        if n == 1:
            return True
        if n in seen:
            return False
        seen.add(n)
        new = sum(int(i) ** 2 for i in str(n))
        return self.isHappy(new, seen)
            
