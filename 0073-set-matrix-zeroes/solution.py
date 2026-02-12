class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_pos = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = matrix[i][j]
                if num == 0:
                    zero_pos.append([i, j])

        
        for k in range(len(zero_pos)):
            for l in range(len(zero_pos[0]) - 1):
                row = zero_pos[k][l]
                col = zero_pos[k][l+1]
                
                matrix[row] = [0] * len(matrix[0])
                for m in range(len(matrix)):
                    matrix[m][col] = 0

