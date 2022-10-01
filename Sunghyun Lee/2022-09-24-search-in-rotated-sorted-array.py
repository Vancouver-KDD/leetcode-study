class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m= 0
        while l <= r:
            m = (l+r)//2
            if(nums[m] == target):
                return m
          
            
            if nums[m] >= nums[l]:
                if nums[m] < target:
                    l= m+1
                elif target < nums[m]  and target >= nums[l]:
                    r= m - 1
                elif target < nums[m] and target < nums[l] :
                    l= m +1    
            else:
                if nums[m] > target:
                    r= m-1
                elif target > nums[m]  and target <= nums[r]:
                    l= m + 1
                elif target > nums[m] and target > nums[r] :
                    r= m -1    
        return -1
