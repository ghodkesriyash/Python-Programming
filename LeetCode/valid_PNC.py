"""
Question: Given a 0-indexed integer array nums, return true if it is a good array.
A good array is defined as one that contains [1, 2, ..., n, n] for some positive integer n,
i.e., all integers from 1 to n exactly once, and n appears exactly twice.

Logic: Find max as base n, verify length is n+1, check all integers 1 to n exist
and remove them one by one, then confirm the remaining element is n.
"""

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base = max(nums)  # n is the maximum element
        if len(nums) == (base + 1):  # Good array must have exactly n+1 elements
            for i in range(1, base + 1):
                if i not in nums:  # Every integer from 1 to n must be present
                    return False
                nums.remove(i)  # Remove each verified integer
            if nums[0] == base:  # Only remaining element must be the duplicate n
                return True
            else:
                return False
        else:
            return False