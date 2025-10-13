class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate the rows
        for i in range(9):
            set1 = set()
            for j in range(9):
                if board[i][j] in set1:
                    return False
                if board[i][j] != ".":
                    set1.add(board[i][j])

        # Validate the columns
        for i in range(9):
            set1 = set()
            for j in range(9):
                if board[j][i] in set1:
                    return False
                if board[j][i] != ".":
                    set1.add(board[j][i])
        # Validate the boxes
        starts = [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3), (6,6)]

        for i, j in starts:
            set1 = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in set1:
                        return False
                    if item != ".":
                        set1.add(item)
        return True
        
