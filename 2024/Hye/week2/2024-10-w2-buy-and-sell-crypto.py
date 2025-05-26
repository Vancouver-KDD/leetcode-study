""" Buy and Sell Crypto

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions,
in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100

python3 Hye/week2/2024-10-w2-buy-and-sell-crypto.py
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. Iterate through the prices
        2. purchase on the low and sell on the high
        3. return the sum of profits
        """
        if len(prices) == 0:
            return 0
        
        profits = 0
        price = prices[0]
        for i in range(len(prices)):
            next_price = prices[i]
            if next_price > price:
                profits += (next_price - price)
            price = next_price

        return profits

def main():
    s = Solution()
    print("Week 2: Buy and Sell Crypto")

    prices = [10,1,5,6,7,1]
    profits = s.maxProfit(prices)
    print("prices: ", prices)
    print("profits: ", profits)
    assert profits == 6

    prices = [10,8,7,5,2]
    profits = s.maxProfit(prices)
    print("prices: ", prices)
    print("profits: ", profits)
    assert profits == 0

if __name__ == "__main__":
    main()
