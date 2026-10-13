import heapq

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = [n * n for n in nums]
        k = (len(sq) + 1) // 2
        top = heapq.nlargest(k, sq)
        return 2 * sum(top) - sum(sq)

        #not my code trying AI solution 