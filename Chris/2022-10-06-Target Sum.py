class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        dp = {}
        
        def dfs(curSum, i):
            
            
            if i < 0 and curSum == target:
                return 1
            if i < 0:
                return 0
            if (curSum, i) in dp:
                return dp[(curSum,i)]
            
            
            dp[(curSum, i)] = dfs(curSum+nums[i] , i-1) + dfs(curSum-nums[i], i-1)
            return dp[(curSum, i)]
        
        return dfs(0, len(nums)-1)
                
            