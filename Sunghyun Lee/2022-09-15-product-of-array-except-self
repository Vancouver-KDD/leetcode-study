class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = 1
        right = 1
        resultlist =[]

        for i in range(len(nums)):
            resultlist.append(left)
            left *= nums[i]
            
        for i in range(len(nums)-1,-1,-1):
            resultlist[i] =  resultlist[i] * right
            right *= nums[i]
        return resultlist
