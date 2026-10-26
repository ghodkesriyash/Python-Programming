class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for x in moves:
            if x == "R":
                pos[0] += 1
            elif x == "L":
                pos[0] -= 1
            elif x == "U":
                pos[1] += 1
            else:
                pos[1] -= 1
        return (pos[0] == 0 and pos[1] == 0)