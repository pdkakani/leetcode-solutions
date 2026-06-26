import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        n = len(hand)

        heap = list(freq.keys())
        heapq.heapify(heap)

        while heap:
            smallest = heap[0]
            for card in range(smallest, smallest + groupSize):
                if freq[card] == 0:
                    return False
                freq[card] -= 1
                if freq[card] == 0:
                    if card != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True

        # for _ in range(0, len(hand), groupSize):
        #     curr = min(freq)
        #     g = 0
        #     while curr in freq and freq[curr] > 0 and g < groupSize:
        #         freq[curr] -= 1
        #         if freq[curr] == 0:
        #             del freq[curr]
        #         curr += 1
        #         g += 1
                
        #     if g != groupSize:
        #         return False
        # return True
