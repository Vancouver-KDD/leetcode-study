## Approach
- Keep the 2-dimensional array of DP for each substring, n * m, to record the longest subsequence at the index
  - with initialization of 0 with size + 1, then no need to concern 0,0 case specifically
- Iterate each char for text1 and text2, and update with +1 if the two chars are the same, otherwise pick the max one from the previous dp value

### Complexity
- Time complexity - O(n * m)
- Space complexity - O(n * m)

### Solution
```
# @param {String} text1
# @param {String} text2
# @return {Integer}
def longest_common_subsequence(text1, text2)
    dp = Array.new(text1.size + 1) { Array.new(text2.size + 1) {0} }

    i = 0
    while i < text1.size do
        j = 0
        while j < text2.size do
            if text1[i] == text2[j]
                dp[i][j] = dp[i - 1][j - 1] + 1
            else
                dp[i][j] = [dp[i][j - 1], dp[i - 1][j]].max
            end

            j += 1
        end

        i += 1
    end

    dp[text1.size - 1][text2.size - 1]
end
```
