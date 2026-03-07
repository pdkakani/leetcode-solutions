class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 1

        def k_works(speed):
            total_hrs = sum(ceil(pile/speed) for pile in piles)
            return total_hrs <= h

        while low <= high:
            mid = (low + high) // 2
            if k_works(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
