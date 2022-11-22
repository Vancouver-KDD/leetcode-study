class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 0:
            return ""
        
        rsf = [0, 0]
        
        def find_pal(k, p):
            while k >= 0 and p < len(s) and s[k] == s[p]:
                k -= 1
                p += 1
            sub = [k+1, p-1]
            return sub
        
        #for loop for each pointer
        #helper returns string 
        for i in range(1, len(s)):
            p1 = find_pal(i, i)
            p2 = find_pal(i-1, i)
            
            if p1[1]-p1[0] > rsf[1]-rsf[0]:
                rsf = p1
            if p2[1]-p2[0] > rsf[1]-rsf[0]:
                rsf = p2
            
        return s[rsf[0]:rsf[1]+1]