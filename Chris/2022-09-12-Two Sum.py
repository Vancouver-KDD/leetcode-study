class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dict to store val - index pairs
        
        valDict = {}
        
        for i, num in enumerate(nums):
            
            if target - num in valDict:
                return [i, valDict[target-num]]
            
            valDict[num] = i
            
          
