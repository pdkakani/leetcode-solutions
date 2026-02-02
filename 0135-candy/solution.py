class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n

        prefix = 1
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                prefix += 1
            else:
                prefix = 1
            res[i] = prefix
        
        suffix = 1
        for i in range(n-2, -1,-1):
            if ratings[i] > ratings[i+1]:
                suffix += 1
            else:
                suffix = 1
            res[i] = max(res[i], suffix)
        
        return sum(res)
        


        
