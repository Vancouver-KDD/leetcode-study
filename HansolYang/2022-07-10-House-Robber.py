class Solution:
    def rob(self, nums: List[int]) -> int:
       # return max(self.robHelper(False, nums[1:], 0), self.robHelper(True, nums[1:], nums[0]))
        
   # def robHelper(self, robbed, arr, res):
        
   #     if len(arr) == 0:
   #         return res
        
   #     if robbed:
   #         return self.robHelper(False, arr[1:], res)
        
   #     else:
   #         return max(self.robHelper(True, arr[1:], res + arr[0]), self.robHelper(False, arr[1:], res))
        if len(nums) == 0:
            return 0
    
        if len(nums) == 1:
            return nums[0]
    
        evenSum = 0
        oddSum = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                evenSum += nums[i]
                if evenSum < oddSum:
                    evenSum = oddSum
            else:
                oddSum += nums[i]
                if evenSum > oddSum:
                    oddSum = evenSum
                
        return max(evenSum, oddSum)

