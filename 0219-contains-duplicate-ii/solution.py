class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = defaultdict(list)

        for i in range(len(nums)):
            nums_map[nums[i]].append(i)
        
    
        dist = float('inf')
        for l in nums_map.values():

            n = len(l)
            if n > 1:
                for i in range(n-1):
                    dist = min(dist, abs(l[i] - l[i+1]))
        if dist <= k:
            return True

      
        
        return False

        
