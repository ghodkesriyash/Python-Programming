class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if target > i:
                    count += 1
                else:
                    break
            return count