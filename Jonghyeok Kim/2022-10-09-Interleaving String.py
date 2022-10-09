class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len, s3_len  = len(s1), len(s2), len(s3)
        
        if s1_len + s2_len != s3_len:
            return False
        
        dp = [[False for _ in range(s1_len + 1)] for _ in range(s2_len + 1)]
        dp[-1][-1] = True 

        for s2_index in range(s2_len, -1, -1):
            for s1_index in range(s1_len, -1, -1):
                if s1_index < s1_len and s1[s1_index] == s3[s1_index+s2_index] and dp[s2_index][s1_index+1]:
                    dp[s2_index][s1_index] = True  
                
                if s2_index < s2_len and s2[s2_index] == s3[s1_index+s2_index] and dp[s2_index+1][s1_index]:
                    dp[s2_index][s1_index] = True  
        return dp[0][0]