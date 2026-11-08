class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows = len(board)
        cols = len(board[0])
        temp = [[0] * cols for _ in range(rows)]
        for x in range(rows):
            for y in range(cols):
                count = 0
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2  ):
                        if (i == x and j == y):
                            continue
                        if(0 <= i < rows and 0 <= j < cols):
                            if(board[i][j] == 1):
                                count += 1
                if (count < 2 and board[x][y] == 1):
                    temp[x][y] = 0
                if (2 <= count <= 3 and board[x][y] == 1):
                    temp[x][y] = 1
                if (count > 3 and board[x][y] == 1):
                    temp[x][y] = 0
                if (count == 3 and board[x][y] == 0):
                    temp[x][y] = 1
        for x in range(rows):
            for y in range(cols):
                board[x][y] = temp[x][y]