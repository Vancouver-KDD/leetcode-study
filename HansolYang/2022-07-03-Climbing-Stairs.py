class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        fir = 1
        sec = 1
        
        for i in range(n-1):
            sec = fir + sec
            fir = sec - fir
            
        return sec