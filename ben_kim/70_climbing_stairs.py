class Solution:
    def climbStairs(self, n: int) -> int:
        res_arr = [0, 1, 2]

        if n <= 2:
            return res_arr[n]
        
        for i in range(3, n):
            res = res_arr[i-1] + res_arr[i-2] # 1
            res_arr.append(res)

        return res_arr[n-1] + res_arr[n-2]

# 1. The number of ways to get to n stair is (n-1)th stair + (n-2)th stair
# n-1 stairs + 1 step
# n-2 stairs + 2 step