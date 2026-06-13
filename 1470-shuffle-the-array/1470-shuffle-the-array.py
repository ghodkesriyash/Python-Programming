class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        f = []
        for i in range(n):
            f.append(nums[i]) 
            f.append(nums[i + n])
        return f