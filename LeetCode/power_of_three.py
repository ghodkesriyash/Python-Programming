"""
Question: Power of Three
Given an integer n, return True if it is a power of three, otherwise return False.
A number is a power of three if there exists an integer x such that n == 3^x.

Categories: Math | Recursion
"""

def isPowerOfThree(self, n: int) -> bool:
    """
    Approach: Iterative Division
    Keep dividing n by 3 as long as it is divisible.
    If we end up with 1, it means n was a power of three.
    """

    """ Powers of three are always positive """
    if n < 1:
        return False

    """ Divide by 3 until no longer divisible """
    while n % 3 == 0:
        n //= 3

    """ If reduced to 1, n was a power of three """
    return n == 1