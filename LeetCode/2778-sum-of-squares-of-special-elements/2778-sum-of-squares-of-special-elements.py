class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        size = len(nums)

        for x in range(size):
            if size % (x + 1) == 0: #here the array is 1 index
                result += nums[x] * nums[x]
        return result