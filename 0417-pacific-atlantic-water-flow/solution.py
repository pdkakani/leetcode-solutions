class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def bfs(borders):
            visited = set(borders)
            queue = deque(borders)

            while queue:
                r, c = queue.popleft()

                for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)]:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in visited:
                        continue
                    if 0 > nr or nr >= rows or 0 > nc or nc >= cols:
                        continue
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr,nc))
            return visited
        
        # top row + left most col
        pac = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        # bottom row + right most col
        atl = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        return list(bfs(pac) & bfs(atl))

        
