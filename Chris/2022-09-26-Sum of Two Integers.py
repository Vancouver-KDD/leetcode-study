class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # To limit the size of int to 32 bits as default int in python is 32 bit 
        mask = 0xffffffff
        
        while b&mask > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        return a&mask if b > 0 else a