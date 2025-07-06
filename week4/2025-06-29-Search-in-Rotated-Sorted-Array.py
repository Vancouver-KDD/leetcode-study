class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
               if target > nums[mid] or target < nums[left]:
                   left = mid + 1
               else:
                   right = mid - 1
            # If the left half is not sorted, then the right half must be sorted
            else:
               if target < nums[mid] or target > nums[right]:
                   right = mid - 1
               else:
                   left = mid + 1

        return -1