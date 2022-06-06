class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dict to store val - index pairs
        valIndex = {} 
        
        for i in range(len(nums)):
            val = nums[i]
            
            # Look up corresponding value in dictionary. 
            # If there is, get the index of the corresponding value. j = None otherwise.
            j = valIndex.get(target - val)
            
            
            if(j != None):   # Using "!= None" is important b/c j can be 0 which is false when used as boolean   
                return [i,j]
            
            
            # store current val - index pair to the dictionary
            valIndex[val] = i
            
    ## When calculating the runtime, do I need to use average case or amortized worst case?
    ## https://wiki.python.org/moin/TimeComplexity