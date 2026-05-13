"""
Question: Two Sum
Given an array of integers and a target, return the indices of the two numbers
that add up to the target.

Categories: Array | Hash Table
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Approach: Brute Force
    Check every pair of elements to find the two that sum to target.
    """

    for i in range(len(nums)):

        """ For each element, check all elements after it """
        for j in range(i + 1, len(nums)):

            """ Return indices if the pair sums to target """
            if (nums[i] + nums[j] == target):
                return [i, j]