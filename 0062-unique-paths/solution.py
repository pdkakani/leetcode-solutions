class Solution:
    memo = {}
    def uniquePaths(self, m: int, n: int) -> int:
        # if memo is None:
        #     memo = {}
        
        if (n,m) in self.memo:
            return self.memo.get((n,m))
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        
        self.memo[(n,m)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.memo.get((n,m)) 
        
        
