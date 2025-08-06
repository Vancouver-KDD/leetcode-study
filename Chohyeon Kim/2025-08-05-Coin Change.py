class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # amount
        # 12 - 10
        # 3 4      6
        #   3   4
        #  3 + 3
        #  4 + 4
        # base condition = when sum >= amount
        #  if sum > amount then -1
        #  if sum == amount return the answer

        memo = {}

        print(memo)

        def dfs(left: int):

            if left == 0:
                return 0

            if left in memo:
                return memo[left]

            res = 1e9

            for coin in coins:
                if left >= coin:
                    res = min(
                        res,
                        1
                        + dfs(
                            left - coin,
                        ),
                    )

            memo[left] = res
            return res

        min_coin = dfs(amount)

        return -1 if min_coin >= 1e9 else min_coin
