"""
Question: Valid Palindrome
Given a string s, return True if it is a palindrome after converting all uppercase
letters to lowercase and removing all non-alphanumeric characters.

Categories: String | Two Pointers
"""

def isPalindrome(self, s: str) -> bool:
    """
    Approach: Filter and Compare
    Strip all non-alphanumeric characters, convert to lowercase,
    then compare the string with its reverse.
    """

    flag = False
    alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"

    """ Filter out non-alphanumeric characters and convert to lowercase """
    temp = [i for i in s.lower() if i in alphanumeric]

    """ Join filtered characters into a clean string """
    s1 = "".join(temp)

    """ Reverse the filtered list and join into a string """
    rev = temp[::-1]
    s2 = "".join(rev)

    """ Compare original cleaned string with its reverse """
    if s1 == s2 or s == " ":
        flag = True

    return flag