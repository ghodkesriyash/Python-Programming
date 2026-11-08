class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(n) for n in nums]
        nums.sort(reverse = True)
        mid = int((len(nums) + 1) // 2)
        left = nums[:mid]
        right = nums[mid:]
        result = 0
        for x in left:
            result += x * x
        for x in right:
            result -= x * x
        return result
