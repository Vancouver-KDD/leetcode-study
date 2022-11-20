class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxlen = -1
        self.start = 0
        
        def expand_around_center(l, r):
            
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
                
            if r-l-1 > self.maxlen:
                self.maxlen = r-l-1
                self.start = l+1
        
        
        for i in range(len(s)):
            expand_around_center(i,i)
            expand_around_center(i,i+1)
            
        return s[self.start:self.start+self.maxlen]
        
        
        
        
                
                                
                    
                
                
            