class Solution:
    def climbStairs(self, n: int) -> int:
        prev_prev, prev = 0, 1
        
        # distinct way to climb nth stair = (n-1) + (n -2)
        for i in range(n-1):
            prev, prev_prev = prev + prev_prev, prev
            
        return prev_prev + prev
