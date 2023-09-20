class Solution:
    '''
    for a given number at index i, do a 2 pointer search from i+1 , end
    runtime: O(n^2)
    space: O(n)
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        abs_diff = float('inf')
        result = None

        for i in range(0, len(nums) - 2):
            curr_num = nums[i]
            lo = i + 1
            hi = len(nums) - 1

            while lo < hi:
                curr_sum = curr_num + nums[lo] + nums[hi]

                if curr_sum == target:
                    return target

                if curr_sum < target:
                    lo += 1
                else:
                    hi -= 1

                curr_abs_diff = abs(target - curr_sum)
                if curr_abs_diff < abs_diff:
                    result = curr_sum
                    abs_diff = curr_abs_diff

        return result