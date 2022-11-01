from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.small_rob(nums[1:]), self.small_rob(nums[:-1]))
    
    def small_rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
           tmp = max(one+num, two)
           two = one
           one = tmp
        return tmp 