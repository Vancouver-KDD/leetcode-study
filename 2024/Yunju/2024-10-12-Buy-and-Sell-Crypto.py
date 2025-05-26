class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0 #거래를 하지 않기를 선택할수도 있으니.. 그 경우 이익은 0임.
        for price in prices:
        	# lowest_price를 찾음
            if price < lowest_price:
                lowest_price = price
            # 최대 이익을 찾음
            elif price - lowest_price > max_profit:
                max_profit = price - lowest_price
         # 최대 이익을 반환
        return max_profit 