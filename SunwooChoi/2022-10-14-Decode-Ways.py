class Solution:
    def numDecodings(self, s: str) -> int:
        # the first 0 can't be decoded to letter
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s)+1)
        dp[0], dp[1] = 1, 1
        
        for idx in range(2, len(s)+1):
            # when current char is not 0, then we can decode current char as a single digit
            if 0 < (int) (s[idx-1: idx]):
                dp[idx] += dp[idx-1]
            # when current char is within the below range, then we can decode last two digit
            if 10 <= (int) (s[idx-2: idx]) <= 26:
                dp[idx] += dp[idx-2]
        
        return dp[-1]