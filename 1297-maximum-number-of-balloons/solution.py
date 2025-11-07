class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = Counter("balloon")
        inp = Counter(text)


        res = float('inf')
        for b in a:
            count = inp[b] // a[b]
            res = min(count, res)

        return res



