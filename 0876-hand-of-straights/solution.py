class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        for _ in range(0, len(hand), groupSize):
            curr = min(freq)
            g = 0
            while curr in freq and freq[curr] > 0 and g < groupSize:
                freq[curr] -= 1
                if freq[curr] == 0:
                    del freq[curr]
                curr += 1
                g += 1
                
            if g != groupSize:
                return False
        return True
