from functools import cache

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @cache
        def best(left, right):
            if left == right:
                return piles[left]
            return max(
                piles[left] - best(left + 1, right),
                piles[right] - best(left, right - 1),
            )

        return best(0, len(piles) - 1) > 0