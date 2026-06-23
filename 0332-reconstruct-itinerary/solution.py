class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for f, t in sorted(tickets, reverse = True):
            adj[f].append(t)
        
        res = []
        
        def dfs(airport):
            while adj[airport]:
                next_ap = adj[airport].pop()
                dfs(next_ap)
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]
        
