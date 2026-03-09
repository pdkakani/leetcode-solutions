class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)

        def is_smallest(mid):
            total = sum(math.ceil(num/mid) for num in nums)
            return total <= threshold
        
        while low < high:
            mid = (low + high) // 2
            if is_smallest(mid):
                high = mid
            else:
                low = mid + 1
        return low

        
