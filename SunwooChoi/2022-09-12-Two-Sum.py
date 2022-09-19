class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # store previous values with their index in nums
        val_hash = {}
        
        for idx, num in enumerate(nums):
            target_val = target - num
            if target_val in val_hash:
                return [idx, val_hash[target_val]]
            else:
                # we can overwrite index since we can gaurantee only one solution exists
                val_hash[num] = idx 
        
        assert False, "Answer not found"