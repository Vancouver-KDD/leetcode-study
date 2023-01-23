class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        acc = 1
        
        for idx in range(1, len(nums)):
            ans[idx] = ans[idx-1] * nums[idx-1]
        for idx in range(len(nums)-1, -1, -1):
            ans[idx] = ans[idx] * acc
            acc = acc * nums[idx]
        return ans
