class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = prices[0] + fee
        profit = 0

        for p in range(1, len(prices)):
            curr_price = prices[p]
            if curr_price + fee < buy: # means i can buy since cheaper price found
                buy = curr_price + fee
            elif curr_price > buy: # means i can sell since higher price found
                profit += curr_price - buy
                buy = curr_price

        return profit

        # cash = 0 # empty handed
        # hold = -prices[0] # the stock we hold
        # for p in prices:
        #     cash = max(cash, hold + p - fee) #updates on sell
        #     hold = max(hold, cash - p) # updates on buy
        # return cash



        
