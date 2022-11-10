class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        
        dp = {}
        
        
        def dfs(i,j):
            
            
            if i == len(s1) and j == len(s2):
                return True
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i < len(s1) and s3[i+j] == s1[i] and dfs(i+1, j):
                return True
            
            if j < len(s2) and s3[i+j] == s2[j] and dfs(i, j+1):
                return True
            
            dp[(i,j)] = False
            return False
        
        
        return dfs(0,0)