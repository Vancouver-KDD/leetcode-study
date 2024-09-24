class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums):
            rest = target - num
            if rest in seen.keys():
                return [seen[rest], index]
            seen[num] = index
        return -1