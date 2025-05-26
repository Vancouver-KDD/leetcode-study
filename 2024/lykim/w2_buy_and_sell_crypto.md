## Approach_1
- Keep a reference of the global max profit, while checking the local max profit
- The local max profit can be calculated by sliding two pointers, buying day and selling day. If current min price is larger than the selling day price, shift the buy day to the right. Otherwise, shift selling day only to the right

### Complexity
- Time complexity - O(n)
- Space complexity - O(1)

### Solution
```
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    buy, sell = 0, 1
    profit = 0

    while sell < prices.size do
        if prices[buy] < prices[sell]
            curr_profit = prices[sell] - prices[buy]
            profit = [curr_profit, profit].max
        else
            buy = sell
        end

        sell += 1
    end

    profit
end

```


## Approach_2, inefficient brute force
- Keep a reference of the global max profit, while checking the local max profit
- The local max profit can be calculated by sliding two pointers, buying day and selling day. If local profit is less than global profit, move the window

### Complexity
- Time complexity - O(n^2), bad
- Space complexity - O(1) with pointers

### Solution
```
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    size = prices.size
    return 0 if size < 2

    buy, sell = 0, 1
    profit = 0

    while buy < sell && sell < size do
        if prices[sell] - prices[buy] > profit
            profit = prices[sell] - prices[buy]
        end

        if sell < size - 1
            sell += 1
        else
            buy += 1
            sell = buy + 1
        end
    end

    profit
end
```

