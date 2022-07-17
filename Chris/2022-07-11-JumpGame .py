#DP : TC : O(n*m) m = max(nums). SC  O(n)
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lenNum = len(nums)
        dp = [False for i in range(lenNum)]
        
        for i in range(lenNum-1, -1, -1):
            
            if i+nums[i] >= lenNum - 1:
                dp[i] = True
            else:
                for j in range(1, nums[i]+1, 1):
                    if dp[i+j]:
                        dp[i] = True
                        break
        
        return dp[0]
            


#Non-dp TC: O(n). SC: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        j = 0 # farthest reacheable index 
        
        for i in range(len(nums)-1):
            j = max(i + nums[i], j)
            
            if j >= len(nums)-1:
                return True
            
            if j <= i:
                return False
            
            
        
        return True
            
            
        