class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxresult = 0;
        buyingPrice= prices[0]
        for i in range(1,len(prices)):
            maxresult = max(maxresult, prices[i]-buyingPrice)
            buyingPrice = min(buyingPrice, prices[i])
        return maxresult
