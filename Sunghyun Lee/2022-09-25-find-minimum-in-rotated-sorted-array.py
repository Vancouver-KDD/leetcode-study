class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1
        result = nums[0]
        while (left <= right):
            middle = (left + right) // 2
            result = min(result, nums[middle])
            
            if (nums[right] > nums[left]):
                result = min(nums[left], result)
                break
            if(nums[left] <= nums[middle]):
                left =  middle + 1
            else:
                right =  middle - 1
                
        return result
