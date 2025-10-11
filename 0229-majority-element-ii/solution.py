class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        map1 = dict(Counter(nums))
        result = []
        for key,val in map1.items():
            if val > n/3:
                result.append(key)
        return result

