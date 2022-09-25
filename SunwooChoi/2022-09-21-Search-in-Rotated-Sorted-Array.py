class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        noTargetFound = -1
        
        # Binary search
        while left <= right:
            # set the median as the pivot
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
           
            if nums[mid] < nums[right]:
                # target is in the range (mid, right]
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                # target is in the range [left, mid)    
                else:
                    right = mid - 1
            else:
                # target is in the range [left, mid)
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                # target is in the range (mid, right]    
                else:
                    left = mid + 1
                    
        return noTargetFound