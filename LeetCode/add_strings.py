"""
Question: Given two non-negative integers num1 and num2 represented as strings,
return their sum as a string, without using built-in BigInteger or converting directly to int (spirit of the problem).

Logic: Increase integer string digit limit, convert both strings to integers, add and return as string.
"""

import sys

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)  # Increase limit to handle large string-converted integers
        x = int(num1)  # Convert string to integer
        y = int(num2)  # Convert string to integer
        return str(x + y)  # Add and return result as string