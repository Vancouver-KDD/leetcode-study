from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for idx, num in enumerate(nums):
            if num in hash:
                return True
            else:
                hash[num] = 1
        return False
