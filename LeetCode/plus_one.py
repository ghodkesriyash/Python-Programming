"""
Question: Plus One
Given a large integer represented as an array of digits, increment the integer by one
and return the resulting array of digits.

Categories: Array | Math
"""

def plusOne(self, digits: List[int]) -> List[int]:
    """
    Approach: Reverse Traversal
    If the last digit is not 9, simply increment it.
    Otherwise, find the rightmost non-9 digit, increment it,
    and set all digits after it to 0.
    If all digits are 9, prepend 1 and set all digits to 0.
    """

    lambi = len(digits)

    """ Simple case: last digit is not 9, just increment and return """
    if digits[-1] != 9:
        digits[-1] = digits[-1] + 1
        return digits

    else:
        """ Find the rightmost non-9 digit """
        index = -1
        i = 1
        while i <= lambi:
            if digits[lambi - i] != 9:
                index = lambi - i
                break
            i += 1

        """ All digits were 9, prepend 1 and zero out all digits """
        if index == -1:
            return [1] + [0] * lambi

        """ Increment the rightmost non-9 digit """
        digits[index] += 1

        """ Set all digits after the incremented index to 0 """
        for x in range(index + 1, lambi):
            digits[x] = 0

        return digits