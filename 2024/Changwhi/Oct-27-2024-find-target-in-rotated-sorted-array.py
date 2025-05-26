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



    class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        similar to finding minimum value in rotated sorted array
        in this case, you need to find index of target value
        
        I would say that you can implement the same way, but adds one more condition which is greater than or equal to target.
        if mid is smaller than first element, then, 
        (mid < first),
            bigger smaller <-<- mid ->-> biger 
            if target < mid
                to the left side
            if target > mid
                right or left?? 
                if target >= first 
                    to the left
                if target < first
                    to the right    
        (mid >= first),
            smaller <-<-  mid  ->-> bigger smaller
            if taget < mid 
                if target < first:
                    to the right
                if target > first 
                    to the left

                to the left
            if target > mid
                to the right             
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < nums[left]:
                if target < nums[mid]:
                    right = mid -1
                elif target > nums[mid]:
                    if target > nums[left]:
                        right = mid - 1
                    elif target < nums[left]:
                        left = mid + 1
                    else: 
                        return left
                else:
                    return mid
            else:
                if target < nums[mid]:
                    if target < nums[left]:
                        left = mid + 1
                    elif target > nums[left]:
                        right = mid - 1
                    else: 
                        return left
                elif target > nums[mid]:
                    left = mid + 1
                else: 
                    return mid
        return -1