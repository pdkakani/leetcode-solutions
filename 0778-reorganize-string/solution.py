class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_freq = max(freq.values())

        if max_freq > (len(s)+ 1) // 2:
            return ""

        res = []
        prev = None
        heap = [(-v,k) for k,v in freq.items()]
        heapify(heap)

        for _ in range(len(s)):
            freq, char = heappop(heap)
            res.append(char)

            if prev is not None:
                heappush(heap, prev)
            
            prev = (freq+1, char) if freq + 1 < 0 else None
        return "".join(res)
            


        
