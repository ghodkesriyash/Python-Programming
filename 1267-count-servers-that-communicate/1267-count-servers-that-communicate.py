class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        return count