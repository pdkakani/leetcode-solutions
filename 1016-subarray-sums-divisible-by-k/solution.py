class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem = defaultdict(int)

        res = prefix_sum = 0

        rem[0] = 1

        for n in nums:
            prefix_sum += n
            remainder = prefix_sum % k
            res += rem[remainder]
            rem[remainder] += 1

        return res

        

