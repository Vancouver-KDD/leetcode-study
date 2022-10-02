class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 1:
            if (n & 1):
                count += 1
            
            n = n >> 1
        
        return count if n != 1 else count + 1