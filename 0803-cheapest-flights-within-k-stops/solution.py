class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for f, t, p in flights:
            adj[f].append((p, t))
        
        heap = [(0, src, 0)]
        visited = {}

        while heap:
            price, node, count = heapq.heappop(heap)
            if node in visited and visited[node] < count:
                continue
            visited[node] = count
            if node == dst:
                return price
            if count <= k:
                for nbr in adj[node]:
                    curr_p, s = nbr 
                    heapq.heappush(heap, (price + curr_p, s, count + 1))
        
        return -1

