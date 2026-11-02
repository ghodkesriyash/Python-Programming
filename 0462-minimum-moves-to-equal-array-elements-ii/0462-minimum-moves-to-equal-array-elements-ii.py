class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = n // 2
        if n % 2 == 1:
            median = nums[mid]
        else:
            median = (nums[mid - 1] + nums[mid - 1]) // 2
        moves = sum(abs(x - median) for x in nums)
        return moves 