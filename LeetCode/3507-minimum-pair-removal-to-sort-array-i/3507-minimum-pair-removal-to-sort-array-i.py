class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while any(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
            msum = float('inf')
            idx = 0
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < msum:   
                    msum = nums[i] + nums[i + 1]
                    idx = i
            nums[idx] = msum
            nums.pop(idx + 1)
            count += 1
        return count