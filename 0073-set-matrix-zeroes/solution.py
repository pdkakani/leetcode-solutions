class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_pos = []

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_pos.append([i,j])

        for row, col in zero_pos:
            matrix[row] = [0] * cols
            for m in range(rows):
                matrix[m][col] = 0
