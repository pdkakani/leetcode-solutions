class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #validate rows
        for i in range(9):
            valid = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in valid:
                        return False
                    valid.add(board[i][j])
        
        # Validate columns
        for j in range(9):
            valid = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in valid:
                        return False
                    valid.add(board[i][j])

        #validate boxes
    
        for box_row in range(0, len(board), 3):
            for box_col in range(0, len(board), 3):
                box_set = set()
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] not in box_set:
                            if board[i][j] != ".":
                                box_set.add(board[i][j])
                        else:
                            return False

        return True
