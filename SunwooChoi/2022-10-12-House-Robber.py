class Solution:
    def rob(self, nums: List[int]) -> int:
        # only can rob one house
        if len(nums) == 1:
            return nums[0]

        for i in range(2, len(nums)):
            # rob current house + max profit of previous robbing except adjacent house
            nums[i] += max(nums[:i-1])
                
        
        return max(nums[-1], nums[-2])
