class Solution:
    def alienOrder(self, words: List[str]) -> str:
        in_degree = {key: 0 for word in words for key in word}
        n = len(words)

        def get_edge(fword, sword):
            k = 0
            m = min(len(fword), len(sword))
            while k < m:
                if fword[k] != sword[k]:
                    return [fword[k], sword[k]]
                k += 1
        
        def is_prefix(fword, sword):
            return fword.startswith(sword)

        i = 0
        j = 1
        adj = defaultdict(list)
        while j < n:
            fword = words[i]
            sword = words[j]

            if is_prefix(fword, sword) and len(fword) > len(sword):
                return ""
            
            edge = get_edge(fword, sword)
            if edge:
                adj[edge[0]].append(edge[1])
            i += 1
            j += 1
        
        for val in adj.values():
            for v in val:
                in_degree[v] += 1

        queue = deque()
        for k, v in in_degree.items():
            if v == 0:
                queue.append(k)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)

            for nbr in adj[node]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    queue.append(nbr)

        if len(res) != len(in_degree):
            return ""
        
        return "".join(res)


