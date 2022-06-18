class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i, nums_set = 0, set()
        while i < len(nums):
            j = len(nums_set)
            nums_set.add(nums[i])
            if j == len(nums_set):
                return True
            i += 1
        return False