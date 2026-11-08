class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        out = []
        nums.sort()
        for x in range(len(nums)):
            if nums[x] == target:
                out.append(x)
        return out 
