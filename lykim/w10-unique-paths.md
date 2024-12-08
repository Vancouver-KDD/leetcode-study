## Approach
- First intuition is just using factorial
  - That's easier and better in complexity - O(m+n), O(1)

- Dynamic programming
  - Initialize an array dp with the column length and value 1 for all.
  - Then iterate the nested array with row and column with the bottom up approach, and increment the dp array with the previous value
    
### Complexity
- Time complexity - O(n * m)
- Space complexity - O(n)

### Solution
Using factorial
```
# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
    return 1 if n == 1 || m == 1
  
    down_count = m - 1 
    right_count = n - 1

    total = down_count + right_count
    factorial(total) / (factorial(down_count) * factorial(right_count))
end

private def factorial(number)
    if number == 0 || number == 1
        return 1
    else
        number * factorial(number - 1)
    end
end
```

Using DP
```
# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
    dp = Array.new(n, 1)
    (m - 2).downto(0) do |i|
        (n - 2).downto(0) do |j|
            dp[j] += dp[j + 1]
        end
    end

    dp[0]
end
```
