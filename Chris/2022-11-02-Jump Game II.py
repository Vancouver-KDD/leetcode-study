class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cur = 0
        farthest = 0
        jumps = 0
        curEnd = 0
        while cur < len(nums)-1:
            farthest = max(cur+nums[cur], farthest)
            
            
            
            # At the end of farthest we can go from previous jump, 
            if cur == curEnd:
                # Pick the farthest reacheable index on the way to get this point from previous jump
                curEnd = farthest
                jumps += 1
            
            cur += 1
        
        return jumps
            