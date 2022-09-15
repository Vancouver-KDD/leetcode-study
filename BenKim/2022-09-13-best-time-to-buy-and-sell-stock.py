class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 아무리 큰 금액도 갱신되게 하기 위해 os의 가장큰값을 최소가격으로 설정
        min_price = sys.maxsize
        profit = 0
        
        # 최대가격과 최소가격을 갱신
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
        return profit