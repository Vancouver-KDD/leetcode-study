class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, num in enumerate(nums):
            if target - num in index:
                return [i, index[target - num]]
            index[num] = i