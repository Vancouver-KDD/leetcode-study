class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # top-down approach
        last_pos = len(nums) -1
        
        for idx in range(len(nums)-1, -1, -1):
            # if last_pos is reachable from idx, set last_pos to idx
            if idx + nums[idx] <= last_pos:
                last_pos = idx
        
        return last_pos == 0 # last_pos is reachable from 0 index