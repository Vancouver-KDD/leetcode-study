"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    # Single pass
    # Time complexity: O(n): single pass
    # Space complexity: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        min_price = 100001
        max_profit = 0

        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)
        return max_profit

    # Double Pointers
    # Time complexity: O(n): single pass
    # Space complexity: O(1)
    def maxProfitDoublePointer(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r  # not l += 1, move to the lowest value
                r += 1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
        return max_profit


def main():
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfitDoublePointer([7,1,5,3,6,4]))


if __name__ == "__main__":
    main()
