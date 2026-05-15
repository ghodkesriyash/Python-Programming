"""
Question: Given a number represented as string num and an integer t, find the smallest
number >= num such that the product of its digits is divisible by t.
Return the result as a string, or "-1" if impossible.

Logic: Factorize t into primes (2,3,5,7) — if any other prime factor exists return -1.
Track required prime counts, then greedily assign the smallest possible digits
from left to right. If no valid number exists with same length, extend the length.
Use precomputed base factorizations per digit to efficiently update prime counts.
"""

bases = [[], [], [2], [3], [2,2], [5], [2,3], [7], [2,2,2], [3,3]]  # Prime factors of digits 0-9
primes = (2, 3, 5, 7)

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        count = [0] * 10  # Tracks required count of each prime factor
        for p in primes:
            while t % p == 0:
                count[p] += 1  # Decompose t into prime factors
                t = t // p
        if t != 1: return "-1"  # t has a prime factor outside (2,3,5,7), impossible

        res = [int(ch) for ch in num]  # Work with digit list for easy mutation

        def inc(v, added):
            for p in bases[v]: count[p] += added  # Add/remove prime contributions of digit v

        def getn():
            """
            Compute minimum additional digits needed to satisfy remaining prime requirements.
            Prioritizes using digit 9(3^2), 8(2^3), 7, 5 to minimize digit count.
            """
            n2, n3, n5, n7 = [max(count[p], 0) for p in primes]
            n = n3 // 2 + n5 + n7  # Digits needed for 3s(via 9), 5s, 7s
            if n3 % 2 == 1:
                n, n2 = n + 1, n2 - 1  # Odd 3 leftover handled by digit 3, frees a factor of 2
            return n + (n2 + 2) // 3  # Remaining 2s handled via digits 8(2^3)

        last = len(res)
        for i, v in enumerate(res):
            if v == 0:
                last = i  # Track last non-zero digit position
                break
            inc(v, -1)  # Subtract prime contributions of existing digits

        def fill(start):
            for i in range(start, len(res)):
                for j in range(1, 10):
                    inc(j, -1)
                    if getn() <= len(res) - 1 - i:  # Check if remaining digits can fulfill requirement
                        res[i] = j
                        break
                    inc(j, 1)
            return ''.join(str(v) for v in res)

        if getn() <= len(res) - last: return fill(last)  # Current length is sufficient

        for i in range(last - 1, -1, -1):  # Try incrementing earlier digits
            inc(res[i], 1)
            for j in range(res[i] + 1, 10):
                inc(j, -1)
                if getn() <= len(res) - 1 - i:
                    res[i] = j
                    return fill(i + 1)
                inc(j, 1)

        res.append(0)  # Must extend number length
        nx = getn()
        while len(res) < nx: res.append(0)  # Pad to minimum required length
        return fill(0)