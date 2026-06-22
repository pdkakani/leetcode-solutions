import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append(((v,t)))
        
        heap = [(0, k)] # (dist, k)
        visited = {}

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited[node] = dist

            for nbr, t in adj[node]:
                if nbr not in visited:
                    heapq.heappush(heap, (dist + t, nbr))
        
        if len(visited) < n:
            return -1
        return max(visited.values())
