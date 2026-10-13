class Solution:
    def jump(self, nums: list[int]) -> int:
        count = 0
        cur_end = 0     
        farthest = 0     

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:       
                count += 1
                cur_end = farthest
        return count