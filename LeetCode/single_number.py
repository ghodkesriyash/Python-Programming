"""
Question: Single Number
Given a non-empty array of integers, every element appears twice except for one.
Find and return that single element.

Categories: Array | Hash Table | Bit Manipulation
"""

def singleNumber(self, nums: List[int]) -> int:
    """
    Approach: Pop and Search
    Pop each element and check if it exists in the remaining list.
    If it does, remove that duplicate. If it does not, it is the single element.
    """

    while nums:
        """ Pop the last element and check if it exists elsewhere in the list """
        term = nums.pop()

        """ If duplicate found, remove it. Otherwise return the unique element """
        if term in nums:
            nums.remove(term)
        else:
            return term