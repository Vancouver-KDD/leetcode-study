class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0

        #going for index so it has to be -1 at the end to not have out of range error
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            #tryna return the right index
            if nums[mid] == target:
                return mid
            
            #bringing the top range down
            if nums[mid] > target:
                right = mid - 1
                
            #bringing the low range up
            else:
                left = mid + 1
        
        return -1


        #Time complexity == O(log n)
        #Space complexity == O(1)