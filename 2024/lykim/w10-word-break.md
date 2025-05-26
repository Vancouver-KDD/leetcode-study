## Approach
- Bottom up approach, initializing DP cache array with false, the very last DP sets as true as base case
- iterate from the last element of string, do nested loop for the dictionary.
  - At each iteration compare if every word in the dictionary is in there, with the length check, then set the DB cache array as true from the last DP value


### Complexity
- Time complexity - O(n * m * t) at worst, t is the max length of any word in the dictionary
- Space complexity - O(n)

### Solution
```
# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
    dp = Array.new(s.size + 1, false)
    dp[s.length] = true

    (s.length - 1).downto(0) do |i|
        for w in word_dict do
            if (i + w.length) <= s.length && s[i..(i + w.length - 1)] == w #check from the last point
                dp[i] = dp[i + w.length]
            end

            if dp[i]
                break
            end
        end
    end

    return dp[0]
end
```
