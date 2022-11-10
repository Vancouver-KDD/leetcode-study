class Solution:
    def climbStairs(self, n: int) -> int:
        
        temp = [0 for i in range(n + 1)]
        # r = 5
        # c = 3
        # arr = [[0] * c for _ in range(r)] for 2-D array copy
        # arr[0][0] = 1
        # # for i in range(len(arr)):
        # print(arr)
        temp[0] = 1
        temp[1] = 2
        
        for i in range(2, len(temp)):
            temp[i] = temp[i-1]+temp[i-2]
            
        return temp[n-1]
            
        
        