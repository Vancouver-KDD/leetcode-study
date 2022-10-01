class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        
        while b & mask:
            tmp_a = (a ^ b)
            tmp_b = ((a & b) << 1)
            a, b = tmp_a, tmp_b
        
        # if b != 0, overflow occurs
        return (a & mask) if b != 0 else a

