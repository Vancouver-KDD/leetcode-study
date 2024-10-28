class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3, 4, 5, 1, 2]
        
        mid = 5
        
        compare to first one to see if first one is greater than mid. 
            if yes, smallest value should be on the left side. 
            if no, smallest value should be on the right side.
        move corresponding pointer.    
        """
    
        left, right = 0, len(nums) - 1
        res = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
                
            mid = (left + right) // 2
            res = min(res, nums[mid])
            
            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        return res