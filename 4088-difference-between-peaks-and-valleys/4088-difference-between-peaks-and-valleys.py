class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peaks = 0
        valleys = 0
        for x in range(1,len(nums) - 1):
            if nums[x-1]< nums[x] and nums[x] > nums[x+1]:
                peaks += nums[x]
            elif nums[x-1] > nums[x] and nums[x] < nums[x+1]:
                valleys += nums[x]
        return peaks - valleys