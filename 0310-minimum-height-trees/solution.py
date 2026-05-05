class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # DFS solution where you make each node a root, get its height and add only those root with minimum height. O(n2) solution

        # adj = defaultdict(list)
        # result = []
        # if n == 1:
        #     return [0]

        # for edge in edges:
        #     src, dest = edge
        #     adj[src].append(dest)
        #     adj[dest].append(src)
     

        # def dfs_get_height(node, parent):
        #     max_height = 0
        #     for neighbour in adj[node]:
        #         if neighbour == parent:
        #             continue
        #         height = dfs_get_height(neighbour, node)
        #         max_height = max(max_height, height)
        #     return max_height + 1

        # mht = float('inf')

        # for node in range(n):
        #     temp = dfs_get_height(node, -1)
        #     if temp < mht:
        #         mht = temp
        #         result = [node]
        #     elif temp == mht:
        #         result.append(node)
            
        # return result

        # use topological trimming pattern for O(n) solution
        # each tree can have a max of two centers

        #first create the adj list, since this is undirected graph i.e bidirectional

        if n == 1:
            return [0]
        adj = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        # get the leaves in a queue. For graphs leaves are the one with indegree == 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        
        rem = n

        while rem > 2:
            total_leaves = len(queue)
            rem -= total_leaves

            
            for _ in range(total_leaves):
                leaf = queue.popleft()
                for nod in adj[leaf]:
                    indegree[nod] -= 1
                    if indegree[nod] == 1:
                        queue.append(nod)
        return list(queue)


            
