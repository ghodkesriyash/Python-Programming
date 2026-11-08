class Solution:
    def isGood(self, nums: List[int]) -> bool:
            base = max(nums)
            if len(nums) == (base + 1):
                for i in range(1,base + 1):
                    if i not in nums:
                        return False
                    nums.remove(i)
                if nums[0] == base:
                    return True
                else:
                    return False
            else:
                return False
        