class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        msf = nums[0]
        curr = 0
        
        for i in nums:
            if curr < 0:
                curr = 0
            curr += i
            msf = max(msf, curr)
        
        return msf