"""
Question: Write a function that reverses a string. The input string is given as
an array of characters s. You must do this by modifying the input array in-place
with O(1) extra memory.

Logic: Use two pointers starting at opposite ends, swap characters and move
pointers inward until they meet at the center.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1  # Initialize two pointers at opposite ends

        while start <= end:
            s[start], s[end] = s[end], s[start]  # Swap characters in-place
            start += 1  # Move left pointer inward
            end -= 1    # Move right pointer inward