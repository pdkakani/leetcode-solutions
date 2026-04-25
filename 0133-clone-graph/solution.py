"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # original node: copy node
        visited = {} 

        def dfs(n):
            # check if the mapping for original node already present in map
            if n in visited:
                # return clone node
                return visited[n]

            # create copy
            copy = Node(n.val)
            # add to map
            visited[n] = copy

            # iterate over its neighbors
            for i in n.neighbors:
                # recurse over each of its neigbors, to create thier copies
                res = dfs(i)
                # add the result (copies) to the node.neighbors list
                copy.neighbors.append(res)

            # return the copy
            return copy

        return dfs(node)
        
        
