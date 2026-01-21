class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        res = ""
        ans = []
        heapq.heapify(ans)
        for i in counter:
            heapq.heappush(ans, (counter[i], i))
        
        while ans:
            temp = heapq.heappop(ans)
            res += temp[1] * temp[0]
        
        return res[::-1]

        
