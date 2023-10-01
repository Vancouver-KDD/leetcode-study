# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = len(nums) - 1
        left = 0
        ans = []

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans.insert(0, nums[right] * nums[right])
                right = right - 1
            else:
                ans.insert(0, nums[left] * nums[left])
                left = left + 1

        return ans


# The code uses a two-pointer approach to square the elements of the input list nums
# while sorting them in non-decreasing order.
# It initializes two pointers, left and right, at the start and end of the list.
# In a loop, it compares the absolute values of elements at these pointers.
# The smaller absolute value is squared and placed in the result list,
# and the corresponding pointer is moved accordingly.
# This process continues until all elements are processed,
# resulting in a sorted list of squared values.
