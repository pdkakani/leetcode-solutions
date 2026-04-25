class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # first lets make an adj list out of the equations and values array
        # example: [a : [(b, 2.0)]]
        adj = defaultdict(list)
        for i in range(len(equations)):
            adj[equations[i][0]].append((equations[i][1], values[i]))
            adj[equations[i][1]].append((equations[i][0], 1/values[i]))

        result = []
        # write a dfs function to find the path
        def dfs(src, dst, visited, product):
            # visited is only for keeping track of cycles thats why no weights are tarcked here
            if src in visited:
                return -1.0
            # we found the path, so return the weights product    
            if src == dst:
                return product

            # add src node to set
            visited.add(src)

            # loop over its neighbors
            for neighbor in adj[src]:
                # get the node, and its weight
                n, weight = neighbor
                # do the recursion on its neighbor, while multipying the weight
                res = dfs(n, dst, visited, weight * product)
                # if no valid path found through this neighbor, try the next one. The valid path not found could be either, if the node was in visited set already or this particular neighbor was not in the path
                if res == -1.0:
                    continue
                # return the result of recursion
                return res
            # if the path is not found, then simply return -1.0
            return -1.0
        
        for query in queries:
            # check if the node is in adj list or not before calling dfs, if not simply append -1.0 to the result list
            if query[0] not in adj or query[1] not in adj:
                result.append(-1.0)
            else:
                # else call dfs to find the path and add its result which is the product of the weights along teh path to the result list
                temp = dfs(query[0], query[1], set(), 1)
                result.append(temp)

        return result
                

