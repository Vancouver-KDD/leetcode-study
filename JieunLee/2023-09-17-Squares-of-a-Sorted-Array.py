## Method 1
# O(nlog(n)) time | O(n) space where n is the length of the input array
#class Solution:
#    def sortedSquares(self, nums: List[int]) -> List[int]:
#        sqr_list = []
#        sqr_list = [n**2 for n in nums]
#        sqr_list.sort()
#        return sqr_list



## Method 2
# O(n) time | O(n) space where n is the length of the input array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr_list = [0 for _ in nums]

        left_idx = 0
        right_idx = len(nums) - 1

        for idx in reversed(range(len(nums))):
            left_val = nums[left_idx] * nums[left_idx]
            right_val = nums[right_idx] * nums[right_idx]

            if left_val > right_val:
                sqr_list[idx] = left_val
                left_idx += 1
            else:
                sqr_list[idx] = right_val
                right_idx -= 1
        
        return sqr_list