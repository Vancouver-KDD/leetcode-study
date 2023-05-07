class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n = i
            for j in range(i + 1, len(nums)):
                if nums[n] + nums[j] == target:
                    return [n, j]