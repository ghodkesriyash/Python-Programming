class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        rows = len(grid)
        columns = len(grid[0])
        pos = [0,0]
        seen = set()
        while 0 <= pos[0] < rows and 0 <= pos[1] < columns and tuple(pos) not in seen:
            last = pos[:]
            seen.add((pos[0],pos[1]))
            if grid[pos[0]][pos[1]] == "L":
                pos[1] -= 1
            elif grid[pos[0]][pos[1]] == "R":
                pos[1] += 1
            elif grid[pos[0]][pos[1]] == "U":
                pos[0] -= 1
            elif grid[pos[0]][pos[1]] == "D":
                pos[0] += 1
        return last

