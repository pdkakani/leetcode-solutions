class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_map = Counter(stones)
        res = 0
        for i in jewels:
            res = res + stones_map.get(i, 0)
        return res
        
