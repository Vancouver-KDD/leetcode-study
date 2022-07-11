from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
           tmp = max(one+num, two)
           two = one
           one = tmp
        
        return tmp 