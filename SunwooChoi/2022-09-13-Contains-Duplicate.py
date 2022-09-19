class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # delete duplicated elements
        nums_set = set(nums)
        
        return len(nums_set) != len(nums)
