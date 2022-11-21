class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        #go for for loop here: from 1 to len s:
            #using while loop, check whether two are same
            
        def check_palindrome(k, p):
            count = 0
            while k >= 0 and p < len(s) and s[k] == s[p]:
                    count += 1
                    k -=1
                    p += 1
            return count
            
        for i in range(1, len(s)):
            res += (check_palindrome(i, i) + check_palindrome(i-1, i))
        
        return res + 1