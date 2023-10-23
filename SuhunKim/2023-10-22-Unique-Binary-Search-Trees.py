class Solution:
    def numTrees(self, n: int) -> int:
        # method 1: dynamaic programming
        dp = [0 for _ in range(n+1)]
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
                print(dp)
        return dp[-1]
        
        # method 2: catalan number with recursive function for factorial
        def factorial(i):
            if (i == 0 or i == 1): return i
            return i * factorial(i-1)
        
        return int(factorial(2*n) / (factorial(n+1) * factorial(n)))
        
        # method 3: catalan number with built-in factorial function
        return int(math.factorial(2*n) / (math.factorial(n+1) * math.factorial(n)))