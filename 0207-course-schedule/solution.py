class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # since the courses are already numbered from 0 to n-1, we can use a list instead of map for indegrees
        in_degrees = [0] * numCourses
        
        # make adj list
        adj = defaultdict(list)

        for course in prerequisites:
            c, p = course
            adj[p].append(c)
            in_degrees[c] += 1
        
        # adj = {0: [1,2]}
        # in_degrees = [1,2]

        queue = deque()

        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.pop()
            count += 1

            for n in adj[node]:
                in_degrees[n] -= 1
                if in_degrees[n] == 0:
                    queue.append(n)
            
        return count == numCourses

        
        

        
