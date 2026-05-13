"""
Question: Remove Duplicates from Sorted Array
Given a sorted array, remove duplicates in-place such that each element
appears only once. Return the number of unique elements k.

Categories: Array | Two Pointers
"""

def removeDuplicates(self, nums: List[int]) -> int:
    """
    Approach: Two Pointers
    Use a slow pointer k to track the position of the next unique element.
    Fast pointer i scans through the array and copies unique elements forward.
    """

    """ k starts at 1 since the first element is always unique """
    k = 1
    
    for i in range(1, len(nums)):

        """ If current element differs from previous, it is unique """
        if nums[i] != nums[i - 1]:

            """ Place unique element at the next available position """
            nums[k] = nums[i]
            k += 1

    return k