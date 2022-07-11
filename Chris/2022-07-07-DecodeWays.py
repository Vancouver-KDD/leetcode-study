# O(n*n*m) Solution Time Limit
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * len(s)
        wordIndices = []
        
        
        for i in range(len(s)-1, -1, -1):
            
            if s[i:] in wordDict:
                dp[i] = True
                wordIndices.append(i)
            else:
                for j in wordIndices:
                    if s[i:j] in wordDict:
                        dp[i] = True
                        wordIndices.append(i)
                        break
        
        
        return dp[0]
                    
            
        
                    
            
        