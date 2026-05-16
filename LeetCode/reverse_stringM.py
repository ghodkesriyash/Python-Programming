"""
Question: Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], return 0.

Logic: Extract sign, reverse absolute value as string, reapply sign,
return result if within 32-bit bounds else return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1          # Preserve sign separately
        reversed_str = str(abs(x))[::-1]    # Reverse digits as string
        result = sign * int(reversed_str)   # Reapply sign to reversed number

        if -2**31 <= result <= 2**31 - 1:   # Check 32-bit integer bounds
            return result
        return 0