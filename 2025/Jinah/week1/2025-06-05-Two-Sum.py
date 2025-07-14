# Time: 0 ms (100%), Space: 19 MB (24.18%)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in map:
                return [map[comp], idx]
            map[num] = idx