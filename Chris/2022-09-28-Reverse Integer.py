class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        reversed = 0
        isNegative = False
        
        if x < 0:
            x *= -1
            isNegative = True
        
        
        while x%10 == 0:
            x //= 10

        while x>0:
            reversed *= 10
            reversed += (x % 10)
            x //= 10
        
        
        if isNegative:
            reversed *= -1
        
        if reversed < -2**31 or reversed >= 2**31:
            return 0
        
        return reversed
            
            