class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 1 or len(prices) > 10**5:
            raise ValueError('Invalid Length')
        max_profit = 0
        if prices[0] < 0 or prices[0] > 10**4:
            raise ValueError('Invalid Length')
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < 0 or prices[i] > 10**4:
                raise ValueError('Invalid Length')
            if prices[i] < lowest_price:
                # check if the elem is less than the lowest price
                lowest_price = prices[i]
            max_profit = max(max_profit, prices[i] - lowest_price)
        return max_profit


s = Solution()
lst1 = [7, 1, 5, 3, 6, 4]
lst2 = [7, 6, 4, 3, 1]
lst3 = [-1, 1]
print(s.maxProfit(lst1))
print(s.maxProfit(lst2))
# print(s.maxProfit(lst3))
