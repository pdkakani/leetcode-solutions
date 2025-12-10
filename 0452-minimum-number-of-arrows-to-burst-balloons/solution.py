class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        res = n

        prev = points[0]

        for i in range(1, n):
            curr = points[i]

            if curr[0] <= prev[1]:
                prev = [curr[0], min(curr[1], prev[1])]
                res -= 1
            else:
                prev = curr
        return res



        
