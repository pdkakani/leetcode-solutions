class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = set()
        left = 0

        # create the window
        for right in range(n):
            if right > k:
                seen.remove(nums[right-k-1])
            if nums[right] in seen:
                return True
            seen.add(nums[right])

        return False


        
