class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        need = [amount + 1] * (amount + 1)
        need[0] = 0
        for am in range(1, amount + 1):
            min_val = need[am]
            for coin in coins:
                if coin <= am:
                    min_val = min(min_val, need[am - coin] + 1)
            need[am] = min_val
        if need[-1] > amount:
            return -1
        else:
            return need[-1]