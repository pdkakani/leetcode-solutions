class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = dict(Counter(nums))
        sorted_map = sorted(map1.items(), key = lambda x: x[1], reverse = True)

        result = []
        count = 0
        for val in sorted_map:
            if count == k:
                break
            result.append(val[0])
            count+=1
        return result

        



        
