class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True
        

    def search(self, word: str) -> bool:
        return self._search(self.root, 0, word)
    
    def _search(self, node, index, word):
        # all chars visited
        if len(word) == index:
            return node.endOfWord
        
        char = word[index]

        if char == ".":
            return any(self._search(child, index+1, word) for child in node.children.values())
        else:
            if char not in node.children:
                return False
            return self._search(node.children[char], index+1, word)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
