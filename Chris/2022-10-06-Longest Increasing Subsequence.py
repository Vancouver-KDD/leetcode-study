class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        ls = [1] * len(nums)
        
        # Size of maximum subsequence starting from index i
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                
                if nums[i] < nums[j]:
                    ls[i] = max(ls[j]+1, ls[i])
                
            
        return max(ls)