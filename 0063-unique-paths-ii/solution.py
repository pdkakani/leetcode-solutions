class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}

        if obstacleGrid[0][0] == 1:
            return 0

        def grid(r, c):
            if r < 0 or c < 0:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0

            if r == 0 and c == 0:
                return 1

            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = grid(r - 1, c) + grid(r, c - 1)
            return dp[(r, c)]

        return grid(rows - 1, cols - 1)

        
            
            
                

        
