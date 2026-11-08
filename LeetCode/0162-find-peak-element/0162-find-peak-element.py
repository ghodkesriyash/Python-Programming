class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = nums[i-1] if i > 0 else float(-inf)
            right = nums[i+1] if i < len(nums) - 1 else float(-inf)

            if left < nums[i] and nums[i] > right:
                return i
            
        