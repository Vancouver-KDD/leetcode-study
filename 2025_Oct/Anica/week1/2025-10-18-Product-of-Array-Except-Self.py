class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1 
        res = []

        for i in range(len(nums)):
            res.append(prefix)
            prefix*=nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]

        return res


        