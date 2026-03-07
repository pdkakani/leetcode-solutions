class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        print(low, high)
        ans = high

        def is_minimum(capacity):
            days_needed = 1
            curr_load = 0
            for weight in weights:
                if curr_load + weight > capacity:
                    days_needed += 1
                    curr_load = 0
                curr_load += weight
            return days_needed <= days
        
        while low <= high:
            mid = (low + high) // 2
            if is_minimum(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

        
