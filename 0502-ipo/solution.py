class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # create sorted list of (capital, profit) sorted by capital
        # iterate through that list, add tuples with same capital to a max heap by profits
        # fetch the top of the heap, add to the current capital
        # repeat while k or sorted list runs out

        cap_prof = sorted(list(zip(capital, profits)))
        i = 0
        heap = []
        for _ in range(k):
            while i < len(cap_prof) and cap_prof[i][0] <= w:
                heapq.heappush(heap, -cap_prof[i][1])
                i += 1
            
            if not heap:
                return w
            
            w += (-heapq.heappop(heap))
        return w

