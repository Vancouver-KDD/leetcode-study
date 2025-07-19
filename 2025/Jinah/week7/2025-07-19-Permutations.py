from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(head: int):
            if head == len(nums):
                res.append(nums[:])
                return

            for i in range(head, len(nums)):
                nums[head], nums[i] = nums[i], nums[head]
                backtrack(head+1)
                nums[head], nums[i] = nums[i], nums[head]
            
        backtrack(0)
        
        return res