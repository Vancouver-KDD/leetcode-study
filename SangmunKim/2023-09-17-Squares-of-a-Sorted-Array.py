class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        index = right
        output = [0] * len(nums)

        while index >= 0 :
            if abs(nums[left]) > abs(nums[right]):
                output[index] = nums[left] * nums[left]
                left += 1
            else :
                output[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        
        return output
