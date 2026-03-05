class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        inp = ''.join(str(i) for i in digits)
        res = int(inp) + 1
        return [int(x) for x in str(res)]

