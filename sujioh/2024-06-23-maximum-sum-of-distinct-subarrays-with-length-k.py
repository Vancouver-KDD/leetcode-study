from typing import List
import collections

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        curr_map = collections.Counter(nums[:k])
        curr_sum = sum(nums[:k])
        res = 0 

        if len(curr_map) == k:
            res = curr_sum

        for r in range(k, len(nums)):
            n_r = nums[r]
            n_l = nums[l]
            
            curr_map[n_r] += 1
            curr_map[n_l] -= 1
            
            if curr_map[n_l] == 0:
                del curr_map[n_l]
            
            curr_sum = curr_sum + n_r - n_l 
            
            if len(curr_map) == k:
                res = max(res, curr_sum)
            
            l += 1 

        return res
