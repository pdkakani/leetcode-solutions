class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        xFound = False
        yFound = False
        zFound = False
        x, y, z = target
        for a, b, c in triplets:
            if a <= x and b <=y and c<=z:
                if a == x: xFound = True
                if b == y: yFound = True
                if c == z: zFound = True

        return xFound and yFound and zFound

        
