class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        
        for num in nums:
            if(numDict.get(num)):
                return True
        
            numDict[num] = True
        
        return False
        # Time Comp. : O(n)
        # Space Comp : O(n)