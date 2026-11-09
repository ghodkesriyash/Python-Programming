class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        best = float('-inf')
        result = [-1, -1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j] and nums[i] + nums[j] == target:
                    prod = nums[i] * nums[j]
                    if prod > best:
                        best = prod
                        result = [i, j]
        return result