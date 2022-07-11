class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) <= 3:
            return max(nums)
        
        evenSumFirst = 0
        oddSumFirst = 0
        
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                evenSumFirst += nums[i]
                if evenSumFirst < oddSumFirst:
                    evenSumFirst = oddSumFirst
            else:
                oddSumFirst += nums[i]
                if evenSumFirst > oddSumFirst:
                    oddSumFirst = evenSumFirst
                    
        evenSumSec = 0
        oddSumSec = 0
        
        for i in range(1, len(nums)):
            if i % 2 == 0:
                evenSumSec += nums[i]
                if evenSumSec < oddSumSec:
                    evenSumSec = oddSumSec
            else:
                oddSumSec += nums[i]
                if evenSumSec > oddSumSec:
                    oddSumSec = evenSumSec
        
        return max(evenSumFirst, oddSumFirst, evenSumSec, oddSumSec)