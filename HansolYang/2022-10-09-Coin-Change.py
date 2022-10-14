class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
#         temp = [0] * len(coins)
#         left = amount
        
        arr = [float(inf)]*(amount+1)
        #each element shows the min. amount of coins
        
        arr[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                arr[i] = min(arr[i], arr[i - coin] + 1)
        
        return arr[-1] if arr[-1] != float(inf) else -1
        
#         for i in range(len(temp)-1, -1, -1):
#             temp[i] = left // coins[i]
#             left -= temp[i]*coins[i]
        
#         return sum(temp) if left == 0 else -1