class Solution:
    def rob(self, nums):
        # Bottom Up DP (Tabulation) - for loop instead of recursion
        # Time: O(n)
        # Space: O(1) - only need one step back or/and two step back
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])

        dp = [0] *n
        dp[0]=nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i]=max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[n-1]


solution = Solution()
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))


