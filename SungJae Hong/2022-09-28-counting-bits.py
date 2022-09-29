from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # create an array with this size.
        dp = [0] * (n + 1)
        # offset starts at 1. 1, 2, 4, 8, 16, 32, etc
        offset = 1
        #start at 1 because offset is 1.
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

# O(n)