class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)

        def pattern(s):
            res = set()
            for i in range(n):
                res.add(s[:i] + "*" + s[i+1:])
            return res
        
        adj = defaultdict(list)

        for word in wordList:
            for p in pattern(word):
                adj[p].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            node, dist = queue.popleft()
            if node == endWord:
                return dist
            
            node_pattern = pattern(node)
            for p in node_pattern:
                for a in adj[p]:
                    if a not in visited:
                        visited.add(a)
                        queue.append((a, dist + 1))
        return 0
