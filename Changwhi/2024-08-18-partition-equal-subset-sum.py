class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2

        # If the total sum is odd, we cannot partition the array into two equal sum subsets
        if total // 2 != total /2:
            return False
        
        dp = [False] * (target+1)
        
        dp[0] = True
        
        # Loop through each element in the input array
        for num in nums:
            # Starting from the target sum, loop backwards through the dp list
            for j in range(target, num-1, -1):
                # If we can form a sum j-num using the previous elements in the input array,
                # we can also form a sum j using the current element
                dp[j] = dp[j] or dp[j-num]
        
        # Return whether or not we can form a sum of target_sum using the input array
        return dp[target]