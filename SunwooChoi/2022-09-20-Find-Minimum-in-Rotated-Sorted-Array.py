class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            # set median index as pivot since it's sorted
            mid = (left + right) // 2
            
            # find minimum
            if left == right:
                return nums[left]
            # minimum value in range [mid+1, right]
            elif nums[right] < nums[mid]:
                left = mid + 1
            # minimum value in range [left, mid]
            else:
                right = mid

