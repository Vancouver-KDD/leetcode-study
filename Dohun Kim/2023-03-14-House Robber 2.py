class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(num[0], self.helper(nums[:-1]), self.helper(nums[1:]))
    
    def helper(self, nums: List[int]) -> int:
        l, r = 0, 0
        for n in nums:
            temp = max(l+n, r)
            l = r
            r = temp
        return r