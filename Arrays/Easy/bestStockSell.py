### We just had to identify the pattern and see what's going on.

class Solution:
    def maxProfit(self, prices) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > minPrice:
                maxProfit += prices[i] - minPrice
                minPrice = prices[i]
            else:
                minPrice = prices[i]
        if maxProfit<=0:
            return 0
        else:
            return maxProfit