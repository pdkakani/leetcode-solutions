class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)] # max time/elevation on path, r, c

        visited = set()
        while heap:
            time, r, c = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            if (r, c) == (n-1,n-1):
                return time
            visited.add((r,c))
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = dr +r, dc + c
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                    heapq.heappush(heap, (max(grid[nr][nc], time), nr, nc))
        
        return -1
        
