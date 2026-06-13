class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        total = 0
        for x in range(len(cost)):
            if (x + 1)% 3 == 0:
                continue
            total += cost[x]
        return total