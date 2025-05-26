## Approach
- Use bottom up approach. Set a base case for the last index, and with DFS, it goes to the end of the array and adds up to the left from there.
- For space optimization, instead of a dp array, keep 3 variables (temp, dp1, dp2) and iterate the string from the last to the first. 
  
### Complexity
- Time complexity - O(n)
- Space complexity - O(n) / O(1) with optimization

### Solution
**With Space optimiazation O(1)**
```
# @param {String} s
# @return {Integer}
def num_decodings(s)
    dp, dp2 = 0, 0
    dp1 = 1

    i = s.size - 1

    until i == -1
        if s[i] == "0"
            dp = 0
        else
            dp = dp1
        end 

        if i + 1 < s.size && (s[i] == "1" || s[i] == "2" && "0123456".include?(s[i + 1])) # double digit case
            dp += dp2
        end

        dp, dp1, dp2 = 0, dp, dp1
        i -= 1
    end

    dp1
end

private def dfs(i, s = @s)
    return @dp[i] if @dp[i]
    return 0 if s[i] == "0"

    res = dfs(i + 1)
    
    if i + 1 < s.size && (s[i] == "1" || s[i] == "2" && "0123456".include?(s[i + 1])) # double digit case
        res += dfs (i + 2)
    end

    @dp[i] = res

    res
end
```

```
# @param {String} s
# @return {Integer}
def num_decodings(s)
    @dp = {}
    @dp[s.size] = 1 # base case
    @s = s
    dfs(0) 
end

private def dfs(i, s = @s)
    return @dp[i] if @dp[i]
    return 0 if s[i] == "0"

    res = dfs(i + 1)
    
    if i + 1 < s.size && (s[i] == "1" || s[i] == "2" && "0123456".include?(s[i + 1])) # double digit case
        res += dfs (i + 2)
    end

    @dp[i] = res

    res
end
```
