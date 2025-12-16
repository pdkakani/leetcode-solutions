class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        balls = 0
        moves = 0
        res = [0] * n

        #left to right pass
        for i in range(n):
            res[i] += moves
            balls += int(boxes[i])
            moves += balls

        balls = 0
        moves = 0

        #right to left
        for i in range(n-1, -1, -1):
            res[i] += moves
            balls += int(boxes[i])
            moves += balls

        return res



