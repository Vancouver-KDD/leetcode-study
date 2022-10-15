class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        
        dp = set()
        dp.add(0)
        
        for num in nums:
            nextDp = set()
            for subsetSum in dp:
                if num + subsetSum == target:
                    return True
                
                nextDp.add(subsetSum) # Do not add num
                nextDp.add(subsetSum + num) # Add num
            
            dp = nextDp
        
        return True if target in dp else False
                
            
        