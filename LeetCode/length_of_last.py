"""
Question: Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word.

Categories: String
"""

def lengthOfLastWord(self, s: str) -> int:
    """
    Approach: Built-in Split
    Split the string by whitespace and return the length of the last element.
    split() automatically handles leading, trailing, and multiple spaces.
    """

    """ Split string into list of words """
    l = s.split()

    """ Return length of the last word """
    return len(l[-1])