class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        return heapq.nsmallest(k, count.keys(), key = lambda w: (-count[w], w))
        
