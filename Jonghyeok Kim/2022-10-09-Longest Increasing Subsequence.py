class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        num_len = len(nums)
        #use dp list that keeps track of LIS
        dp = [0] * (num_len + 1)
        for i in range(num_len-1,-1,-1):
            for j in range(num_len-1, i, -1):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp) + 1
