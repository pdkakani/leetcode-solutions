class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # minimum spanning tree

        visited = set()
        heap = [(0,0)]
        n = len(points)
        total = 0
        while heap and len(visited) < n:
            cost, pIndex = heapq.heappop(heap)
            if pIndex in visited:
                continue
            visited.add(pIndex)
            total += cost

            for j in range(n):
                if j not in visited:
                    temp_cost = get_dist(points[pIndex], points[j])
                    heapq.heappush(heap, (temp_cost, j))
        return total
