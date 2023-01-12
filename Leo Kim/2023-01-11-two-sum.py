class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for k, v in enumerate(nums):
            diff = target - nums[k]

            if diff in seen:
                return [k, seen[diff]]
            else:
                seen[v] = k