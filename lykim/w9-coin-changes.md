## Approach
- Initialize an array to cache with length of the amount + 1 (with a base case)
- Iterate the amount from 1, and check each coin if they can make up the amount, and record the minimum case.

### Complexity
- Time complexity - O(n * t), t is the amount
- Space complexity - O(t)

### Solution
```
# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}
def coin_change(coins, amount)
    dp = Array.new(amount + 1, amount + 1)
    dp[0] = 0

    i = 1
    while i <= amount do
        for coin in coins do
            if coin <= i
                dp[i] = [dp[i - coin] + 1, dp[i]].min
            end
        end

        i += 1
    end

    if dp[amount] != amount + 1
        dp[amount]
    else
        -1
    end
end
```
