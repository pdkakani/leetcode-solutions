class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 1
        if n in self.memo:
            return self.memo[n]
        count = 0
        
        for i in range(1,3):
            remainder = n - i
            res = self.climbStairs(remainder)
            
            count += res
        
        self.memo[n] = count
        return count
        


        
