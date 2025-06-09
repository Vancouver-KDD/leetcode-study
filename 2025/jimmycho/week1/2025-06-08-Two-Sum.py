class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_and_idx = {}
        for idx, num in enumerate(nums):
            num_and_idx[num] = num_and_idx.get(num, [])
            num_and_idx[num].append(idx)
        nums.sort()
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                return [num_and_idx[nums[start]].pop(0), num_and_idx[nums[end]].pop(0)]
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1