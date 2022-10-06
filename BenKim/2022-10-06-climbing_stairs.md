# 70. Climbing Stairs

> Problem link: https://leetcode.com/problems/climbing-stairs/  
> [**Python**]submission detail: https://leetcode.com/submissions/detail/816126922/  

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 1칸, 2칸만 이동할 수 있기 때문에 n번째 stair는 n-1번째까지의 도달방법과 n-2까지의 도달방법의 합과 같다
        # n-1 계단 + 1스텝
        # n-2 계탄 + 2스텝         
        dp = [0, 1, 2]
        if n <= 2:
            return dp[n]

        for i in range(3, n):
            tmp = dp[i-1] + dp[i-2]
            dp.append(tmp)

        return dp[n-1] + dp[n-2]
```