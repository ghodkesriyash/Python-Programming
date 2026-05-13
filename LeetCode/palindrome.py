"""
Question: Palindrome Number
Given an integer x, return True if x is a palindrome and False otherwise.
A palindrome reads the same forwards and backwards.

Categories: Math | String
"""

def isPalindrome(self, x: int) -> bool:
    """
    Approach: String Conversion and Reverse Comparison
    Convert the integer to a string, reverse it, and compare with original.
    Negative numbers are never palindromes.
    """

    """ Negative numbers cannot be palindromes """
    if x < 0:
        return False

    """ Convert integer to list of characters """
    x = str(x)
    l = list(x)

    """ Compare list with its reverse """
    if (l == l[::-1]):
        return True
    else:
        return False