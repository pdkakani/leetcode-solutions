class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        def is_valid(mid):
            splits = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > mid:
                    splits += 1
                    curr_sum = 0
                curr_sum += num
            return splits <= k
        
        ans = high
        while low <= high:
            mid = (low+ high) // 2
            if is_valid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

