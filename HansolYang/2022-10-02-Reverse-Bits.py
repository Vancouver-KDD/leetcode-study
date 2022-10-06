class Solution:
    def reverseBits(self, n: int) -> int:
        
        ans = 0
        
        for i in range(32):
            ans = ans | (((n >> i) & 1) << (31 - i))
            
        return ans