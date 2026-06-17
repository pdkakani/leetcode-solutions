class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = defaultdict(list)

        for c, p in prerequisites:
            in_degree[c] += 1
            adj[p].append(c)

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.popleft()
            count += 1

            for n in adj[node]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)
                    
        return count == numCourses

            
