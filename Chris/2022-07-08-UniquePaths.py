class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def factorial(num:int) -> int:
            
            if num < 1:
                return 1
            
            return num * factorial(num-1)
       
    
    
        return factorial(m+n-2)//factorial(m-1)//factorial(n-1)