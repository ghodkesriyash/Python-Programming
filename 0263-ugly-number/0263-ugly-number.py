class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        
        remaining = [x for x in factors if x not in (2, 3, 5)]
        return len(remaining) == 0