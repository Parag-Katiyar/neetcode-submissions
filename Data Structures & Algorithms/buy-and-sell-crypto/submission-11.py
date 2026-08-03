class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]

        profit = 0 

        if len(prices) == 1:
            return 0

        if len(prices) == 2:
            if prices[1] - prices[0] > 0:
                return prices[1] - prices[0]
            else:
                return 0  


        for i in range(1,len(prices)):

            if buy > prices[i]:
                buy = prices[i]

            if buy < prices[i] and profit < prices[i] - buy:
                profit = prices[i] - buy
        
        return profit



        