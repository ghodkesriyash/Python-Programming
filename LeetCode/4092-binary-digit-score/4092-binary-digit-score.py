class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def popcount(x: int) -> int:
            c = 0
            while x > 0:
                c += x & 1
                x >>= 1
            return c

        s1 = popcount(a)
        s2 = popcount(b)

        if s1 >= s2:
            return s1 * s2
        return s2 // s1