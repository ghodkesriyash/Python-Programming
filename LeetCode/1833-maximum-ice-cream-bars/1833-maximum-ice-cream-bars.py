class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs_sorted = sorted(costs)
        spent = 0
        count = 0
        for i in costs_sorted:
            if spent + i > coins:  # Stop if next purchase exceeds budget
                break
            spent += i
            count += 1
        return count