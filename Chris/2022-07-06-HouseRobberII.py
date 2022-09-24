class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if(len(nums) < 4):
            return max(nums)
        
        def robArray(arrayNums: List[int]) -> int:
            
            dp = [0 for i in range(len(arrayNums) + 2)]
            
            for i in range(len(arrayNums)-1, -1, -1):
                dp[i] = max(dp[i+1], dp[i+2] + arrayNums[i])
                
            return dp[0]
        
        
        return max(robArray(nums[1:]) , robArray(nums[2:-1]) + nums[0])