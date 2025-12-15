class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        
        10 9 2 5 3 7 101 18
        dp[i] :: including nums[i], increasing subsequence 
        j < i  and if nums[j] < nums[i]
        dp[i] = max(dp[i], dp[j] + 1)

        모든 i 에 대해 앞의 모든 j 를 검사하면, i 에서 끝나는 최장 길이를 
        정확히 구할 수 있다. 
        전체 문자(배열 전체의 LIS) 는 max(dp[i])
        """

        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


    