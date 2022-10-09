class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub_max = [1] * len(nums) 
        ans = -1
        for i in range(len(nums)):
            for j in range(i):
                # satisfy increasing subsequence
                if nums[j] < nums[i]:
                    sub_max[i] = max(sub_max[i], sub_max[j] + 1)
            ans = max(sub_max[i], ans) # track max value
        return ans