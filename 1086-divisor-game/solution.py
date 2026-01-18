class Solution:
    memo = {}
    def divisorGame(self, n: int) -> bool:
        # current player losses
        if n == 1:
            return False
        if n in self.memo:
            return self.memo[n]

        # try all possible moves
        for i in range(1,n):
            if n % i == 0:
                # if opponent losses after our move, we win
                if not self.divisorGame(n - i):
                    self.memo[n] = True
                    return True

        # if no winning moves exists, current player losses
        self.memo[n] = False
        return False
        
        
        
