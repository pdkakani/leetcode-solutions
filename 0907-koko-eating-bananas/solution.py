class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            return hours <= h

        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2
            if k_works(k):
                right = k
            else:
                left = k + 1

        return left  



        
