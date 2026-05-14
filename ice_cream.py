"""
Question: Given an array costs where costs[i] is the price of the ith ice cream bar,
and an integer coins representing the total coins available, return the maximum number
of ice cream bars you can buy with the given coins.

Logic: Sort costs in ascending order, greedily buy the cheapest bars first,
accumulate spend and stop when the next bar exceeds remaining budget.
"""

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs_sorted = sorted(costs)  # Sort to greedily pick cheapest first
        spent = 0
        count = 0
        for i in costs_sorted:
            if spent + i > coins:  # Stop if next purchase exceeds budget
                break
            spent += i
            count += 1
        return count