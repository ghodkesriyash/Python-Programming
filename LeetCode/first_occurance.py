"""
Question: Find the Index of the First Occurrence in a String
Given two strings haystack and needle, return the index of the first
occurrence of needle in haystack, or -1 if needle is not found.

Categories: String | Two Pointers | Sliding Window
"""

def strStr(self, haystack: str, needle: str) -> int:
    """
    Approach: Sliding Window
    Slide a window of needle's length across haystack and compare
    each substring with needle until a match is found.
    """

    """ Empty needle is always found at index 0 """
    if needle == "":
        return 0
    
    """ Iterate only up to the point where needle can still fit """
    for i in range(len(haystack) - len(needle) + 1):

        """ Compare current window with needle """
        if haystack[i:i + len(needle)] == needle:
            return i
    
    return -1