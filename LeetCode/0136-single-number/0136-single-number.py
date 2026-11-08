class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while nums:
            term = nums.pop()
            if term in nums:
                nums.remove(term)
            else:
                return term
            
