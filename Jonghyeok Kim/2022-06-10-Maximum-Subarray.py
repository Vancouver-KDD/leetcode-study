from operator import le
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = nums[0], 0
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sum = max(cur_sum, max_sum)
        return max_sum
    

# Divide and conquer O(nlogn)
def max_crossing_sum(arr, m, l, h):
    right_max, cur_sum = 0, 0
    for idx in range(m, h+1):
        cur_sum += arr[idx]
        right_max = max(right_max, cur_sum)
    left_max, cur_sum = 0, 0
    for idx in range(m-1, l-1, -1):
        cur_sum += arr[idx]
        left_max = max(left_max, cur_sum)
    return max(right_max+left_max, right_max, left_max)

def max_array_sum(arr, l, h):
    if l == h:
        return arr[l]
    m = (l + h) // 2
    return max(max_array_sum(arr,l,m), max_array_sum(arr, m+1, h), max_crossing_sum(arr, m, l, h))