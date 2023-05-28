class Solution:
    def countBits(self, n: int) -> List[int]:
        # initial empty array to return 
        ans = [0] * (n+1)

        for i in range (1, (n+1)):
            j = i

            while j != 0:
                count = j % 2

                if count == 1:
                    ans[i] += 1
                j = j // 2 

        return ans
    

    class Solution:
    def countBits(self, n: int) -> List[int]:
        # initial empty array to return 

        """
        dp[]

        offset = 1 
        *2 

        0 = 0000  :  0
        1 = 0001  :  1 = 1 + dp[n-1] (offset = 1)
        2 = 0010  : 1 = 1 + dp[n-2] (offset = 2 )
        3 = 0011  : 2 = 1 + dp[n-2] = 2 (offset =2)
        4 = 0100 : 1 + dp[i-4] of
        5 = 0101 : 1 + dp[1]
        6 = 0110 : 1 + dp[2]
        7 = 0111 : 1 + dp[3] : 3
        8 = 1000 : 1 + dp[i-8]

        """

        dp = [0] * (n+1)
        offset = 1

        for i in range (1,n+1):
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i-offset]

        return dp