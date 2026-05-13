"""
Question: Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
Return an empty string if there is no common prefix.

Categories: String | Trie
"""

def longestCommonPrefix(self, strs: List[str]) -> str:
    """
    Approach: Vertical Scanning
    Find the length of the shortest string to set the scan boundary.
    Scan character by character across all strings simultaneously.
    Stop and return the prefix built so far as soon as a mismatch is found.
    """

    pre = ""
    x = 0

    """ Find the length of the shortest string to avoid index out of bounds """
    mini = 200
    for i in strs:
        if len(i) < mini:
            mini = len(i)

    while x < mini:
        """ Take the current character from the first string as reference """
        curr = strs[0][x]

        """ Compare current character across all strings """
        for i in strs:
            if i[x] != curr:
                return pre

        """ All strings matched at this position, add to prefix """
        pre += curr
        x += 1

    return pre