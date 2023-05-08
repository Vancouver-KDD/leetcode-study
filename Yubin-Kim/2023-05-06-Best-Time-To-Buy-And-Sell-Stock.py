
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        maxProfit = 0

        for price in prices:
            if price < buy:
                buy = price
            elif price > buy:
                maxProfit = max(maxProfit, price - buy)
        return maxProfit


def main(self=None):
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution.maxProfit(self, prices)
    print(result)

    prices2 = [7, 6, 4, 3, 1]
    result2 = Solution.maxProfit(self, prices2)
    print(result2)

    prices3 = [2, 4, 1]
    result3 = Solution.maxProfit(self, prices3)
    print(result3)

    prices4 = [2, 1, 2, 1, 0, 1, 2]
    result4 = Solution.maxProfit(self, prices4)
    print(result4)


if __name__ == "__main__":
    main()
