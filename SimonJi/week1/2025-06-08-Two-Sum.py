class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            sum = target - num
            if sum in hashmap:
                return [hashmap[sum], i]
            hashmap[num] = i