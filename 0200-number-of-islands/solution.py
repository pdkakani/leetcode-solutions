class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # check bounds
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return

            # check if its water cell
            if grid[r][c] != '1':
                return
            
            # sink the land cell
            grid[r][c] = '0'

            # check the nieghbours
            dfs(r - 1, c) # up
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right
            dfs(r + 1, c) # down
        
        # traverse from each cell
        for i in range(rows):
            for j in range(cols):
                # found island
                if grid[i][j] == '1':
                    dfs(i,j) # sink the whole island
                    count += 1 # count it once
        
        return count
        
