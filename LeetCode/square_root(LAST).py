"""
Question: Given a non-negative integer x, return the square root of x rounded
down to the nearest integer. The returned integer should be non-negative and
you may not use any built-in exponent function or operator.

Logic: Binary search between 1 and x, narrow range by comparing mid squared
to x. When no exact match found, right pointer holds the floor of the square root.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0  # Edge case
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid          # Exact square root found
            elif mid * mid < x:
                left = mid + 1      # Search right half
            else:
                right = mid - 1     # Search left half
        return right                # Floor of square root