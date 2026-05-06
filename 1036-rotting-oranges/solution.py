class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(1,0),(-1,0), (0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr,nc))
            res += 1
        
        return res if fresh == 0 else -1
        
