class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        seen = {0:1} # prefix: count

        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix - k
            if rem in seen:
                count += seen[rem]
            seen[prefix] = seen.get(prefix, 0) + 1
        return count





