class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        seen = set()
        n = len(nums)

        for right in range(n):
            window = right - left
            if window > k:
                seen.remove(nums[left])
                left += 1
            if nums[right] in seen:
                return True
            seen.add(nums[right])
        return False
        
