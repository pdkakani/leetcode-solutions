class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        res = 0

        for price in prices[1:]:
            profit = 0
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy
                res += profit
                buy = price
                

        return res
        
