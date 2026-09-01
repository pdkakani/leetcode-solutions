class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # this is search for answer problem

        def check(speed):
            total_hrs = sum(math.ceil(pile / speed) for pile in piles)
            return total_hrs <= h

        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low
