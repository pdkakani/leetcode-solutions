class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def check(cap):
            days_needed = 1
            curr_weight = 0
            for w in weights:

                # if the current weight plus the new wieght exceeeds above cap that means ship is full, increase the days needed to send that ship by one
                if curr_weight + w > cap:
                    days_needed += 1
                    curr_weight = 0
                curr_weight += w
            return days_needed <= days
        
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
            
        return low

        
