class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # m bouquets of k size is impossible to make if we have total flowers less than m * k
        if m * k > len(bloomDay):
            return -1
        low = 1
        high = max(bloomDay)

        def is_min_days(mid):
            number_of_bouq = 0
            total_flowers = 0
            for flower in bloomDay:
                if flower <= mid:
                    total_flowers += 1
                else:
                    total_flowers = 0
                if total_flowers == k:
                    number_of_bouq += 1
                    total_flowers = 0
            return number_of_bouq >= m

        ans = high
        while low <= high:
            mid = (low+high)//2
            if is_min_days(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans




        
