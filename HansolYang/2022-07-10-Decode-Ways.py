class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if s[0] == "0":
            return 0
        
        if len(s) <= 1:
            return len(s)
        
        fir, sec = 1, 0
        for i in range(len(s)):
            cur = 0
            if s[i] != '0':
                cur = fir
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                cur += sec
            fir, sec = cur, fir
        return fir


#checking the length of the given data
#sometimes it's better to start from the end in Dynamic Programming