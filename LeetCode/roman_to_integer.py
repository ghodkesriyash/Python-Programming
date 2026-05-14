"""
Question: Roman to Integer
Given a roman numeral string, convert it to an integer.
Roman numerals use subtractive notation where a smaller value
preceding a larger value is subtracted instead of added.

Categories: String | Hash Table | Math
"""

def romanToInt(self, s: str) -> int:
    """
    Approach: Left to Right Traversal with Lookahead
    Map each roman character to its integer value.
    If the current value is less than the next value, subtract it.
    Otherwise add it. This handles subtractive notation naturally.
    """

    num = 0
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    for i in range(len(s)):

        """ Get value of current and next roman character """
        temp = roman[s[i]]
        temp1 = roman[s[i+1]] if i+1 < len(s) else 0

        """ Subtract if current value is less than next, otherwise add """
        if temp < temp1:
            num -= temp
        else:
            num += temp

    return num