class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        total_non_obs_cells = 0
        start_r, start_c = 0, 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != -1:
                    total_non_obs_cells += 1
                if grid[i][j] == 1:
                    start_r, start_c = i, j

        def bt(r,c, visited_count):
            #bounds check
            if r<0 or r>= row or c<0 or c>= col: return 0

            #constraint check
            if grid[r][c] == -1:
                return 0
            if grid[r][c] == "#":
                return 0

            #Reached end
            if grid[r][c] == 2:
                return 1 if visited_count == total_non_obs_cells else 0
            
        
            tmp = grid[r][c]
            grid[r][c] = "#"
            
            count = (bt(r+1, c, visited_count+1) +
            bt(r-1, c, visited_count+1) +
            bt(r, c+1, visited_count+1) +
            bt(r, c-1, visited_count+1))

                
            grid[r][c] = tmp
            return count

        return bt(start_r, start_c, 1)
    
