
class Solution:
    '''
    Build result form backward
    runtime: O(n)
    space: O(n) // storing result
    '''
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

    '''
    same run time as above, but more verbose 
    - "expand around center"
    - build array from lower number to higer number by finding a pivot where 
     negative/zero number turns into positive. Then do 2 pointers from center to outward
    '''
    def sortedSquaresV2(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        left = 0
        for i in range(1, arr_len - 1):
            if nums[i] <= 0:
                left = i

        right = left + 1
        result = []

        while left >= 0 and right <= arr_len - 1:
            left_num = nums[left] ** 2
            right_num = nums[right] ** 2

            if left_num <= right_num:
                result.append(left_num)
                left -= 1
            else:
                result.append(right_num)
                right += 1

        while left >= 0:
            result.append(nums[left] ** 2)
            left -= 1

        while right <= arr_len - 1:
            result.append(nums[right] ** 2)
            right += 1

        return result