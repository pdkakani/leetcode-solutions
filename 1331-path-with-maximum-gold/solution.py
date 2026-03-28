class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        total_gold = 0
        
        
        
                
        def bt(r, c):
            #bound check
            if r<0 or r >= row or c<0 or c>=col: return 0

            #constraint check
            if grid[r][c] == 0:
                return 0
            
            temp = grid[r][c]
            grid[r][c] = 0

            gold = temp + max((bt(r-1, c),
            bt(r+1, c),
            bt(r, c-1),
            bt(r, c+1)))

            
            grid[r][c] = temp

            return gold
        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    total_gold = max(total_gold, bt(i,j))
        return total_gold



