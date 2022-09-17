class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = [0] * len(nums)
        products[0] = 1
        acc = 1 # acculmulative product in reverse
        
        # product x[n] = 1 * x[0] * x[1] * ... * x[n-1]
        for idx in range(1, len(nums)):
            products[idx] = products[idx-1] * nums[idx-1]
        
        for idx in range(len(nums)-1, -1, -1):
            products[idx] = products[idx] * acc
            acc = acc * nums[idx]
        return products