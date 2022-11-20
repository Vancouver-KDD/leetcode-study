class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s)+1)
        dp[len(s)-1] = 1 if s[-1] != '0' else 0
        
        dp[len(s)] = 1
        
        for i in range(len(s)-2,-1,-1):
            
            if s[i] == '1':

                dp[i] = dp[i+1] + dp[i+2]
                
                
            elif s[i] == '2':
                if s[i+1] not in ['7','8','9']:
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
            
            else:
                if s[i] == '0':
                    dp[i] == 0
                else:
                    dp[i] = dp[i+1]
                    
        return dp[0]
                
                
                    
                
            