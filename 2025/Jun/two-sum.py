class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        res = []
        for index, num in enumerate(nums):
            if num in dict:
                return [dict[num], index]
            dict[target - nums[index]] = index