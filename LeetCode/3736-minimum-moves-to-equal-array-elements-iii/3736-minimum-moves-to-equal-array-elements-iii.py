class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = max(nums)* len(nums) - sum(nums) 
        return moves