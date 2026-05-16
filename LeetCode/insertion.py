"""
Question: Given a sorted array of distinct integers and a target value, return the
index if the target is found. If not, return the index where it would be inserted
in order to keep the array sorted.

Logic: If target exists return its index directly, otherwise count how many
elements are smaller than target to determine the insertion position.
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        count = 0
        if target in nums:
            return nums.index(target)  # Return index if target exists
        else:
            for i in nums:
                if target > i:
                    count += 1  # Count elements smaller than target
                else:
                    break       # Stop at first element greater than target
            return count        # Count equals the insertion index