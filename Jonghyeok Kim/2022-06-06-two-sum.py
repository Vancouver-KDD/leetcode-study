from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in hash_map:
                return [index, hash_map[diff]]
            else:
                hash_map[nums[index]] = index
                