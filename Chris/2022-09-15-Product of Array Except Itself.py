class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        before = [1] * length  # before[k] = product of all elements in nums prior to index k
        after =  [1] * length  # after[k] = product of all elements in nums after index k
        res = [0] * length
        
        for i in range(1,length):
            before[i] = before[i-1] * nums[i-1]
            after[length - i - 1] = after[length-i] * nums[length - i]
            
        
        for i in range(length):
            res[i] = before[i] * after[i]
            
        return res
            
            