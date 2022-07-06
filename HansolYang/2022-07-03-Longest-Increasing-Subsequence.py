class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        prev = nums[0]
        maximum = 0
        curr = 0
        
        for i in nums:
            if i > prev:
                curr += 1
                maximum = max(curr, maximum)
            else:
                curr = 0
            
            prev = i
        
        return maximum
                