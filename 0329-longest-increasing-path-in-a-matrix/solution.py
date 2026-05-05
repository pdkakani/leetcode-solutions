class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        max_path = 0

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]
            
            best = 1
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[r][c]:
                        best = max(best, 1+ dfs(nr, nc))
            memo[r][c] = best
            return best
        
        for i in range(rows):
            for j in range(cols):
                max_path = max(max_path, dfs(i, j))

        return max_path

