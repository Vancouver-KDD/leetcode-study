class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        s_len, t_len = len(s), len(t)
        
        dp = [[0] * t_len for _ in range(s_len +1)]
        
        
        
        for i in range(s_len-1,-1,-1):
            for j in range(t_len-1,-1,-1):
                # Trivial cases
                if t_len - j > s_len - i:
                    continue
                
                # Common part 
                dp[i][j] = dp[i+1][j]
                
                # last char of t
                if j == t_len-1 and s[i] == t[j]:
                    dp[i][j] += 1
                    continue
                
                # all other cases
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        
        return dp[0][0]
                    