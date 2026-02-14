class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        copy = [row[:] for row in board]

        for i in range(m):
            for j in range(n):
                live = 0

                for di in [-1,0,1]:
                    for dj in [-1,0,1]:

                        if di ==0 and dj == 0:
                            continue
                        
                        ni = di + i
                        nj = dj + j

                        if ni < m and ni >= 0 and nj <n and nj >= 0:
                            if copy[ni][nj] == 1:
                                live += 1
        
                if copy[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1




