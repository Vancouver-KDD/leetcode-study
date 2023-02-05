class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}

        for idx in range(len(nums)):
            find_num = target - nums[idx]
            if find_num in prev_nums:
                return [idx, prev_nums[find_num]]
            prev_nums[nums[idx]] = idx
