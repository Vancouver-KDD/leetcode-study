class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {} # pair of number and index

        for index, num in enumerate(nums):
            if target - num in dict_nums:
                return [index, dict_nums[target - num]]
            dict_nums[num] = index
