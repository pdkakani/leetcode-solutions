class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # step 1: build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        
        rows = len(board)
        cols = len(board[0])
        results = []

        def dfs(r, c, node):
            if not(0 <= r < rows and 0 <= c < cols):
                return
            
            char = board[r][c]
            if char not in node.children:
                return False

            next_node = node.children[char]
            if next_node.word:
                results.append(next_node.word)
                next_node.word = None

            board[r][c] = "#"

            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, next_node)
            
            board[r][c] = char

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        return results


        

        

        
