class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            for length in range(1, n - i + 1):
                temp = nums[i:i + length]
                result += len(set(temp)) ** 2
        return result


            