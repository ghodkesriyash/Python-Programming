class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_chain = 0
        cur = 0
        for x in nums:
            if x:
                cur += 1
            else:
                max_chain = max(cur,max_chain)
                cur = 0
        return max(cur,max_chain)