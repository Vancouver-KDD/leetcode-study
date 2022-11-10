class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m ==1 or n == 1:
            return 1
        
        #else:
        #    return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        
        nu = 1
        de = 1
        for i in range(1, m + n - 1):
            nu *= i
        
        for j in range(1, m):
            de *= j
        
        for k in range(1, n):
            de *= k
        
        return nu//de