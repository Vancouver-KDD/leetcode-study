# Input: nums = [2,7,11,15], target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target-num], i]
            else:
                num_map[num] = i 
        