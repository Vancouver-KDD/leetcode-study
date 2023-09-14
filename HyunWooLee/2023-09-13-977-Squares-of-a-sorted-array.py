
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        lo, hi = 0, len(nums) - 1
        index = hi

        while lo <= hi:
            lo_num, hi_num = nums[lo] ** 2, nums[hi] ** 2

            if lo_num >= hi_num:
                result[index] = lo_num
                lo += 1
            else:
                result[index] = hi_num
                hi -= 1

            index -= 1
        return result