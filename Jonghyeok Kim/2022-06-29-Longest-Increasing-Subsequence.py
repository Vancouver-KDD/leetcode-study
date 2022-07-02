from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        num_len = len(nums)
        sub = [1]*num_len
        
        
        for idx, num in enumerate(nums[::-1]):
            if idx != 0:
                for idx2, num2 in enumerate(nums[num_len-idx:]):
                    if num2 > num:
                        sub[num_len-idx-1] = max(sub[num_len-idx-1], 1+sub[num_len-idx+idx2])
        return max(sub)