class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums)-1
        
        while l < r:
            m = (l+r)//2
            cur = nums[m]
            if cur == target:
                return m
            elif cur < target:
                l = m +1
            else:
                r = m -1
                
        return l if nums[l] == target else -1
    
            
            