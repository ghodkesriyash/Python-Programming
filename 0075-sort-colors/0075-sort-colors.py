class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_idx = i + nums[i:].index(min(nums[i:]))  
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        
        