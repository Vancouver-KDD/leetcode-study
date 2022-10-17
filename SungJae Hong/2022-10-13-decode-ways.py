class Solution:
    def numDecodings(self, s: str) -> int:
        #initialize the cache
        dp = {len(s) : 1}

        #recursive function

        def dfs(i):
            # good base case
            if i in dp:
                return dp[i]
            #bad base case
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)


