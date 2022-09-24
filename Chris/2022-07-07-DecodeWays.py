class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0 for i in range(len(s)+2)]
        
        n = len(s)
        dp[n] = 1
        if s[n-1] != '0':
            dp[n-1] = 1
        
        
        for i in range(len(s)-2, -1,-1):
            
            if s[i] == '0':
                dp[i] = 0
            
            elif s[i] == '1':
                if s[i+1] == '0':
                    dp[i] = dp[i+2]
                else:
                    dp[i] = dp[i+1] + dp[i+2]
            
            elif s[i] == '2':
                if s[i+1] == '0':
                    dp[i] = dp[i+2]
                elif s[i+1] == '7' or s[i+1] == '8' or s[i+1] == '9':
                    dp[i] = dp[i+1]
                else:
                    dp[i] = dp[i+1] + dp[i+2]
            else:
                if s[i+1] == '0':
                    return 0
                
                dp[i] = dp[i+1]
                
        
        return dp[0]
        