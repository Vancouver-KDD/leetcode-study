import collections

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return sum(i > 1 for i in collections.Counter(nums).values())
