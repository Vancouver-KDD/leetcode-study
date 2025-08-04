class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #left side
        #right side
        #while left <= right:
        #define mid:
        #if left side is sorted, then we do our binary search
        #if right isde sorted, then we do our binary search

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            #means left side is sorted
            if nums[left] <= nums[mid]:

                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            #means right side is sorted
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        

       #Time complexity == O(log n)
       #Space complexity == O(1)