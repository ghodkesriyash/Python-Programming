class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        new = []
        n = len(nums)
        for i in range(0,n-1,2):
            new.append(int(str(int(nums[i])) + str(int(nums[i + 1]))))
        return min(new)
