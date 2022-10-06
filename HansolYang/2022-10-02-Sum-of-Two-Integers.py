class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        while b != 0:
            temp = a & b
            a = a ^ b
            b = temp << 1
        
        return a