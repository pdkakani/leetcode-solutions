class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # first make indegrees array
        # we are douing topological sort here to get the order
        result = []
        indegrees = [0] * numCourses
        adj = defaultdict(list)

        for i in range(len(prerequisites)):
            dest, src = prerequisites[i]
            adj[src].append(dest)
            indegrees[dest] += 1

      
        queue = deque()
        for n in range(numCourses):
            if indegrees[n] == 0:
                queue.append(n)
        print(queue)
        
        while queue:
            #take the first node off
            node = queue.popleft()
            #add to result
            result.append(node)
            #loop over the neighbours
            for i in adj[node]:
                # reduce thier indegree by 1
                indegrees[i] -= 1
                # if the indegree happens to reduce down to 0 add to queue as that will be the next node to be processed
                if indegrees[i] == 0:
                    # add to the queue
                    queue.append(i)

        if len(result) != numCourses:
            return []
        return result
        
