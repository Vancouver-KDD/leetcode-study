class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        sortednums = sorted(nums)
        for index, item in enumerate(sortednums):
            if index != item:
                return index
        return count
