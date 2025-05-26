from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, num in enumerate(nums):
            d = target - num

            if d in m:
                return [m[d], i]

            m[num] = i

solution = Solution()
result = solution.twoSum([3,4,5,6], 7)
print(result)
