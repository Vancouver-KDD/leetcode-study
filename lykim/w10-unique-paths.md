## Approach
- Dynamic programming
  - Initialize an array dp with the column length and value 1 for all.
  - Then iterate the nested array with row and column with the bottom up approach, and increment the dp array with the previous value
- Math way 

### Complexity
- Time complexity - O(n * m)
- Space complexity - O(n)

### Solution
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
