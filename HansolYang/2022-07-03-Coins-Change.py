class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return -1
        
        maximum = max(coins)
        num = 0
        
        if amount % maximum == 0:
            return amount / maximum
        elif amount < maximum:
            coins = coins.remove(maximum)
            return self.coinChange(coins, amount)
        else:
            curr = amount // maximum
            num += curr
            amount -= curr*maximum
            coins.remove(maximum)
            return num + self.coinChange(coins, amount)