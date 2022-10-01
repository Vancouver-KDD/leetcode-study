class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums == None or len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left < right - 1:
        
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            
            if nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            
            elif nums[mid] < nums[left]:
                if target > nums[right] or target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[left] < target < nums[mid]:
                    right = mid
                else:
                    left = mid
                    
        return left if nums[left] == target else right if nums[right] == target else -1